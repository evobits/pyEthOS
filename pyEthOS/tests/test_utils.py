from unittest import TestCase

import pyEthOS.pyEthOS as ethos
import pyEthOS.utils as utils

class Test_Utils(TestCase):

    def test_valid_HTTP_METHODS(self):

        expected_keys   = ['PUT', 'PATCH', 'GET', 'POST', 'DELETE']
        expected_values = ['PUT', 'PATCH', 'GET', 'POST', 'DELETE']

        self.assertListEqual(sorted(ethos.HTTP_METHODS.values()), sorted(expected_values))
        self.assertListEqual(sorted(ethos.HTTP_METHODS.keys()), sorted(expected_keys))

    def test_valid_ETHOS_API_GRAPH_DATA_ROUTES(self):

        expected_keys   = ['SYSLOAD', 'GPU_FANRPM', 'GPU_TEMP', 'CPU_LOAD', 'GPU_HASHRATE', 'GPU_CORECLOCK', 'HASHRATE', 'RX_KBPS', 'TX_KBPS', 'GPU_MEMCLOCK']
        expected_values = ['load', 'fanrpm', 'temp', 'cpu_temp', 'miner_hashes', 'core', 'hash', 'rx_kbps', 'tx_kbps', 'mem']

        self.assertListEqual(sorted(ethos.ETHOS_API_GRAPH_DATA_ROUTES.values()), sorted(expected_values))
        self.assertListEqual(sorted(ethos.ETHOS_API_GRAPH_DATA_ROUTES.keys()), sorted(expected_keys))
