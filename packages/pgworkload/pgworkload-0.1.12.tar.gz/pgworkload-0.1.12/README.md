# pgworkload - workload utility for the PostgreSQL protocol

## Overview

The goal of `pgworkload` is to ease the creation of workload scripts by providing a utility with the most common functionality already implemented.

`pgworkload` is run in conjunction with a user supplied Python `class`. This class defines the workload transactions and flow.

The user has complete control of what statements the transactions actually execute, and what transactions are executed in which order.

`pgworkload` can seed a database with random generated data, whose definition is supplied in a YAML file and can be extracted from a DDL SQL file.

## Example

Class `Bank` in file `workloads/bank.py` is an example of one such user-created workload.
The class defines 3 simple transactions that have to be executed by `pgworkload`.
Have a look at the `bank.py`, `bank.yaml` and `bank.sql` in the `workload` folder in this project.

Head to file `workload/bank.sql` to see what the database schema look like. We have 2 tables:

- the `transactions` table, where we record the bank payment transactions.
- the `ref_data` table.

Take a close look at this last table: each column represent a different type, which brings us to the next file.

File `bank.yaml` is the data generation definition file.
For each column of table `ref_data`, we deterministically generate random data.
This file is meant as a guide to show what type of data can be generated, and what args are required.

File `bank.py` defines the workload.
The workload is defined as a class object.
The class defines 2 methods: `run()` and the constructor, `__init__()`.
All other methods are part of the application logic of the workload.
Read the comments along the code for more information.

Let's run the sample **Bank** workload.

### Step 0 - env setup

```bash
# upgrade pip - must have pip version 20.3+ 
pip3 install --upgrade pip

pip3 install pgworkload

mkdir workloads
cd workloads

# the workload class
wget https://raw.githubusercontent.com/fabiog1901/pgworkload/main/workloads/bank.py

# the DDL file
wget https://raw.githubusercontent.com/fabiog1901/pgworkload/main/workloads/bank.sql

# the data generation definition file
wget https://raw.githubusercontent.com/fabiog1901/pgworkload/main/workloads/bank.yaml
```

### Step 1 - init the workload

Make sure your **CockroachDB** cluster or **PostgreSQL** server is up and running.

Connect to the SQL prompt and load the `bank.sql` file.
In CockroachDB, you can run

```sql
sql> \i bank.sql
```

Next, generate some CSV data to seed the database:

```bash
pgworkload util csv -i bank.yaml -x 1
```

The CSV files will be located inside a `bank` directory.

```bash
$ ls -lh bank
total 1032
-rw-r--r--  1 fabio  staff   513K Apr  9 13:01 ref_data.0_0_0.csv
```

Now you can import the CSV file.
In CockroachDB, my favorite method is to use a webserver to serve the CSV file.
Open a new terminal then start a simple python server

```bash
cd workloads
cd bank
python3 -m http.server 3000
```

If you open your browser at <http://localhost:3000> you should see file `ref_data.0_0_0.csv` being served.

At the SQL prompt, import the file

```sql
sql> IMPORT INTO ref_data CSV DATA ('http://localhost:3000/ref_data.0_0_0.csv') WITH delimiter = e'\t'; 
```

### Step 2 - Run the workload

Run the workload using 8 connections for 120 seconds or 100k cycles, whichever comes first.

```bash
# CockroachDB
pgworkload run -w bank.py -c 8 --url 'postgres://root@localhost:26257/bank?sslmode=disable&application_name=Bank' -d 120 -i 100000

# PostgreSQL
pgworkload run -w bank.py -c 8 --url 'postgres://root@localhost:5432/bank?sslmode=disable&application_name=Bank' -d 120 -i 100000
```

`pgworkload` uses exclusively the excellent [Psycopg 3](https://www.psycopg.org/psycopg3/docs/) to connect.
No other ORMs or drivers/libraries are used.
Psycopg has a very simple, neat way to [create connections and execute statements](https://www.psycopg.org/psycopg3/docs/basic/usage.html) and [transactions](https://www.psycopg.org/psycopg3/docs/basic/transactions.html).

`pgworkload` will output something like below

```text
2022-01-28 17:22:43,893 [INFO] (MainProcess 29511) URL: 'postgres://root@localhost:26257/bank?sslmode=disable&application_name=Bank'
id               elapsed    tot_ops    tot_ops/s    period_ops    period_ops/s    mean(ms)    p50(ms)    p90(ms)    p95(ms)    p99(ms)    pMax(ms)
-------------  ---------  ---------  -----------  ------------  --------------  ----------  ---------  ---------  ---------  ---------  ----------
__cycle__             10       1342       133.72          1342           134.2       54.9       35.76     165.94     192.89     245.42      333.6
read                  10       1215       121.03          1215           121.5       41.11      19.58     113.21     146.79     208.86      291.02
txn1_new              10        130        12.95           130            13         48.29      53.81      74.7       90.84      95.66      108.37
txn2_verify           10        129        12.85           129            12.9       70.9       73.73      94.3       99.69     137.99      164.96
txn3_finalize         10        127        12.65           127            12.7       67.21      72.48      93.64     105.97     129.57      166 

[...]

2022-01-28 17:24:44,765 [INFO] (MainProcess 29511) Requested iteration/duration limit reached. Printing final stats
id               elapsed    tot_ops    tot_ops/s    period_ops    period_ops/s    mean(ms)    p50(ms)    p90(ms)    p95(ms)    p99(ms)    pMax(ms)
-------------  ---------  ---------  -----------  ------------  --------------  ----------  ---------  ---------  ---------  ---------  ----------
__cycle__            121      14519       120.12            66             6.6       94.08      96.68     203.74     216.83     242.24      262.69
read                 121      13050       107.96            54             5.4       70.6       62.7      127.88     151.29     203.52      203.62
txn1_new             121       1469        12.15             7             0.7       51.08      51.07      71.71      73.66      75.23       75.62
txn2_verify          121       1469        12.15            11             1.1       70.52      76.92     102.31     102.32     102.33      102.33
txn3_finalize        121       1469        12.15            12             1.2       81.19      98.97     103.88     103.97     103.98      103.98 
```

There are many built-in options.
Check them out with

```bash
pgworkload --help
```

## How it works

It’s helpful to understand first what `pgworkload` does:

- At runtime, `pgworkload` first imports the class you pass, `bank.py`.
- It spawns _n_ threads for concurrent execution (see next section on Concurrency).
- By default, it sets the connection to `autocommit` mode.
- **psycopg v3** will _PREPARE_ statements automatically after 5 executions.
- Each thread creates a database connection - no need for a connection pool.
- In a loop, `pgworkload` will:
  - execute function `run()` which returns a list of functions.
  - execute each function in the list sequentially. Each function, typically, executes a SQL statement/transaction.
- Execution stats are funneled back to the _MainThread_, which aggregates and prints them to _stdout_.
- If the connection drops, it will recreate it. You can also program how long you want the connection to last.
- `pgworkload` stops once a limit has been reached (iteration/duration), or you Ctrl+C.

## Concurrency - processes and threads

`pgworkload` uses both the `multiprocessing` and `threading` library to achieve high concurrency, that is, opening multiple connections to the DBMS.

There are 2 parameters that can be used to configure how many processes you want to create, and for each process, how many threads:

- `--procs`, or `-x`, to configure the count of processes (defaults to the CPU count)
- `--concurrency`, or `-c`, to configure the total number of executing workloads to run (also referred to as _executing threads_)

`pgworkload` will spread the load across the processes, so that each process has an even amount of threads.

Example: if we set `--procs 4` and `--concurrency 10`, pgworkload will create as follows:

- Process-1: MainThread + 1 extra threads. Total = 2
- Process-2: MainThread + 1 extra threads. Total = 2
- Process-3: MainThread + 2 extra thread.  Total = 3
- Process-4: MainThread + 2 extra thread.  Total = 3

Total workloads = 10

This allows you to fine tune the count of Python processes and threads to fit your system.

Furthermore, each _executing thread_ receives a unique ID (an integer).
The ID is passed to the workload class with function `setup()`, along with the total count of threads, i.e. the value passed to `-c/--concurrency`.
You can leverage the ID and the thread count in various ways, for example, to have each thread process a subset of a dataset.

## Generating CSV files

- You can seed a database quickly by letting `pgworkload` generate pseudo-random data and import it.
- `pgworkload` takes the DDL as an input and creates an intermediate YAML file, with the definition of what data you want to create (a string, a number, a date, a bool..) based on the column data type.
- You then refine the YAML file to suit your needs, for example, the size of the string, a range for a date, the precision for a decimal, a choice among a discrete list of values..
- You can also specify what is the percentage of NULL for any column, or how many elements in an ARRAY type.
- You then specify the total row count, how many rows per file, and in what order, if any, to sort by.
- Then `pgworkload` will generate the data into CSV or TSV files, compress them if so requested.
- You can then optionally merge-sort the files using command `merge`.

Write up blog: [Generate multiple large sorted csv files with pseudo-random data](https://dev.to/cockroachlabs/generate-multiple-large-sorted-csv-files-with-pseudo-random-data-1jo4)

Find out more on the `yaml`, `csv` and `merge` commands by running

```bash
pgworkload util --help
```

Consult file `workloads/bank.yaml` for a list of all available generators and options.

## Built-in Workloads

`pgworkload` has the following workload already built-in and can be called without the need to pass a class file

### Querybench

Querybench runs a list of SQL Statements sequentially and iteratively.
It assumes the schema and data have been created and loaded.

SQL statements file `mystmts.sql`

```sql
-- Query 1
select 1;
select 
  version();
-- select now();

-- Query 2
SELECT * FROM my_table 
WHERE id = 1234;
```

Run **Querybench** like this:

```bash
pgworkload run --builtin-workload Querybench --args mystmts.sql --url <conn-string>
```

## Acknowledgments

Some methods and classes have been taken and modified from, or inspired by, <https://github.com/cockroachdb/movr>
