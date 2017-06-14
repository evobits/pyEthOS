import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':

    wallet_addr = "t3Vz22vK5z2LcKEdg16Yv4FFneEL1zg9ojd" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_ZCASH_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
        'success':True,
        'payload':{
            'totalRecv':19600.399374999997,
            'minedCount':0,
            'balance':7.275957614183426e-12,
            'address':'t3Vz22vK5z2LcKEdg16Yv4FFneEL1zg9ojd',
            'totalSent':19600.39937499999,
            'recvCount':17708,
            'firstSeen':1477671596,
            'sentCount':548,
            'lastSeen':1482338648
        },
        'timestamp':'2017-06-14 02:57:21'
    }
    '''
