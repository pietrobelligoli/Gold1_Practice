#! /usr/bin/env python3
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.log_in_rita import add_employee

class Test(unittest.TestCase):
    def setUp(self):
    
        self.mail_empl = "marco.visentin@gold1.com"
        self.pass_empl = "Marco2000"
        self.f_mail_empl = "rita"
        self.f_pass_empl = []
            
        
    def test_add_employee(self):
        self.assertTrue(add_employee(self.mail_empl, self.pass_empl))  
        self.assertFalse(add_employee(self.f_mail_empl, self.f_pass_empl))
        self.assertFalse(add_employee(self.mail_empl, self.f_pass_empl))
        self.assertFalse(add_employee(self.f_mail_empl, self.pass_empl))
        
        
      
if __name__ == "__main__":
    unittest.main()