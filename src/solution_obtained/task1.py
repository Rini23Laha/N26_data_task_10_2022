import csv
from collections import defaultdict
from uuid import UUID
import logging

# Set up logging for the script
logging.basicConfig(level=logging.INFO)

class TransactionAnalysis:
    def __init__(self, transactions_file, users_file):
        """
        Initializes the class with file paths for transactions and users CSV files.
        """
        self.transactions_file = transactions_file  # Path to the transactions CSV file
        self.users_file = users_file  # Path to the users CSV file
        self.users_data = {}  # Dictionary to store users data
        self.transactions_data = []  # List to store transactions data

    def load_users(self):
        """
        Loads user data from the users.csv file into a dictionary.
        The dictionary maps user_id to is_active (True/False).
        """
        try:
            with open(self.users_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # Check if user_id and is_active are present
                        if 'user_id' not in row or 'is_active' not in row:
                            raise KeyError("Missing 'user_id' or 'is_active' column in the row.")
                        
                        user_id = UUID(row['user_id'])  # Convert user_id to UUID
                        is_active = row['is_active'] == 'True'  # Convert 'True'/'False' to boolean
                        self.users_data[user_id] = is_active
                    except KeyError as e:
                        logging.error(f"Missing key {e} in {self.users_file} row: {row}")
                        continue
                    except ValueError as e:
                        logging.error(f"Invalid user data in {self.users_file} row: {row}, Error: {e}")
                        continue
        except FileNotFoundError:
            logging.error(f"Error: File {self.users_file} not found.")
            raise
        except Exception as e:
            logging.error(f"Unexpected error while loading users: {e}")
            raise

    def load_transactions(self):
        """
        Loads transaction data from the transactions.csv file into a list.
        Each transaction is stored as a dictionary with necessary fields.
        """
        try:
            with open(self.transactions_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        # Check for missing required fields
                        if 'transaction_id' not in row or 'user_id' not in row or 'transaction_amount' not in row or 'transaction_category_id' not in row:
                            raise KeyError("Missing required column(s) in the transaction row.")

                        transaction = {
                            'transaction_id': UUID(row['transaction_id']),  # Convert to UUID
                            'date': row['date'],  # Assuming date format is correct
                            'user_id': UUID(row['user_id']),  # Convert user_id to UUID
                            'is_blocked': row['is_blocked'] == 'True',  # Convert 'True'/'False' to boolean
                            'transaction_amount': float(row['transaction_amount']),  # Convert to float
                            'transaction_category_id': int(row['transaction_category_id'])  # Convert to int
                        }
                        self.transactions_data.append(transaction)
                    except KeyError as e:
                        logging.error(f"Missing key {e} in {self.transactions_file} row: {row}")
                        continue
                    except ValueError as e:
                        logging.error(f"Invalid transaction data in {self.transactions_file} row: {row}, Error: {e}")
                        continue
        except FileNotFoundError:
            logging.error(f"Error: File {self.transactions_file} not found.")
            raise
        except Exception as e:
            logging.error(f"Unexpected error while loading transactions: {e}")
            raise

    def compute_results(self):
        """
        Computes the results equivalent to the SQL query:
        - Filters transactions based on 'is_blocked' and 'is_active' status
        - Groups transactions by category and sums the amounts
        - Counts the distinct users per category
        """
        result = defaultdict(lambda: {'sum_amount': 0, 'num_users': set()})

        # Check if there's any valid data loaded
        if not self.transactions_data:
            logging.warning("No transactions data found.")
        
        # Iterate over all transactions to calculate the required results
        for transaction in self.transactions_data:
            # Filter transactions where 'is_blocked' is False
            if not transaction['is_blocked']:
                user_id = transaction['user_id']
                # Check if user is active and exists in the users_data dictionary
                if user_id in self.users_data and self.users_data[user_id]:
                    category_id = transaction['transaction_category_id']
                    # Accumulate sum and track unique users for each category
                    result[category_id]['sum_amount'] += float(transaction['transaction_amount'])
                    result[category_id]['num_users'].add(user_id)

        # Convert the results to a list of dicts for easy assertion in tests
        final_result = [{'transaction_category_id': category_id, 'sum_amount': data['sum_amount'], 'num_users': len(data['num_users'])}
                        for category_id, data in result.items()]

        # Handle case where no results are found
        if not final_result:
            logging.warning("No valid results after computation.")
        
        return final_result

    def print_results(self, results):
        """
        Prints the results to stdout with the appropriate header.
        """
        if not results:
            print("No results found.")
            return

        # Print header
        print("transaction_category_id,sum_amount,num_users")
        # Print each result in the required format
        for result in results:
            print(f"{result['transaction_category_id']},{result['sum_amount']},{result['num_users']}")

def main():
    """
    Main function to initialize the analysis, load data, compute results, and print them.
    """
    # Specify the paths to the CSV files
    transactions_file = 'transactions.csv'  # Path to the transactions CSV file
    users_file = 'users.csv'  # Path to the users CSV file

    # Create an instance of TransactionAnalysis
    analysis = TransactionAnalysis(transactions_file, users_file)

    try:
        # Load the users and transactions data
        analysis.load_users()
        analysis.load_transactions()

        # Compute the results based on the loaded data
        results = analysis.compute_results()

        # Print the computed results to stdout
        analysis.print_results(results)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)  # Exit with error code if something goes wrong

if __name__ == '__main__':
    main()  # Call the main function when the script is executed
