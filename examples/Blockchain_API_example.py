import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':
    wallet_addr = "eb090e55b3d0cb2544d5b4fb6f485845068bd932" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
    	"payload": {
    		"balance": 0,
    		"final_balance": 0,
    		"total_sent": 0,
    		"address": "260e285b113b8be32a5141c35d18257792c757db",
    		"total_received": 0,
    		"final_n_tx": 0,
    		"n_tx": 0,
    		"unconfirmed_balance": 0,
    		"unconfirmed_n_tx": 0
    	},
    	"timestamp": "2017-06-12 15:51:15",
    	"success": "True"
    }
    '''
