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