#! /usr/bin/env python3
import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from packages.log_in_rita import add_user

class Test(unittest.TestCase):
    def setUp(self):
    
        # add_user function
        self.mail_user = "eva.castelli@gmail.com"
        self.pass_user = "Pallocchio"
        self.f_mail_user = "ghilardi.miriam@hotmail.com"
        self.f_pass_user = 25
        
    def test_add_user(self):
        self.assertTrue(add_user(self.mail_user, self.pass_user))
        self.assertFalse(add_user(self.f_mail_user, self.f_pass_user))
        self.assertFalse(add_user(self.mail_user, self.f_pass_user))
        self.assertFalse(add_user(self.f_mail_user, self.pass_user))
        
        
if __name__ == "__main__":
    unittest.main()
