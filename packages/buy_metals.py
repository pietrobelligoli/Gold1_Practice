def buy_metal(metal,quantity):
    import pandas as pd

    df = pd.read_csv (r'csv_file/inventory.csv')
    w = pd.read_csv (r'csv_file/wallet.csv')
    presence = False
    for i in range(0,5):
        if df.loc[i,'Metal'] == metal:
            presence = True
            break
    if presence == False:
        print ('We are sorry, the metal that you want to buy is not traded by us. \n You can buy from us Gold, Silver, Platinum, Palladium and Rhodium')
    else:
        if quantity <= df.loc[i,'Quantity']:
            df.loc[i,'Quantity']  =df.loc[i,'Quantity']-quantity
            p = round((quantity * df.loc[i,'Price'] * 1.2),3)
            w.loc[0,'Inflow'] = w.loc[0,'Inflow'] + p
            w.loc[0,'Balance'] = w.loc[0,'Inflow'] - w.loc[0,'Outflow']
            print('Thank you so much, you have just bought ', quantity, 'g of ', metal, ' at the price of ', p, ' EUR')
        
    df.to_csv(r'csv_file/inventory.csv')
    w.to_csv(r'csv_file/wallet.csv')
buy_metal('Gold',5)