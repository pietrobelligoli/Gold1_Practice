#! /usr/bin/env python3
import unittest
import sys
import os
#import pandas as pd

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


#df_employees = pd.read_csv(r'csv_file/employees.csv')
#db_employees = pd.read_csv(r'csv_file/db_employees.csv')
#db_users = pd.read_csv(r'csv_file/db_users.csv')

from packages.log_in_rita import log_in 
from packages.log_in_rita import add_employee 
from packages.log_in_rita import add_user 
from packages.buy_metals import buy_metal 
from packages.pay_loan import pay_loan
from packages.read_register import read_register 
from packages.get_balance import get_balance 

class TestInput(unittest.TestCase):

    # smoke tests: valid inputs
    def test_correct_values(self):
        
        #log_in
        self.assertEqual(log_in("roberto.celi@gmail.com", "Peru2021"), "user")
        self.assertEqual(log_in("pietro.belligoli@gold1.com", "Juice123456"), "employee")
        
        #add_employee
        self.assertTrue(add_employee("rita.ghilardi@gold1.com", "Peru2021"), None)
        
        #add_user
        self.assertTrue(add_user("francesca.paris@gmail.com", "Ciao!"), None)
        
        #buy_metal
        self.assertTrue(add_employee("rita.ghilardi@gold1.com", "Peru2021"), None)
        
    #def test_wrong_values(self):
        # input wrong data
        #self.assertEqual(return_birthday("Ada Lovelae"), None)
        #self.assertEqual(return_birthday(7), None)

    # corner case: empty string
    #def test_empty_string(self):
        #self.assertEqual(return_birthday(""), None)
    
    
        
        
        


if __name__ == '__main__':
    unittest.main(verbosity = 2)
