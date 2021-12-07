#! /usr/bin/env python3
import argparse

from packages.log_in_rita import log_in 
from packages.log_in_rita import add_employee 
from packages.log_in_rita import add_user 
from packages.buy_metals import buy_metal 
from packages.pay_loan import pay_loan
from packages.read_register import read_register 
from packages.get_balance import get_balance 
 
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="Insert the username that you want to use")
    parser.add_argument("password", help="Insert the password that you want to use")
    
    parser.add_argument("-au","--add_user", help="Register as a user with the username and password that you provide", action="store_true")                    
    parser.add_argument("-ae","--add_employee", help="Register as an employee with the username and password that you provide", action="store_true")
    
    parser.add_argument("-bm","--buy_metal", default= None, help="Specify the metal that you want to buy (this argument must be used with bq)", type = str)
    parser.add_argument("-bg","--buy_grams", default= None, help="Specify the grams that you want to buy (this argument must be used with bm)", type = int)  
    
    parser.add_argument("-rr","--read_register", help="Method only for employees: show the register of all transactions", action="store_true")
    parser.add_argument("-gb","--get_balance", help="Method only for employees: show the inventory and the cash balance", action="store_true")
    parser.add_argument("-pb","--pay_bank", help="Method only for employees: pay back the bank if there are debts", action="store_true")
    
    args = parser.parse_args()
    return args
    
arg=parse_arguments()

username=arg.username
password=arg.password
metal=arg.buy_metal
grams=arg.buy_grams
add_user=arg.add_user
add_employee=arg.add_employee
read_register=arg.read_register
get_balance=arg.get_balance
pay_bank=arg.pay_bank

log = None

if add_employee == True:
    add_employee(username,password)
elif add_user == True:
    add_user(username,password)
else:
    log=log_in(username,password)
if log != None:
    if log == 'employee':
        s=False
        if read_register:
            read_register()
            s=True
        if get_balance:
            get_balance()
            s=True
        if pay_bank:
            pay_loan()
            s=True
        if s == False:
            print('You succesfully logged in as a employee, but you have to type other arguments to do something')
            
    elif log == 'user':
        if metal == None:
            print('To buy metals you have to specify them using --buy_metal')
        elif grams == None:
            print('To buy metals you have to specify the grams you want using --buy_grams')
        else:
            buy_metal(username,metal,grams)
