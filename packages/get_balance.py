def get_balance():
    
    df_inventory = pd.read_csv (r'csv_file/inventory.csv')
    df_wallet = pd.read_csv (r'csv_file/wallet.csv')

    # Inventory balance
    for i in range(0,len(inventory)):
        total_value = inventory.iloc[i]['Quantity'] * inventory.iloc[i]['Price']
        print(inventory.iloc[i]['Metals'], 'balance:', inventory.iloc[i]['Quantity'], 'grams,', total_value, 'EUR value.')
    
    # Cash available
    print('\nCash available:', wallet.iloc[0]['Balance'])
    
    
get_balance()