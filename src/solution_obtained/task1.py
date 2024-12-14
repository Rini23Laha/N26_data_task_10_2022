import csv
from collections import defaultdict
from uuid import UUID
import logging

# Set up logging for the script
logging.basicConfig(level=logging.INFO)

class TransactionAnalysis:
    def __init__(self, transactions_file, users_file):
        self.transactions_file = transactions_file
        self.users_file = users_file
        self.users_data = {}  # Dictionary to store users data
        self.transactions_data = []  # List to store transactions data

    def load_users(self):
        """
        Loads user data from the users.csv file into a dictionary.
        """
        try:
            with open(self.users_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        user_id = UUID(row['user_id'])  # Convert user_id to UUID
                        is_active = row['is_active'] == 'True'  # Convert 'True'/'False' to boolean
                        self.users_data[user_id] = is_active
                    except ValueError as e:
                        logging.error(f"Invalid user data: {e} for row {row}")
        except FileNotFoundError:
            logging.error(f"Error: File {self.users_file} not found.")
            raise

    def load_transactions(self):
        """
        Loads transaction data from the transactions.csv file into a list.
        """
        try:
            with open(self.transactions_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        transaction = {
                            'transaction_id': UUID(row['transaction_id']),  # Convert to UUID
                            'date': row['date'],  # Assuming date format is correct
                            'user_id': UUID(row['user_id']),  # Convert user_id to UUID
                            'is_blocked': row['is_blocked'] == 'True',  # Convert 'True'/'False' to boolean
                            'transaction_amount': float(row['transaction_amount']),  # Convert to float
                            'transaction_category_id': int(row['transaction_category_id'])  # Convert to int
                        }
                        self.transactions_data.append(transaction)
                    except ValueError as e:
                        logging.error(f"Invalid transaction data: {e} for row {row}")
        except FileNotFoundError:
            logging.error(f"Error: File {self.transactions_file} not found.")
            raise

    def compute_results(self):
        """
        Computes the results equivalent to the SQL query using hash maps for aggregation.
        """
        result = defaultdict(lambda: {'sum_amount': 0, 'num_users': set()})

        # Iterate through all transactions and process the valid ones
        for transaction in self.transactions_data:
            # Filter out blocked transactions
            if not transaction['is_blocked']:
                user_id = transaction['user_id']
                # Check if user is active
                if self.users_data.get(user_id, False):  # User must be active
                    category_id = transaction['transaction_category_id']
                    # Update sum and track unique users for this category
                    result[category_id]['sum_amount'] += transaction['transaction_amount']
                    result[category_id]['num_users'].add(user_id)

        # Convert the results to a sorted list by sum_amount in descending order
        final_result = sorted(
            [{'transaction_category_id': category_id, 
              'sum_amount': data['sum_amount'], 
              'num_users': len(data['num_users'])}
             for category_id, data in result.items()],
            key=lambda x: x['sum_amount'],
            reverse=True
        )

        return final_result

    def print_results(self, results):
        """
        Prints the results to stdout with the appropriate header.
        """
        if not results:
            print("No results found.")
            return

        # Print the header
        print("transaction_category_id,sum_amount,num_users")
        # Print each result in the required format
        for result in results:
            print(f"{result['transaction_category_id']},{result['sum_amount']},{result['num_users']}")

def main():
    transactions_file = 'transactions.csv'  # Path to the transactions CSV file
    users_file = 'users.csv'  # Path to the users CSV file

    analysis = TransactionAnalysis(transactions_file, users_file)

    try:
        analysis.load_users()
        analysis.load_transactions()

        results = analysis.compute_results()

        analysis.print_results(results)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        exit(1)

if __name__ == '__main__':
    main()
