import pandas as pd
import argparse
import hashlib

# FUNCTION LOG-IN

def log_in(email, password):
    
    db_employees = pd.read_csv(r'csv_file/db_employees.csv')
    db_users = pd.read_csv(r'csv_file/db_users.csv')
    
    suffix = email.split("@")[1]
   
    #employees
    if suffix == "gold1.com":
        
        for address in db_employees["email"]:
            if address == email:
                line = list(db_employees["email"]).index(address)
                digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if db_employees["password"][line] == digest_password:
                    print("Access allowed")
                    break
                
                else:
                    print("Please check password")
                    break
                
                
            elif address != email and list(db_employees["email"]).index(address) == len(db_employees["email"])-1:
                print("Please, log-in as a user")
            
                
            else: 
                continue
        
      
    #users   
    else: 
      
        for mail in db_users["email"]:
            if mail == email:
                line = list(db_users["email"]).index(mail)
                digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if db_users["password"][line] == digest_password:
                    print("Access allowed")
                    break
                
                else:
                    print("Please check password")
                    break
                
                
            elif mail != email and list(db_users["email"]).index(mail) == len(db_users["email"])-1:
                print("No correspondence")
            
                
            else: 
                continue
            
            
log_in("francesca.signorello@gold1.com", "Sushi<3")


# FUNCTION ADD_USER

from email_validator import validate_email, EmailNotValidError

def add_user(email, password):
    
    db_users = pd.read_csv(r'csv_file/db_users.csv')
    
    if "@" not in email:
        print("Please enter a valid email")
        
    else: 
        suffix = email.split("@")[1]
   
        if suffix == "gold1.com":
            print("Invalid email, please register as a user")
        
        else:
            try:
                valid = validate_email(email)
                email = valid.email
                digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                new_df = pd.DataFrame({ "ID": [len(db_users["password"])+1], "email": [email], "password": [digest_password]})
                new_df.to_csv('db_users.csv', mode = "a", index = False, header = False)
                print("Registration was successful!")


            except EmailNotValidError as e:
                print(str(e))

        

add_user("pietro.belligoli@gold1.com", "HAPPY")

# FUNCTION ADD_EMPLOYEE

def add_employee(email, password):
    
    df_employees = pd.read_csv(r'csv_file/employees.csv')
    db_employees = pd.read_csv(r'csv_file/db_employees.csv')
    
    try: 
        valid = validate_email(email)
        email = valid.email
        
        if "@gold1.com" not in email:
            print("Please enter an employee email")

        else:
            check = False
            for mail in db_employees["email"]:
                if mail == email:
                    check = True
                    print("This account is already registered")
                    break

            if check == False:     
                presence = False
                for mail in df_employees["Email"]:
                    if email == mail:
                        presence = True
                        digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                        new_df = pd.DataFrame({"email": [email], "password": [digest_password]})
                        db_employees = db_employees.append(new_df)
                        db_employees.to_csv(r'csv_file/employees.csv', index = False)
                        print("Registration was successful!")
                        break

                if presence == False: 
                    print("No correspondence")
                    
    except EmailNotValidError as e:
        print(str(e))
                        
                       
add_employee("marco.visentin@gmail.com", "HAPPY")


