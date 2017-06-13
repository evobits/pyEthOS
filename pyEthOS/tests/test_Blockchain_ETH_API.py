from unittest import TestCase

import pyEthOS.pyEthOS as ethos

class Test_Blockchain_ETH_API(TestCase):

    def test_valid_account_balance(self):
        raised = False
        error  = ""

        try:
            api = ethos.Blockchain_ETH_API('0xeb090e55b3d0cb2544d5b4fb6f485845068bd932')

            response = api.get_account_balance()

            self.assertTrue(response["success"])

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)
