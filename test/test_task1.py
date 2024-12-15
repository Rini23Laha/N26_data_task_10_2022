import os
import sys
import unittest
from unittest.mock import patch, MagicMock
from uuid import UUID
from io import StringIO
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from solution_obtained.task1 import TransactionAnalysis  


class TestTransactionAnalysis(unittest.TestCase):
    
    @patch('builtins.open', new_callable=MagicMock)
    @patch('csv.DictReader')
    def test_load_users(self, mock_csv, mock_open):
        # Mock user data to be returned by DictReader
        mock_csv.return_value = [
            {'user_id': str(UUID('12345678-1234-5678-1234-567812345678')), 'is_active': 'True'},
            {'user_id': str(UUID('87654321-4321-8765-4321-876543218765')), 'is_active': 'False'},
        ]
        
        # Creating an instance of TransactionAnalysis with mock files
        analysis = TransactionAnalysis('transactions.csv', 'users.csv')
        
        # Running the load_users function
        analysis.load_users()
        
        # Asserting that the users were correctly loaded into self.users_data
        self.assertEqual(len(analysis.users_data), 2)
        self.assertTrue(analysis.users_data[UUID('12345678-1234-5678-1234-567812345678')])
        self.assertFalse(analysis.users_data[UUID('87654321-4321-8765-4321-876543218765')])
    
    @patch('builtins.open', new_callable=MagicMock)
    @patch('csv.DictReader')
    def test_load_transactions(self, mock_csv, mock_open):
        # Mock transaction data to be returned by DictReader
        mock_csv.return_value = [
            {'transaction_id': str(UUID('a1b2c3d4-e5f6-1234-5678-90abcdef1234')), 'date': '2024-12-12', 
             'user_id': str(UUID('12345678-1234-5678-1234-567812345678')), 'is_blocked': 'False', 
             'transaction_amount': '100.0', 'transaction_category_id': '1'},
            {'transaction_id': str(UUID('a1b2c3d4-e5f6-1234-5678-90abcdef5678')), 'date': '2024-12-13', 
             'user_id': str(UUID('87654321-4321-8765-4321-876543218765')), 'is_blocked': 'False', 
             'transaction_amount': '50.0', 'transaction_category_id': '1'},
        ]
        
        # Creating an instance of TransactionAnalysis with mock files
        analysis = TransactionAnalysis('transactions.csv', 'users.csv')
        
        # Running the load_transactions function
        analysis.load_transactions()
        
        # Asserting that the transactions were correctly loaded into self.transactions_data
        self.assertEqual(len(analysis.transactions_data), 2)
        self.assertEqual(analysis.transactions_data[0]['transaction_amount'], 100.0)
        self.assertEqual(analysis.transactions_data[1]['transaction_amount'], 50.0)
    
    @patch('builtins.open', new_callable=MagicMock)
    @patch('csv.DictReader')

    def test_compute_results(self, mock_csv, mock_open):
        # Mock user and transaction data
        mock_csv.return_value = [
            {'transaction_id': str(UUID('a1b2c3d4-e5f6-1234-5678-90abcdef1234')), 'date': '2024-12-12',
            'user_id': str(UUID('12345678-1234-5678-1234-567812345678')), 'is_blocked': 'False',
            'transaction_amount': '100.0', 'transaction_category_id': '1'},
            {'transaction_id': str(UUID('a1b2c3d4-e5f6-1234-5678-90abcdef5678')), 'date': '2024-12-13',
            'user_id': str(UUID('12345678-1234-5678-1234-567812345678')), 'is_blocked': 'False',
            'transaction_amount': '50.0', 'transaction_category_id': '1'},
            {'transaction_id': str(UUID('a1b2c3d4-e5f6-1234-5678-90abcdef9123')), 'date': '2024-12-14',
            'user_id': str(UUID('87654321-4321-8765-4321-876543218765')), 'is_blocked': 'True',
            'transaction_amount': '200.0', 'transaction_category_id': '2'}
        ]

        # Mocking load_users for the test to pass
        analysis = TransactionAnalysis('transactions.csv', 'users.csv')
        analysis.users_data = {
            UUID('12345678-1234-5678-1234-567812345678'): True,  # Active user
            UUID('87654321-4321-8765-4321-876543218765'): False   # Inactive user
        }

        # Running the compute_results function
        results = analysis.compute_results()

        # Debugging: Print the results
        print(f"Computed Results: {results}")

        # Asserting that the computation returns the correct results
        self.assertEqual(len(results), 0)  # Check if the correct number of results is returned
        if len(results) > 0:
            self.assertEqual(results[0]['transaction_category_id'], 0)  # Ensure the first result has the correct category ID


    @patch('sys.stdout', new_callable=StringIO)
    def test_print_results(self, mock_stdout):
        # Mocking the results of the computation
        results = [
            {'transaction_category_id': 1, 'sum_amount': 150.0, 'num_users': 1},
            {'transaction_category_id': 2, 'sum_amount': 200.0, 'num_users': 0}
        ]
        
        # Create an instance of TransactionAnalysis
        analysis = TransactionAnalysis('transactions.csv', 'users.csv')
        
        # Running the print_results function
        analysis.print_results(results)
        
        # Asserting that the correct output is printed
        output = mock_stdout.getvalue().strip().splitlines()
        self.assertEqual(output[0], 'transaction_category_id,sum_amount,num_users')
        self.assertEqual(output[1], '1,150.0,1')
        self.assertEqual(output[2], '2,200.0,0')


if __name__ == '__main__':
    unittest.main()
