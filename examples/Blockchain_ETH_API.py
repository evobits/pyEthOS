import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':

    wallet_addr = "260e285b113b8be32a5141c35d18257792c757db" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_ETH_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
        'timestamp':'2017-06-14 03:05:49',
        'payload':{
            'unconfirmed_n_tx':0,
            'address':'260e285b113b8be32a5141c35d18257792c757db',
            'final_n_tx':0,
            'balance':0,
            'final_balance':0,
            'n_tx':0,
            'total_received':0,
            'unconfirmed_balance':0,
            'total_sent':0
        },
        'success':True
    }
    '''
