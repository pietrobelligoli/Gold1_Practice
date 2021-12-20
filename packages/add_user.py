import pandas as pd
import argparse
import hashlib
from email_validator import validate_email 
from email_validator import EmailNotValidError
from packages.check_password import check_password
from packages.get_number import get_number
from packages.get_date import get_date
from packages.get_cvc import get_cvc
import random



def add_user(email, password):
    
    db_users = pd.read_csv(r'csv_file/db_users.csv')
    
    result = False
    
    
    if "@" not in email:
        print("Please enter a valid email. \n")
        
    else: 
        suffix = email.split("@")[1]
        
        if suffix == "gold1.com":
            print("Invalid email, please register as a user. \n")
        
        else:
            try:
                valid = validate_email(email)
                email = valid.email
                
                #Check if the email is already registered
                
                presence = False
                
                
                for i in range(len(db_users)):
                    if email == db_users.loc[i,'email']:
                        presence = True
                        print('An existing account is already associated with this email. \n')
                
                if presence == False:
                    cp = check_password(password)
                    stop = False
                    if cp == False:
                        stop = True
                    else:
                        number = get_number()
                        if number == None:
                            stop = True
                        else:
                            date = get_date()
                            if date == None:
                                stop = True
                            else:
                                cvc = get_cvc()
                                if cvc == None:
                                    stop = True
                                else:
                                    result = True
                                    print('Thank you, you successfully registered into our website and from now you will be allowed to buy precious metals from us. \n')
                        
                    if stop == True:
                        print('We are sorry but something in the registration process went wrong. Please try again. \n')
                    else:
                        
                        #Generate the random ID without call too many times
                        #Generate a random in an interval where I know that there are no valid ID
                        #ID with min 1 and max 99999999
                        
                        existing_id = list(db_users['ID'])
                        existing_id = sorted(existing_id)
                        
                        list_id = [0]
                        list_id.extend(existing_id)
                        list_id.extend([100000000])
                        
                        
                        #Loop to check, but whould not be necessary
                        
                        new = False
                        
                        while new == False:
                            delta=[]
                            best_i=0
                            for i in range(len(list_id)-1):
                                delta.append(list_id[i+1]-list_id[i])
                                if delta[i] > delta[best_i]:
                                    best_i = i
                                    
                            bottom = list_id[best_i]
                            top = list_id[best_i +1]
                            Id = random.randint(bottom + 1,top -1)
                            if Id not in list_id:
                                new = True
                        
                        digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                        new = pd.DataFrame({ "ID": [Id], "email": [email], "password": [digest_password]})
                        db_users = db_users.append(new)
                        db_users.to_csv(r'csv_file/db_users.csv', index = False)
                        
                        info = pd.read_csv(r'csv_file/info_users.csv')
                        new = pd.DataFrame({ "ID": [Id], "number": [number], "date": [date], "cvc": [cvc]})
                        info = info.append(new)
                        info.to_csv(r'csv_file/info_users.csv', index = False)
                        


            except EmailNotValidError as e:
                print(str(e))
            
    return result