# FUNCTION LOG-IN
import pandas as pd
import hashlib

def log_in(email, password):
    
    db_employees = pd.read_csv("/Users/rita/Desktop/LAB/db_employees.csv")
    db_users = pd.read_csv("/Users/rita/Desktop/LAB/db_users.csv")
    
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



# FUNCTION ADD USER

def add_user(email, password):
    
    db_users = pd.read_csv("/Users/rita/Desktop/LAB/db_users.csv")
    
    suffix = email.split("@")[1]
   
    
    if suffix == "gold1.com":
        print("Invalid email")
        
    else:
        digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        new_df = pd.DataFrame({ "ID": [len(db_users["password"])+1], "email": [email], "password": [digest_password]})
        new_df.to_csv('db_users.csv', mode = "a", index = False, header = False)
        print("Registration was successful")


add_user("pietro.belli@gold1.com", "HAPPY")