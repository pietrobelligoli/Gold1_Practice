from get_prices import get_prices
import time
def buy_metal(metal,quantity):
    import pandas as pd

    df = pd.read_csv (r'csv_file/inventory.csv')
    
    presence = False

    for i in range(0,5):
        if df.loc[i,'Metal'] == metal:
            presence = True
            break
            
    if presence == False:
        print ('We are sorry, the metal that you want to buy is not traded by us. \n You can buy from us Gold, Silver, Platinum, Palladium and Rhodium')
    elif quantity > 10000:
        print('We are sorry, we are not able to supply you this amount of ', metal, '. We can supply you at most 10 kg')
    else:
        w = pd.read_csv (r'csv_file/wallet.csv')
        if quantity <= df.loc[i,'Quantity']:
            df.loc[i,'Quantity']  = df.loc[i,'Quantity']-quantity
            p = round((quantity * df.loc[i,'Price'] * 1.05),3)
            w.loc[0,'Inflow'] = w.loc[0,'Inflow'] + p
            w.loc[0,'Balance'] = w.loc[0,'Inflow'] - w.loc[0,'Outflow']
            print('Thank you so much, you have just bought ', quantity, 'g of ', metal, ' at the price of ', p, ' EUR')
        else:
            #Buy new metal to have the inventory full
            print('We are buying new metals for you, wait some seconde please')
            success, new = get_prices()
            if success == False:
                print('We are sorry, because of an internal problem we are not able to buy enough metal now. If you make an order of at most', df.loc[i,'Quantity'], ' ', metal, ' we will be able to provide it to you')
            else:
                p1 = df.loc[i,'Price']
                q1 = df.loc[i,'Quantity']
                p2 = round(new[metal],3)
                q2 = 10000 - q1
                new_p = ((p1 * q1) + (p2 * q2)) / 10000
                df.loc[i,'Price'] = new_p
                
                w.loc[0,'Outflow'] = w.loc[0,'Outflow'] + round((q2 * p2),3)
                
                df.loc[i,'Quantity']  = 10000 - quantity
                p = round((quantity * new_p * 1.05),3)
                w.loc[0,'Inflow'] = w.loc[0,'Inflow'] + p
                w.loc[0,'Balance'] = w.loc[0,'Inflow'] - w.loc[0,'Outflow']
                
                time.sleep(5)
                print('Thank you so much, you have just bought ', quantity, 'g of ', metal, ' at the price of ', p, ' EUR')
                
    df.to_csv(r'csv_file/inventory.csv', index=False)
    w.to_csv(r'csv_file/wallet.csv', index=False)

buy_metal('Gold',5)