import argparse
import pandas as pd
import hashlib

def parse_args():
    parser = argparse.ArgumentParser(description= 'Check if the username and password' +  
    'given as input are registered')
    
    group = parser.add_mutually_exclusive_group()

    parser.add_argument("username", help="username")
    parser.add_argument("password", help="password of the user")

    args = parser.parse_args()
    username = args.username
    password = args.password

    return args, username, password