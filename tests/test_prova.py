#! /usr/bin/env python3
import unittest
import sys
import os

from packages.log_in_rita import log_in
from packages.log_in_rita import add_user
from packages.log_in_rita import add_employee
from packages.buy_metals import buy_metal


# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Test(unittest.TestCase):
    def setUp(self):

        # user log_in
        self.email_user = "roberto.celi@gmail.com"
        self.password_user = "Peru2021"
        self.f_email_user = "roberto"
        self.f_password_user = "Italy"

        # employee log_in
        self.email_empl = "rita.ghilardi@gold1.com"
        self.password_empl = "HeidieMilady2"
        self.f_log_empl = ""
        self.f_password_empl = "Heidi1"

        # add_user function
        self.n_mail_user = "eva.castelli@gmail.com"
        self.n_pass_user = "Pallocchio"
        self.f_n_user = "ghilardi.miriam@hotmail.com"
        self.f_n_pass = 25

        # add_employee
        self.n_mail_empl = "marco.visentin@gold1.com"
        self.n_pass_empl = "Marco2000"
        self.f_mail_empl = "rita"
        self.f_pass_empl = []

        # add metals
        self.mail = "giada.rovari@gmail.com"
        self.metal = "Silver"
        self.quantity = "1"
        self.f_metal = "Wood"
        self.f_quantity = "0"

    def test_log_in(self):
        self.assertTrue(log_in(self.email_user, self.password_user))
        self.assertFalse(log_in(self.email_user, self.f_password_user))
        self.assertFalse(log_in(self.f_email_user, self.password_user))
        self.assertTrue(log_in(self.email_empl, self.password_empl))
        self.assertFalse(log_in(self.email_empl, self.f_password_empl))
        self.assertFalse(log_in(self.f_log_empl, self.password_empl))

    def test_add_user(self):
        self.assertTrue(add_user(self.n_mail_user, self.n_pass_user))
        self.assertFalse(add_user(self.n_mail_user, self.f_n_pass))
        self.assertFalse(add_user(self.f_mail_empl, self.n_pass_user))

    def test_add_employee(self):
        self.assertTrue(add_employee(self.n_mail_empl, self.n_pass_empl))
        self.assertFalse(add_employee(self.n_mail_empl, self.f_pass_empl))
        self.assertFalse(add_employee(self.f_mail_empl, self.n_pass_empl))

    def test_buy_metals(self):
        self.assertTrue(buy_metal(self.mail, self.metal, self.quantity))
        self.assertFalse(buy_metal(self.mail, self.f_metal, self.quantity))
        self.assertFalse(buy_metal(self.mail, self.metal, self.f_quantity))


if __name__ == "__main__":
    unittest.main()
