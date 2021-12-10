from packages.get_prices import get_prices
import time
import pandas as pd


def ask_cvc(user):
    
    df = pd.read_csv (r'csv_file/info_users.csv')    
    check = False
    
    #Search the cvc using the username. This value will be find by construction, because we already did the log in
    
    for i in range(len(df.index)):
        if df.loc[i,'email'] == user:
            stored = df.loc[i,'cvc']
            break
            
    #Ask to confirm the cvc
    
    i=0

    while check == False:
        number = str(input('Please insert the CVC of your credit card number to confirm the purchase. \n'))
        
        good = False
        
        #Check if the input was empty
        
        if number :
            
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
            check = True
            print('The number was accepted. \n')

        #Check if the user tried more than 3 times to enter the input
        
        elif i >= 2:
            print('Fatal error, the credit card number is not on the correct format and you reached the limit of chances that you had. Please try again to register to our website. \n')
            break
            
        #Increase i if the input was wrong
        
        elif good == False:                    
            i = i + 1
    
    return check
    
def buy_metal(client,metal,quantity):
    import pandas as pd
    from datetime import date

    #Open the inventory
    df = pd.read_csv (r'csv_file/inventory.csv')
    
    quantity = int(quantity)

    presence = False

    result = False

    #Check if the metal is traded by us
    for i in range(0,5):
        if df.loc[i,'Metal'] == metal:
            presence = True
            break
            
    if presence == False:
        #Say that we don't trade the metal
        print ('We are sorry, the metal that you want to buy is not traded by us. \n You can buy from us Gold, Silver, Platinum, Palladium and Rhodium. \n')
   
    elif quantity > 1000:
        #Say if the quantity requested is too much
        print('We are sorry, we are not able to supply you this amount of ', metal, '. We can supply you at most 10 kg. \n')
   
    else:
   
        #Metal and quantity are ok, we open the wallet
   
        w = pd.read_csv (r'csv_file/wallet.csv')
        
        #Check if we have enough metal in the inventory
        
        if quantity <= df.loc[i,'Quantity']:
            
            #We have enough metal, we can sell it without buying it
            #We ask to type the cvc of the credit card to confirm the purchase
            
            check = ask_cvc(client)
            if check == False:
                success = False
                print('We are sorry, the purchase was abort. \n')
                
            else:
                
                success = True
                df.loc[i,'Quantity']  = df.loc[i,'Quantity']-quantity
                
                #Calculate the selling price with a profit of 5%
                
                p = round((quantity * df.loc[i,'Price'] * 1.05),3)
                
                #Record on the wallet the cash inflow and new balance
                
                w.loc[0,'Inflow'] = w.loc[0,'Inflow'] + p
                w.loc[0,'Balance'] = w.loc[0,'Balance'] + p
                
                #Succesful transaction

                result = True
                print('Thank you so much, you have just bought ', quantity, 'g of ', metal, ' at the price of ', p, ' EUR. \n')

        else:
            
            #Buy new metal to have the inventory full
            
            print('We are buying new metals for you, wait some seconde please. \n')
            
            #Call the function get prices to call the API and buy new metal at the actual price
            
            success, new = get_prices()
            
            #Check if the API is online and so we are able to buy new metal
            
            if success == False:
                
                print('We are sorry, because of an internal problem we are not able to buy enough metal now. If you make an order of at most', df.loc[i,'Quantity'], ' ', metal, ' we will be able to provide it to you. \n')
            
            else:
                
                #Before proceeding we check the cvc of the client
                
                check = ask_cvc(client)
                if check == False:
                    success = False
                    print('We are sorry, the purchase was abort. \n')
                    
                else:
                    #We've just bought new metal, we need to update the inventory
                    
                    p1 = df.loc[i,'Price']
                    q1 = df.loc[i,'Quantity']
                    p2 = round(new[metal],3)
                    q2 = 1000 - q1
                    
                    #Control if we have enough cash
                    
                    acq_price = round((q2 * p2),3)
                    if w.loc[0,'Balance'] < acq_price:
                        
                        #Ask a loan to be able to buy the new metals 
                        
                        delta = acq_price - w.loc[0,'Balance']
                        w.loc[0,'Bank_Loan'] = w.loc[0,'Bank_Loan'] + delta 
                        w.loc[0,'Balance'] = w.loc[0,'Balance'] + delta
                        
                    #Calculate the weighted mean of the price and update it
                    
                    new_p = round((((p1 * q1) + (p2 * q2)) / 1000),3)
                    df.loc[i,'Price'] = new_p
                    
                    #Register the cash outflow
                    
                    w.loc[0,'Outflow'] = w.loc[0,'Outflow'] + acq_price
                    w.loc[0,'Balance'] = w.loc[0,'Balance'] - acq_price                    
                    df.loc[i,'Quantity']  = 1000 - quantity
                    
                    #Calculate the selling price with a profit of 5%
                    
                    p = round((quantity * new_p * 1.05),3)
                    
                    #Register cash inflow and new balance
                    
                    w.loc[0,'Inflow'] = w.loc[0,'Inflow'] + p
                    w.loc[0,'Balance'] = w.loc[0,'Balance'] + p
                    
                    #Succesful transaction
                    
                    time.sleep(5)
                    print('Thank you so much, you have just bought ', quantity, 'g of ', metal, ' at the price of ', p, ' EUR. \n')
            
        if success == True:                
            #Register transaction, first open the register
            
            register = pd.read_csv (r'csv_file/register.csv')
            today = date.today()

            # dd/mm/YY
            d1 = today.strftime("%d/%m/%Y")
            
            #Create a new row
            
            add = pd.DataFrame(columns=['Customer', 'Date', 'Metal', 'Quantity', 'Price'])
            add.loc[0] = [client,d1,metal,quantity,p]
             
            #Add the new row
            
            register = register.append(add, ignore_index=True)

            #Close the register
            register.to_csv(r'csv_file/register.csv', index=False)
    
    return result
    
    df.to_csv(r'csv_file/inventory.csv', index=False)
    w.to_csv(r'csv_file/wallet.csv', index=False)