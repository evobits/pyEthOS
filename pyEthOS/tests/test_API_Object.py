from unittest import TestCase

import pyEthOS.pyEthOS as ethos

class Test_API_Object(TestCase):

    ############ __init__() function ############

    def test_invalid_endpoint_none(self):
        self.assertRaises(ValueError, ethos.API_Object)

    def test_invalid_endpoint_numeric(self):
        self.assertRaises(ValueError, ethos.API_Object, endpoint=123)

    def test_invalid_endpoint_badurl(self):
        self.assertRaises(ValueError, ethos.API_Object, endpoint="htp://www.invalidurl.com")

    def test_invalid_debug_numeric(self):
        self.assertRaises(ValueError, ethos.API_Object, endpoint="https://api.blockcypher.com/", debug=123)

    def test_valid_endpoint(self):
        raised = False
        try:
            api = ethos.API_Object(endpoint="https://api.blockcypher.com/")
        except:
            raised = True
        self.assertFalse(raised, 'Exception raised')

    def test_valid_debug_True(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/", debug=True)
        self.assertTrue(api.debug, 'Exception raised')

    def test_valid_debug_False(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/", debug=False)
        self.assertFalse(api.debug, 'Exception raised')

    ############ make_request() function ############

    def test_invalid_method_request_unexisting(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/")
        self.assertRaises(ValueError, api.make_request, method="GEET", path="v1/eth/main")

    def test_invalid_method_request_numeric(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/")
        self.assertRaises(ValueError, api.make_request, method=123, path="v1/eth/main")

    def test_invalid_path_request_unexisting(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/")
        self.assertRaises(RuntimeError, api.make_request, method="GET", path="v1/eth/mainn")

    def test_invalid_path_request_numeric(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/")
        self.assertRaises(ValueError, api.make_request, method="GET", path=123)

    def test_invalid_path_request_badPath(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/")
        self.assertRaises(ValueError, api.make_request, method="GET", path="v1/eth /main")

    def test_invalid_headers_request_list(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/")
        self.assertRaises(ValueError, api.make_request, method="GET", path="v1/eth/main", headers=list())

    def test_invalid_params_request_list(self):
        api = ethos.API_Object(endpoint="https://api.blockcypher.com/")
        self.assertRaises(ValueError, api.make_request, method="GET", path="v1/eth/main", params=list())

    def test_valid_request(self, path="v1/eth/main", params=None, headers=None, debug=False):

        raised = False
        error  = ''

        try:
            api = ethos.API_Object(endpoint="https://api.blockcypher.com/", debug=debug)
            response = api.make_request(ethos.HTTP_METHODS.GET, path, params, headers)

            reference_dict = {
                "name": "",
                "height": 0,
                "hash": "",
                "time": "",
                "latest_url": "",
                "previous_hash": "",
                "previous_url": "",
                "peer_count": 0,
                "unconfirmed_count": 0,
                "high_gas_price": 0,
                "medium_gas_price": 0,
                "low_gas_price": 0,
                "last_fork_height": 0,
                "last_fork_hash": ""
            }

            self.assertTrue(reference_dict.keys() <= response.json().keys()) # Check if all keys existing in reference_dict are present

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    def test_valid_headers_request_dict(self):
        self.test_valid_request(headers=dict())

    def test_valid_params_request_dict(self):
        self.test_valid_request(params=dict())

    def test_valid_path_request_dict_startingSlash(self):
        self.test_valid_request(path="/v1/eth/main")

    def test_valid_request_dict_withDebug(self):
        self.test_valid_request(debug=True)
