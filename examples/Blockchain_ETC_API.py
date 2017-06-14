import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':

    wallet_addr = "6b83f808fce08f51adb2e9e35a21a601e702785f" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_ETC_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
        'payload':{
            'eth_balance':0,
            'balance':46.719429118,
            'address':'0x6b83f808fce08f51adb2e9e35a21a601e702785f'
        },
        'success':True,
        'timestamp':'2017-06-14 03:11:42'
    }
    '''
