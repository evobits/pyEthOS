import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':

    wallet_addr = "LTEoFUTYoYbQwvEck18tEgHUS8VhkzdmJG" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_DASH_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
        'success':True,
        'timestamp':'2017-06-14 11:37:37',
        'payload':{
            'final_balance':0,
            'total_sent':0,
            'address':'LTEoFUTYoYbQwvEck18tEgHUS8VhkzdmJG',
            'final_n_tx':0,
            'n_tx':0,
            'balance':0,
            'total_received':0,
            'unconfirmed_n_tx':0,
            'unconfirmed_balance':0
        }
    }
    '''
