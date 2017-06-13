from unittest import TestCase

import pyEthOS.pyEthOS as ethos

class Test_Ethermine_ETH_API(TestCase):

    def test_valid_account_stats(self):
        raised = False
        error  = ""

        try:
            api = ethos.Ethermine_ETH_API('0xeb090e55b3d0cb2544d5b4fb6f485845068bd932')
            response = api.get_account_stats()

            self.assertTrue(response["success"])

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)
