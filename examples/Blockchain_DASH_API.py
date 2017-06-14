import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':

    wallet_addr = "Xico5nigvR8Kk2PQZuthSb5dETUf5oAj8g" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_DASH_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
        'success':True,
        'timestamp':'2017-06-14 11:35:26',
        'payload':{
            'final_balance':0,
            'total_sent':3000000000,
            'address':'Xico5nigvR8Kk2PQZuthSb5dETUf5oAj8g',
            'final_n_tx':2,
            'n_tx':2,
            'balance':0,
            'total_received':3000000000,
            'unconfirmed_n_tx':0,
            'unconfirmed_balance':0
        }
    }
    '''
