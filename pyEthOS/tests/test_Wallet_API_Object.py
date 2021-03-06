from unittest import TestCase

import pyEthOS.pyEthOS as ethos

class Test_Wallet_API_Object(TestCase):

    def test_invalid_wallet_none(self):
        self.assertRaises(ValueError, ethos.Wallet_API_Object)

    def test_invalid_wallet_numeric(self):
        self.assertRaises(ValueError, ethos.Wallet_API_Object, wallet=24, wallet_min_length=40, wallet_max_length=40)

    def test_invalid_wallet_tooShort(self):
        self.assertRaises(
            ValueError,
            ethos.Wallet_API_Object,
            wallet='eb090e55b3d0cb2544d5b4fb6f485845068bd93',
            wallet_min_length=40,
            wallet_max_length=40
        ) # Wallet is 39 characters long instead of 40

    def test_invalid_wallet_tooLong(self):
        self.assertRaises(
            ValueError,
            ethos.Wallet_API_Object,
            wallet='eb090e55b3d0cb2544d5b4fb6f485845068bd9323',
            wallet_min_length=40,
            wallet_max_length=40
        ) # Wallet is 41 characters long instead of 40

    def test_invalid_wallet_notHex(self):
        self.assertRaises(
            ValueError,
            ethos.Wallet_API_Object,
            wallet='eG090e55b3d0cb2544d5b4fb6f485845068bd932',
            wallet_min_length=40,
            wallet_max_length=40
        )

    def test_valid_wallet(self, addr='eb090e55b3d0cb2544d5b4fb6f485845068bd932'):
        raised = False
        error  = ""

        try:
            api = ethos.Wallet_API_Object(
                'eb090e55b3d0cb2544d5b4fb6f485845068bd932',
                endpoint = "https://api.blockcypher.com/",
                wallet_min_length=40,
                wallet_max_length=40
            ) # Endpoint is checked by API_Object, not tested here

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    def test_valid_wallet_with_0x(self):
        self.test_valid_wallet(addr='0xeb090e55b3d0cb2544d5b4fb6f485845068bd932')
