def read_register():

    ''' This function can be called only by employees.
        The function print the register of all transactiond
        done by the company.
    '''

    # Open the register

    import pandas as pd
    register = pd.read_csv(r'csv_file/register.csv')

    print('Register of transactions: \n')

    # Print each line

    for i in range(len(register.index)):
        print('On', register.loc[i, 'Date'], 'the customer',
              register.loc[i, 'Customer'], 'bought ',
              register.loc[i, 'Quantity'], 'g of',
              register.loc[i, 'Metal'], 'at the price of',
              register.loc[i, 'Price'], 'euro. \n')
