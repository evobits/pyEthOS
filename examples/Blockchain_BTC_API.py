import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':

    wallet_addr = "1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_BTC_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
        'success':True,
        'timestamp':'2017-06-14 03:04:37',
        'payload':{
            'unconfirmed_balance':0,
            'balance':4449209,
            'unconfirmed_n_tx':0,
            'total_received':4449209,
            'address':'1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD',
            'final_n_tx':9,
            'final_balance':4449209,
            'n_tx':9,
            'total_sent':0
        }
    }
    '''
