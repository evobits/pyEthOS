import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':
    wallet_addr = "eb090e55b3d0cb2544d5b4fb6f485845068bd932" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Ethermine_API(wallet_addr, debug=True)

    print(api.get_account_stats())
    '''
    {
    	"payload": {
    		"btcPerMin": 0,
    		"reportedHashRate": "0H/s",
    		"avgHashrate": 0,
    		"hashRate": "0H/s",
    		"rounds": [],
    		"ethPerMin": 0,
    		"payouts": [],
    		"address": "260e285b113b8be32a5141c35d18257792c757db",
    		"usdPerMin": 0,
    		"workers": {},
    		"unpaid": 0,
    		"settings": {
    			"monitor": 0,
    			"vote": 0,
    			"voteip": "",
    			"name": "",
    			"minPayout": 1,
    			"email": "",
    			"ip": ""
    		}
    	},
    	"timestamp": "2017-06-12 15:44:56",
    	"success": "True"
    }
    '''
