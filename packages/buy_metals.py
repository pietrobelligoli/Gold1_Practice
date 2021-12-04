def buy_metal(metal,quantity):
    import pandas as pd

    df = pd.read_csv (r'csv_file/inventory.csv')
    presence = False
    for i in range(0,5):
        if df.loc[i,'Metal']=metal:
            presence = True
            break
    if presence = False:
        print ('We are sorry, the metal that you want to buy is not traded by us. \n You can buy from us Gold, Silver, Platinum, Palladium and Rhodium'
    else: