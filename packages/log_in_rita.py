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
            
            


# A LOT OF PASSWORDS TO CHECK THE INPUT OF CREDIT CARDS
def check_password(pw):
    
    #Set some parameters for the while cycle
    
    c = False
    i = 0
    while c == False:
        
        check = str(input('Enter again the password to verify it \n'))
        
        #Check if the password are the same 
        
        if pw == check:
            c = True
            print('The password was accepted. \n')
        
        #Check if the user tried more than 3 times to enter the input
        
        elif i >= 2:
            print('Fatal error, the two password still not coincide. Please try again to register to our website. \n')
            break
        
        #Increase i if the input was wrong
        
        elif pw != check:                    
            i = i + 1
            print('The two password are not the same, enter again the password. \n')
        
    return c
    
def get_number():
    
    #Set some parameters for the while cycle
    
    cc = False
    i=0

    while cc == False:
        
        number = str(input('Please insert your credit card number. It should be composed by 16 number and no letters or symbols. \n'))
        
        good = False
        
        #Check if the input was empty
        
        if number:
            
            #Check if the input contains only numerical characters
            
            int_number = '0123456789'
            valid = True
            for n in number:
                if n not in int_number:
                    print('Error, you typed a letter or a special character. \n')
                    valid = False
                    break 
            
            if valid == True:
                nnumber = int(number)
                
                #Check if the credit card number has the right format
                
                if len(number) == 16 and nnumber > 0 and nnumber <= 9999999999999999:
                    good = True
        else:
            print('Error, you did not enter any number. \n')
            
        if good == True:
            cc = True
            print('The number was accepted. \n')

        #Check if the user tried more than 3 times to enter the input
        
        elif i >= 2:
            print('Fatal error, the credit card number is not on the correct format and you reached the limit of chances that you had. Please try again to register to our website. \n')
            break
            
        #Increase i if the input was wrong
        
        elif good == False:                    
            i = i + 1
            
    if cc == False:
        number = None
    
    return number
    
def get_date():
    
    #Set some parameters for the while cycle
    
    cc = False
    i=0

    while cc == False:
        m = str(input('Please insert your credit card month on which it will expire (mm). \n'))
        y = str(input('Please insert your credit card year on which it will expire (yyyy). \n'))
        
        good = False
        
        #Check if the input were empty 
        
        if m and y:
            
            #Check if the input contains only numerical characters
            
            int_number = '0123456789'
            valid = True
            
            for n in m:
                if n not in int_number:
                    valid == False
                    break 
                
            for n in y:
                if n not in int_number:            
                    valid = False
                    break 
                
            if valid == True:
                
                #Check if the numbers typed have the correct format
                
                nm = int(m)
                ny = int(y)
                
                today = date.today()

                # dd/mm/YY
                d1 = today.strftime("%d/%m/%Y")
                ay=d1[6:]
                
                if len(m) <= 2 and len(y) == 4 and nm > 0 and nm < 13 and ny >= 2021 and ny < (ay + 6):
                    
                    #Check if the card is valid but expires this year
                    
                    if ny == ay:
                        from datetime import date
                        am = d1[3:5]
                        if m > am:
                            good = True
                        else:
                            print('Error, this credit card is no more valid. \n')
                            
                        
                    else:
                        good = True
                
                else:
                    print('Error, the data that you typed are not of the right format or is no more valid. Please enter a valid date om the format mm and then yyyy. \n')
            else:
                print('Error, you typed a letter or a special character. \n')
                            
        else:
            print('Error, you let one entry empty. \n')
        
        if good == True:
            cc = True
            print('The data was accepted. \n')
            
        #Check if the user tried more than 3 times to enter the input
        
        elif i >= 2:
            print('Fatal error, the credit card number is not on the correct format and you reached the limit of chances that you had. Please try again to register to our website. \n')
            break
            
        #Increase i if the input was wrong
        
        elif good == False:                    
            i = i + 1
            
        
    
    #Create the output based on the inputs and all the checks
    
    if cc == False:
        date = None
    else:
        date = m+'/'+y
    
    return date
            
def get_cvc():
    
    #Set some parameters for the while cycle
    
    cc = False
    i=0

    while cc == False:
        number = str(input('Please insert the CVC of your credit card number. It should be composed by 3 number and no letters or symbols. \n'))
        
        good = False
        
        #Check if the input was empty
        
        if number:
            
            #Check if the input contains only numerical characters
            
            int_number = '0123456789'
            valid = True
            for n in number:
                if n not in int_number:
                    print('Error, you typed a letter or a special character. \n')
                    valid = False
                    break 
            if valid == True:
                nnumber = int(number)
                if len(number) == 3 and nnumber > 0 and nnumber <= 999:
                    good = True
        
        else:
            print('Error, you did not enter any number. \n')
            
        if good == True:
            cc = True
            print('The number was accepted. \n')

        #Check if the user tried more than 3 times to enter the input
        
        elif i >= 2:
            print('Fatal error, the credit card number is not on the correct format and you reached the limit of chances that you had. Please try again to register to our website. \n')
            break
            
        #Increase i if the input was wrong
        
        elif good == False:                    
            i = i + 1
            
            
    if cc == False:
        number = None
    
    return number          
                        
    
# FUNCTION ADD_USER

from email_validator import validate_email, EmailNotValidError

def add_user(email, password):
    
    db_users = pd.read_csv(r'csv_file/db_users.csv')
    
    #To be discussed with Rita
    
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
                                print('Thank you, you successfully registered into our website and from now you will be allowed to buy precious metals from us. \n')
                    
                if stop == True:
                    print('We are sorry but something in the registration process went wrong. Please try again. \n')
                else:
            
                    digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                    new = pd.DataFrame({ "ID": [len(db_users["password"])+1], "email": [email], "password": [digest_password]})
                    db_users = db_users.append(new)
                    db_users.to_csv(r'csv_file/db_users.csv', index = False)
                    
                    info = pd.read_csv(r'csv_file/info_users.csv')
                    new = pd.DataFrame({ "ID": [len(info["ID"])+1], "number": [number], "date": [date], "cvc": [cvc]})
                    info = info.append(new)
                    info.to_csv(r'csv_file/info_users.csv', index = False)
                        


            except EmailNotValidError as e:
                print(str(e))

        



# FUNCTION ADD_EMPLOYEE

def add_employee(email, password):
    
    df_employees = pd.read_csv(r'csv_file/employees.csv')
    db_employees = pd.read_csv(r'csv_file/db_employees.csv')
    
    try: 
        valid = validate_email(email)
        email = valid.email
        
        if "@gold1.com" not in email:
            print("Please enter an employee email. \n")

        else:
            check = False
            for mail in db_employees["email"]:
                if mail == email:
                    check = True
                    print("This account is already registered. \n")
                    break

            if check == False:     
                presence = False
                for mail in df_employees["email"]:
                    if email == mail:
                        presence = True
                        print('Your email allows you to register as an employee. \n')
                        password_check = check_password(password)
                        if password_check == True:
                            digest_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                            new_df = pd.DataFrame({"email": [email], "password": [digest_password]})
                            db_employees = db_employees.append(new_df)
                            db_employees.to_csv(r'csv_file/db_employees.csv', index = False)
                            print("Registration was successful!. \n")
                        
                        break
                        

                if presence == False: 
                    print("No correspondence. \n")
                    
    except EmailNotValidError as e:
        print(str(e))
                        
log_in("francesca.signorello@gold1.com", "Sushi<3")
add_user("pietro.belligoligmail.com", "HAPPY")                       
add_employee("marco.visentin@gold1.com", "HAPPY")
