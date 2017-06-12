from unittest import TestCase

import pyEthOS.pyEthOS as ethos

class Test_Eth_Wallet_API_Object(TestCase):

    def test_invalid_wallet_none(self):
        self.assertRaises(ValueError, ethos.Eth_Wallet_API_Object)

    def test_invalid_wallet_numeric(self):
        self.assertRaises(ValueError, ethos.Eth_Wallet_API_Object, wallet=24)

    def test_invalid_wallet_tooShort(self):
        self.assertRaises(ValueError, ethos.Eth_Wallet_API_Object, wallet='eb090e55b3d0cb2544d5b4fb6f485845068bd93') # Wallet is 39 characters long instead of 40

    def test_invalid_wallet_tooLong(self):
        self.assertRaises(ValueError, ethos.Eth_Wallet_API_Object, wallet='eb090e55b3d0cb2544d5b4fb6f485845068bd9323') # Wallet is 41 characters long instead of 40

    def test_invalid_wallet_notHex(self):
        self.assertRaises(ValueError, ethos.Eth_Wallet_API_Object, wallet='eG090e55b3d0cb2544d5b4fb6f485845068bd932')

    def test_valid_wallet(self, addr='eb090e55b3d0cb2544d5b4fb6f485845068bd932'):
        raised = False
        error  = ""

        try:
            api = ethos.Eth_Wallet_API_Object('eb090e55b3d0cb2544d5b4fb6f485845068bd932', endpoint = "https://api.blockcypher.com/") # Endpoint is checked by API_Object, not tested here

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    def test_valid_wallet_with_0x(self):
        self.test_valid_wallet(addr='0xeb090e55b3d0cb2544d5b4fb6f485845068bd932')
