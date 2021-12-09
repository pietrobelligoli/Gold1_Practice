#! /usr/bin/env python3
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from packages.log_in_rita import log_in 
from packages.log_in_rita import add_user
from packages.get_balance import get_balance
from packages.log_in_rita import add_employee

class Test(unittest.TestCase):

    def setUp(self):
       
        #log_in function
       
        #user
        self.t_email_user = "roberto.celi@gmail.com"
        self.t_password_user = "Peru2021"
        self.f_email_user = "roberto.celi@gmail.com"
        self.f_password_user = "Italy"
        
        #employee
        self.t_email_employee = "rita.ghilardi@gold1.com"
        self.t_password_employee = "HeidieMilady2"
        self.f_email_employee = "rita.ghilardi@gold1.com"
        self.f_password_employee = "Heidi1"
        
        #add_user function
        #self.new_mail_user = "eva.castelli@gmail.com"
        #self.new_pass_user = "Pallocchio"
        
        #add_employee
        self.new_mail_employee = "marco.visentin@gold1.com"
        self.new_pass_employee = "Marco2000"
        
        
    #def test_log_in(self):
        #self.assertTrue(log_in(self.t_email_user, self.t_password_user))
        #self.assertFalse(log_in(self.f_email_user, self.f_password_user))
        #self.assertTrue(log_in(self.t_email_employee, self.t_password_employee))
        #self.assertFalse(log_in(self.f_email_employee, self.f_password_employee))
        
        
    #def test_add_user(self):
        #self.assertTrue(add_user(self.new_mail_user, self.new_pass_user))
        
        
    def test_add_employee(self):  
        self.assertTrue(add_employee(self.new_mail_employee, self.new_pass_employee))
        
        
    #def test_get_balance(self):
        #self.assertTrue
    
    
    
if __name__ == "__main__":
    unittest.main()