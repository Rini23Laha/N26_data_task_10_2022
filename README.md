# N26 Data Task (10/2022)

Hello Team,
My name is Rini Laha, and I bring nearly 7 years of experience as a Data Engineer, specializing in data analytics, big data frameworks, and cloud technologies, particularly AWS. I am currently working as a Lead Data Engineer at JP Morgan & Chase, where I manage and process large-scale datasets using tools such as Airflow, Python, PySpark, and SQL.

# Table of Contents:

1. Project Structure
2. 5. Project Setup
3. Requirements
4. Running the Solution
5. How to Test SQL Queries in PostgreSQL

6. Task Descriptions
   - Task 1
   - Task 2
   - Task 3
7. Known Issues and Troubleshooting

## Project Structure

n26_data_task_10_2022/
|
├── src/                               # Task-related resources
│   ├── init-fixtures/                 # SQL scripts for creating tables and loading dummy data
│   │   ├── task1.sql                  # SQL for Task 1 table creation and sample data
│   │   ├── task2.sql                  # SQL for Task 2 table creation and sample data
│   │   ├── task3.sql                  # SQL for Task 3 table creation and sample data
│   │
│   ├── output_expected/               # Expected outputs for each task in CSV format
│   │   ├── task1_output.csv           # Expected output for Task 1
│   │   ├── task2_output.csv           # Expected output for Task 2
│   │   ├── task3_output.csv           # Expected output for Task 3
│   ├── solution_obtained/             # Solution code for each task
│   │   ├── task1.py                   # Python code for Task 1 (Transaction Analysis)
│   │   ├── task2.sql                  # SQL solution for Task 2 (User Transaction Count)
│   │   ├── task3.sql                  # SQL solution for Task 3 (Removing Redundant Records)
│
├── test/                              # Test cases for each task
│   ├── test_task1.py                  # Test cases for Task 1 (Python-based)
│   ├── test_task2.py                  # Test cases for Task 2 (SQL-based)
│   ├── test_task3.py                  # Test cases for Task 3 (SQL-based)
│
├── transactions.csv                   # Transaction data for Task 1
├── users.csv                          # User data for Task 1
│
├── Dockerfile-python                  # Dockerfile for the Python environment
├── Dockerfile-postgres                # Dockerfile for PostgreSQL environment
├── docker-compose.yaml                # Configuration file to build and run Docker containers
│
├── generate_data.py                   # Script to generate transaction and user data
├── requirements.txt                   # Python dependencies
└── README.md                          # Project overview


## Project Setup
How do I set up the project environment?

1. Install Docker & Docker Compose:

- The project relies on Docker to spin up the PostgreSQL database and the Python environment.
- Make sure Docker and Docker Compose are installed on your machine. Follow the official installation instructions for Docker and Docker Compose.

2. Set up the Docker Containers:
 - Once Docker is installed, navigate to the project folder in your terminal.
 - Run the following command to build the Docker images:
bash
   docker-compose build
- Then, run the Docker Compose to bring up the PostgreSQL container:
   docker-compose up
This will start up the PostgreSQL container, initializing the database and loading necessary data from the SQL files (e.g., task1.sql, task2.sql, task3.sql) located in the src/init-fixtures/ folder.

3. Set up the Virtual Environment for Python:
- Create a virtual environment for the Python dependencies by running: python -m venv venv.
- Activate the virtual environment:
  On macOS/Linux: source venv/bin/activate
- On Windows: venv\Scripts\activate
- pip install -r requirements.txt

4. Verify the PostgreSQL Database Setup:

- The docker-compose will automatically load the necessary data into the PostgreSQL database. You can verify this by connecting to the database using a tool like DBeaver

## Requirements

What dependencies are needed to run the project?

Make sure you have the following installed:

- Docker: Required to run the PostgreSQL database and Python application in isolated containers.
- Python 3.x: Needed to run the Python script for Task 1.
- PostgreSQL: If not using Docker, you can set up PostgreSQL manually on your machine.
- Python dependencies are listed in the requirements.txt file, which includes necessary libraries such as:

psycopg2: PostgreSQL database adapter for Python.
pytest: For running unit tests.
## Running the Solution

How do I run the solution automatically?

Once you've followed the setup steps and the Docker containers are up and running, the system will automatically execute the Python script (task1.py) and run the associated test cases defined in test_task1.py. This ensures that the system is verified automatically.

How do I run the solution manually?

1. Running Python Scripts:
 - If you prefer to manually run the solution, navigate to src/solution_obtained/ and execute the Python script for Task 1:
  python task1.py
- To run the tests for Task 1, use pytest please navigate to test folder/test_task1.py
  pytest test/test_task1.py

2. Running SQL Queries:

- You can manually run the SQL queries in PostgreSQL using a database client like DBeaver.
  - Connect to the PostgreSQL database with the following credentials
  - Host: localhost
  - Database: postgres
  - Username: test
  - Password: test

- Run the necessary SQL queries located in the src/solution_obtained/ directory for each task, and check the results against the expected output in src/output_expected/.

# How to Test SQL Queries in PostgreSQL

once you will run docker compose command in vs code terminal containers will be created please use postgres from Dbeaver for better experience.

# How can I test the SQL queries for the tasks?
1. Using DBeaver:

 - Open DBeaver, go to File → New Connection → PostgreSQL.
  Enter the following credentials:
 - Username: test
 - Password: test
 - Host: localhost
 - Database: postgres

After testing the connection, click OK to establish the connection to the PostgreSQL database.
2. Inserting Data into the Database:

  - For each task, you will find SQL scripts in the src/   init-fixtures/ folder (e.g., task1.sql, task2.sql, task3.sql).
  - Execute these SQL scripts in DBeaver to create the necessary tables and populate them with dummy data from transactions.csv and users.csv.

3. Running the Queries:

  - After loading the tables, you can execute the corresponding SQL queries found in src/solution_obtained/ (e.g., task2.sql, task3.sql).
  - Check the results against the expected outputs in src/output_expected/ to ensure correctness.

  
## Task Descriptions

# Task 1 - Transaction Analysis (Python Script)

Objective:
- Calculate the sum of transaction amounts and the number of distinct users for each transaction category, while filtering out blocked transactions and inactive users.

Solution Details:

when i was running the query mentioned in the task 
 SELECT
t.transaction_category_id,
SUM(t.transaction_amount) AS sum_amount,
COUNT(DISTINCT t.user_id) AS num_users
FROM transactions t
JOIN users u USING (user_id)
WHERE t.is_blocked = False
AND u.is_active = 1
GROUP BY t.transaction_category_id
ORDER BY sum_amount DESC;

i got this error -: ERROR: operator does not exist: boolean = integer
  Hint: No operator matches the given name and argument types. You might need to add explicit type casts.
the reason behind is is_active=1 while in data its true either we have to type cast it to either true  as 1 or run the query without changing this has been done using python code in more effective way .

- steps and idea behind this task:-
1. It calculates the sum of transaction amounts and the number of distinct users for each transaction category, filtering out blocked transactions and inactive users.

- The TransactionAnalysis class encapsulates the entire process of loading data, computing results, and printing them.
- The script processes transaction and user data from CSV files. Here's a summary of its workflow:

1. **`TransactionAnalysis` Class**:
   - **`load_users`**: Loads user data from `users.csv`, mapping user IDs to their active status (True/False).
   - **`load_transactions`**: Loads transaction data from `transactions.csv`, including details like transaction ID, amount, and category.
   - **`compute_results`**: Filters out blocked transactions and inactive users, then calculates the total transaction amount and distinct user count per category.
   - **`print_results`**: Outputs the computed results (category ID, sum of transactions, user count) in CSV format.

2. **Main Flow**:
     - The `main` function loads the data, computes the results, and prints them.
     - Errors (e.g., file not found or invalid data) are logged, and the script exits with an error code if necessary.

The script uses logging for error handling and assumes valid CSV files with necessary columns (`user_id`, `is_active`, `transaction_id`, etc.).

Error observation 

Note :- There could be some potential errors as well which can be occured but not handled in the code .
like data duplicate ,division by 0 or invalid sum , empty transaction or no users data which can be handled more gracefully in this code.

I also tried to load the full data of transaction.csv and users.csv into the athena database using both psycopy and using docker init.sql but i was getting the error ERROR: missing data for column "user_id"
  Where: COPY transactions, line 2: ""
  not  sure of the reason but please do let me know.

### Task 2 

Objective :
Sql script to calculate the number of transactions a user had within the previous seven days for each transaction, we can write a SQL query using a self-join and a date range condition.

Solution: 
 The SQL query to achieve this can be written using a JOIN operation to compare each transaction with the other transactions from the same user and calculate how many of them fall within the previous 7 days.

Assuming the transactions table has the following schema: please refer init-fixtures/task2.sql

transaction_id: Unique identifier for the transaction
user_id: The identifier of the user who made the transaction
date: The date when the transaction occurred

Here t1 and t2 were two tables t1 as current transaction and t2 as previous transaction

- FROM transactions t1: This is the main table, transactions, aliased as t1. We will use this as the reference for each transaction.

- LEFT JOIN transactions t2: We join the same transactions table again, but this time, we alias it as t2. This will allow us to compare the current transaction (t1) to all others (t2) made by the same user (t1.user_id = t2.user_id).

- ON t1.user_id = t2.user_id AND t2.date > t1.date AND t2.date <= t1.date + INTERVAL '7 days':

   - We ensure that we are only looking at transactions made by the same user (t1.user_id = t2.user_id).
   - We ensure that t2.date > t1.date to exclude the current transaction (since the problem statement specifies not to count the current transaction).
   - We then check if t2.date falls within the next 7 days (t2.date <= t1.date + INTERVAL '7 days').
   - COUNT(t2.transaction_id): This counts how many transactions the user made in the 7-day window.

   - GROUP BY t1.transaction_id, t1.user_id, t1.date: We group by each transaction in t1, so the count is computed for each transaction separately.

   - ORDER BY t1.date: Finally, we order the result by the transaction date for better readability and sequence.


---  What Happens Under the Hood in the Database Engine:---

1. query parsing --> checks the syntax errors 
2. query planning --> Database will generate query execution plan
   PostgreSQL’s query planner determines how to execute the query in the most efficient way based on available indexes, table sizes, and any statistics gathered about the distribution of data in the table.
3. join processing --> Then the join operation will take place based on primary key for both the table and      
   necessary lookups to find and match the appropriate rows from the t2 side of the join.
4. Filtering: After the join, the database engine applies the t2.date > t1.date AND t2.date <= t1.date +   INTERVAL   '7 days' condition to ensure that only relevant transactions from the past week are considered.
5. Aggregation: After the joins and filtering, the database engine computes the COUNT(t2.transaction_id) for each   group of transactions (grouped by t1.transaction_id, t1.user_id, and t1.date). This step aggregates the number of transactions for each user within the specified time window.

6. Sorting: Finally, the results are ordered by t1.user_id and t1.date.

--  Considerations for Efficient Query Execution:---


When executing this query, the database engine considers several factors to optimize the query performance:

- Indexes: The database will likely use indexes on the user_id and date columns of the transactions table. These indexes will help to quickly find all transactions for a given user and to filter transactions that fall within the 7-day window.

- Join Strategy: The engine decides the optimal join strategy. A hash join could be used if the dataset is large and there's no appropriate index, while a nested loop join might be used if the tables are small or there are useful indexes.

- Cost Estimation: The database’s query planner estimates the cost of various operations (such as sorting, joining, and filtering). It uses statistics on table sizes, index availability, and distribution of data to choose the most cost-effective strategy.

- Materialization: In some cases, PostgreSQL might create temporary results (or "materialize") if the intermediate results of the join or filtering are large. Materialization could slow down performance, especially if the intermediate tables are large.

- Parallel Query Execution: If the transactions table is very large and the server has enough resources, PostgreSQL might opt for parallel query execution to speed up the process.


## Task 3

Objective :
SQL script to clean up redundant records from a table dim_dep_agreement. The redundant records occur when none of the business attributes (i.e., client_id, product_id, interest_rate) change for a given agrmnt_id, causing unnecessary rows. The goal is to "collapse" such redundant records and create a new table dim_dep_agreement_compacted.

Note :- 
using the data present in init-fixtures task3 create a table and try to query how it looks like and how we can correct it as per the requirement i need to create clear table  dim_dep_agreement_compacted which will contain contain only clean data.

1. This can be achieved by  first ROW_NUMBER() generates a sequential number based on the agrmnt_id (Agreement ID), ordered by actual_from_dt. This provides a way to distinguish individual rows.
The second ROW_NUMBER() generates a sequence based on agrmnt_id, client_id, product_id, and interest_rate (the business attributes). If these values are the same for consecutive rows, they will have the same ROW_NUMBER().
Then i have to find the difference between these two row numbers.

2.  The difference between these two ROW_NUMBER() results (ROW_NUMBER() - ROW_NUMBER()) creates a grp (group) identifier. For rows where the business attributes (client_id, product_id, interest_rate) do not change, the grp value will remain the same.
The rows with the same grp value are identified as part of a redundant group and will be merged.

3.  Main SELECT with GROUP BY:
The GROUP BY clause groups the rows by agrmnt_id, client_id, product_id, interest_rate, and grp. This ensures that redundant records with the same values are combined into a single row.
For each group:
MIN(actual_from_dt) gives the earliest start date.
MAX(actual_to_dt) gives the latest end date, collapsing the period.
MIN(sk) gets the first sk (Surrogate Key) for each group.

4. Final Ordering:
The results are ordered by agrmnt_id and actual_from_dt to maintain the chronological order of the agreement changes.

## Known Issues and Troubleshooting

What if I encounter errors during setup?

Incase of the setup issue please use virtual env

what if there is any other way of doing the sql queries ?

There will be potential way of doing the queries but based on my understanding and knowledge i have written the code we can discuss if there will be any other best approaches.

what if i dont have dbeaver ?

Dbeaver is the open source tool that can be downloaded easily from google for setup related issues i would suggest to watch this video - https://www.youtube.com/watch?v=RdPYA-wDhTA&t=535s

How i can verify if the ooutput is correct ?

In the output_expected/{task.csv} i have added the output which i have received after running the code please do reverify them.