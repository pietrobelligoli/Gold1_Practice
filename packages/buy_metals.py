from get_prices import get_prices
import time


def buy_metal(client,metal,quantity):
    import pandas as pd
    from datetime import date

    #Open the inventory
    df = pd.read_csv (r'csv_file/inventory.csv')
    
    presence = False
    #Check if the metal is traded by us
    for i in range(0,5):
        if df.loc[i,'Metal'] == metal:
            presence = True
            break
            
    if presence == False:
        #Say that we don't trade the metal
        print ('We are sorry, the metal that you want to buy is not traded by us. \n You can buy from us Gold, Silver, Platinum, Palladium and Rhodium')
   
    elif quantity > 10000:
        #Say if the quantity requested is too much
        print('We are sorry, we are not able to supply you this amount of ', metal, '. We can supply you at most 10 kg')
   
    else:
   
        #Metal and quantity are ok, we open the wallet
   
        w = pd.read_csv (r'csv_file/wallet.csv')
        
        #Check if we have enough metal in the inventory
        
        if quantity <= df.loc[i,'Quantity']:
            
            #We have enough metal, we can sell it without buying it
            
            success = True
            df.loc[i,'Quantity']  = df.loc[i,'Quantity']-quantity
            
            #Calculate the selling price with a profit of 5%
            
            p = round((quantity * df.loc[i,'Price'] * 1.05),3)
            
            #Record on the wallet the cash inflow and new balance
            
            w.loc[0,'Inflow'] = w.loc[0,'Inflow'] + p
            w.loc[0,'Balance'] = w.loc[0,'Inflow'] - w.loc[0,'Outflow']
            
            #Succesful transaction
            
            print('Thank you so much, you have just bought ', quantity, 'g of ', metal, ' at the price of ', p, ' EUR')
        
        else:
            
            #Buy new metal to have the inventory full
            
            print('We are buying new metals for you, wait some seconde please')
            
            #Call the function get prices to call the API and buy new metal at the actual price
            
            success, new = get_prices()
            
            #Check if the API is online and so we are able to buy new metal
            
            if success == False:
                
                print('We are sorry, because of an internal problem we are not able to buy enough metal now. If you make an order of at most', df.loc[i,'Quantity'], ' ', metal, ' we will be able to provide it to you')
            
            else:
                
                #We've just bought new metal, we need to update the inventory
                
                p1 = df.loc[i,'Price']
                q1 = df.loc[i,'Quantity']
                p2 = round(new[metal],3)
                q2 = 10000 - q1
                
                #Calculate the weighted mean of the price and update it
                
                new_p = ((p1 * q1) + (p2 * q2)) / 10000
                df.loc[i,'Price'] = new_p
                
                #Register the cash outflow
                
                w.loc[0,'Outflow'] = w.loc[0,'Outflow'] + round((q2 * p2),3)                
                df.loc[i,'Quantity']  = 10000 - quantity
                
                #Calculate the selling price with a profit of 5%
                
                p = round((quantity * new_p * 1.05),3)
                
                #Register cash inflow and new balance
                
                w.loc[0,'Inflow'] = w.loc[0,'Inflow'] + p
                w.loc[0,'Balance'] = w.loc[0,'Inflow'] - w.loc[0,'Outflow']
                
                #Succesful transaction
                
                time.sleep(5)
                print('Thank you so much, you have just bought ', quantity, 'g of ', metal, ' at the price of ', p, ' EUR')
            
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
            
    df.to_csv(r'csv_file/inventory.csv', index=False)
    w.to_csv(r'csv_file/wallet.csv', index=False)

buy_metal('Prova','Silver',5)