# N26_data_task_10_2022

## Instructions to test the solutions

This directory contains some files that can be used to understand the solution and how to test it .

This is project structure 

n26_data_task_10_2022/
│__ init-db/
|   |__init.sql                          # To initialize data directly to postgres sql for test1.py testing
|   |
├── src/                                 # Section folder containing task-related resources
│   ├── init-fixtures/                   # Folder containing necessary data for creating tables and inserting data
|   |   |__task1.sql                     # table creation and sample data for task1
|   |   |__task2.sql
|   |   |__task3.sql
|   |   
│   ├── output_expected/                 # Folder containing expected outputs for each task
│   │   ├── task1_output.csv             # Expected output for Task 1
│   │   ├── task2_output.csv             # Expected output for Task 2
│   │   ├── task3_output.csv             # Expected output for Task 3
│   ├── solution_obtained/               # Folder containing actual solutions (code) for each task
│   │   ├── task1.py                     # Python code solution for Task 1
│   │   ├── task2.sql                    # SQL code solution for Task 2
│   │   ├── task3.sql                    # SQL code solution for Task 3
│
├── test/                                # Folder containing test cases for all tasks
│   ├── test_task1.py                    # Test cases for Task 1 (Python)
│   ├── test_task2.py                    # Test cases for Task 2 (SQL)
│   ├── test_task3.py                    # Test cases for Task 3 (SQL)
│
|                                      
├── transactions.csv                     # Input transaction data for Task 1
├── users.csv                            # Input user data for Task 1
│
├                                        
├── Dockerfile                           # Dockerfile to build the container for running the Python code
├── docker-compose.yaml                  # Docker Compose configuration for setting up services
│
├── generate_data.py                     # Python script to generate transaction and user data
├── requirements.txt                     # File containing dependencies (for Python)
├── tasks.md                             # Markdown file describing each task
└── README.md                            # Project overview and instructions for running


This is how it works:

  * Launch the Docker packaged PostgreSQL database server with:

  * setup virtual env need to be setup as well and please run requirements.txt file to run the testcases


    ```
   1.  docker-compose up
   This will setup the environment and start the database server.

   2. When this docker compose will run you can see task1 will run automatically and will generate the standard output in the terminal with that test cases will be also completed which is present inside the test folder.

   otherwise you can also manually run  solution_obtained-->task1.py manually in vs code to get the output and run the test case using pytest C:\<path of your computer>\N26_data_task_10_2022\test\test_task1.py

   3. once docker-compseup will execute database will get setup i.e postgres database
     Start Docker Compose: Run docker-compose up --build to build and start your services.

    PostgreSQL Initialization: When the postgres-container starts, it will automatically initialize the database by running the COPY commands from the SQL scripts in /docker-entrypoint-initdb.d/.

    Python Script Execution: The feature-table-computation container will run your Python script (task1.py) and execute the test (test_task1.py) once the database is initialized. 

   How to test sql queries in postgres ??

    go to dbeaver --> File --> new connection --> postgres --> authentication = database native 

    give username ='test' and password ='test' hit on test connections your database will be connected 

## Task 1 

 Issues Found :-

 1. when i was running the query mentioned in the task 
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

steps and idea behind this task:-
1. It calculates the sum of transaction amounts and the number of distinct users for each transaction category, filtering out blocked transactions and inactive users.

The TransactionAnalysis class encapsulates the entire process of loading data, computing results, and printing them

The script processes transaction and user data from CSV files. Here's a summary of its workflow:

1. **`TransactionAnalysis` Class**:
   - **`load_users`**: Loads user data from `users.csv`, mapping user IDs to their active status (True/False).
   - **`load_transactions`**: Loads transaction data from `transactions.csv`, including details like transaction ID, amount, and category.
   - **`compute_results`**: Filters out blocked transactions and inactive users, then calculates the total transaction amount and distinct user count per category.
   - **`print_results`**: Outputs the computed results (category ID, sum of transactions, user count) in CSV format.

2. **Main Flow**:
   - The `main` function loads the data, computes the results, and prints them.
   - Errors (e.g., file not found or invalid data) are logged, and the script exits with an error code if necessary.

The script uses logging for error handling and assumes valid CSV files with necessary columns (`user_id`, `is_active`, `transaction_id`, etc.).


Note :- There could be some potential errors as well which can be occured but not handled in the code .

File Not Found (FileNotFoundError): If transactions.csv or users.csv is missing or the path is incorrect.

