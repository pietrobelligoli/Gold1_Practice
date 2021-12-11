def get_balance():
    import pandas as pd
    df_inventory = pd.read_csv(r'csv_file/inventory.csv')
    df_wallet = pd.read_csv(r'csv_file/wallet.csv')

    # Inventory balance
    print('Inventory: \n')
    for i in range(0, len(df_inventory)):
        print(df_inventory.loc[i, 'Metal'], 'balance:',
              df_inventory.loc[i, 'Quantity'], 'grams. \n')

    # Cash available
    print('Cash available:', df_wallet.loc[0, 'Balance'], 'EUR', '\n')

    # Bank loan
    print('Debt with bank:', df_wallet.loc[0, 'Bank_Loan'], 'EUR', '\n')
