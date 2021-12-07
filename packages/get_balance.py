def get_balance():
    
    df_inventory = pd.read_csv (r'csv_file/inventory.csv')
    df_wallet = pd.read_csv (r'csv_file/wallet.csv')

    # Inventory balance
    for i in range(0,len(df_inventory)):
        print(df_inventory.loc[i,'Metals'], 'balance:', df_inventory.loc[i,'Quantity'], 'grams.')
    
    # Cash available
    print('\nCash available:', df_wallet.loc[0,'Balance'])
