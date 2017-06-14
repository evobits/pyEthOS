import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':

    wallet_addr = "DBS699kjdjXr6GAxpg5V1h1qr7t7h4QTzQ" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_DOGE_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
        'success':True,
        'timestamp':'2017-06-14 11:32:33',
        'payload':{
            'final_balance':0,
            'total_sent':0,
            'address':'DBS699kjdjXr6GAxpg5V1h1qr7t7h4QTzQ',
            'final_n_tx':0,
            'n_tx':0,
            'balance':0,
            'total_received':0,
            'unconfirmed_n_tx':0,
            'unconfirmed_balance':0
        }
    }
    '''
