from unittest import TestCase

import pyEthOS.pyEthOS as ethos

import string, random

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def hex_generator(size=6):
    return '%06x' % random.randint(0, 0xFFFFFF)

class Test_EthOS_API(TestCase):

    ############ __init__() function ############

    def test_invalid_none_custompanel(self):
        self.assertRaises(ValueError, ethos.EthOS_API)

    def test_invalid_custompanel_numeric(self):
        self.assertRaises(ValueError, ethos.EthOS_API, custompanel=12345)

    def test_invalid_custompanel_tooShort(self):
        self.assertRaises(ValueError, ethos.EthOS_API, custompanel="12345") # custompanel is 5 characters long instead of 6

    def test_invalid_custompanel_tooLong(self):
        self.assertRaises(ValueError, ethos.EthOS_API, custompanel="1234567") # custompanel is 7 characters long instead of 6

    def test_valid_custompanel(self):
        raised = False
        error  = ""

        try:
            api = ethos.EthOS_API(custompanel="ethos1")

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    ############ get_summary() function ############

    def test_valid_summary_existingPanel(self):
        raised = False
        error  = ''

        try:
            api = ethos.EthOS_API(custompanel="ethos1")
            response = api.get_summary()

            self.assertTrue(response["success"])

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    def test_valid_summary_unexistingPanel(self):
        raised = False
        error  = ''

        try:
            for _ in range(4): # With 4 randomly generated custompanel names, we are sure that one won't be used
                api = ethos.EthOS_API(custompanel=id_generator())
                response = api.get_summary()

                self.assertTrue(response["success"])

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    ############ get_rig_ids() function ############

    def test_valid_get_rig_ids(self):
        raised = False
        error  = ''

        try:
            api = ethos.EthOS_API(custompanel="ethos1")
            response = api.get_rig_ids()

            self.assertTrue(response["success"])

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    ############ reload_rigs_list() function ############

    def test_valid_reload_rigs_list(self):
        raised = False
        error  = ''

        try:
            api = ethos.EthOS_API(custompanel="ethos1")
            response = api.reload_rigs_list()

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    ############ get_rig_status() function ############

    def test_valid_get_rig_status(self):
        raised = False
        error  = ''

        try:
            api = ethos.EthOS_API(custompanel="ethos1")
            response = api.get_rig_status()

            self.assertTrue(response["success"])

        except Exception as e:
            raised = True
            error  = str(e)

        self.assertFalse(raised, error)

    ############ get_graph_data() function ############

    def test_invalid_get_graph_data_rigNotExisting(self):
        raised = False

        api = ethos.EthOS_API(custompanel="ethos1")

        try:
            for _ in range(4): # With 4 randomly generated rigID, we are sure that one won't be used
                api.get_graph_data(api_request=ethos.ETHOS_API_GRAPH_DATA_ROUTES.SYSLOAD,rigID=hex_generator())

        except RuntimeError as e:
            raised = True

        self.assertTrue(raised, "No RuntimeError has been raised")

    def test_invalid_get_graph_data_rigNone(self):
        api = ethos.EthOS_API(custompanel="ethos1")
        self.assertRaises(
            ValueError,
            api.get_graph_data,
            api_request=ethos.ETHOS_API_GRAPH_DATA_ROUTES.SYSLOAD
        )

    def test_invalid_get_graph_data_rigNumeric(self):
        api = ethos.EthOS_API(custompanel="ethos1")
        self.assertRaises(
            ValueError,
            api.get_graph_data,
            api_request=ethos.ETHOS_API_GRAPH_DATA_ROUTES.SYSLOAD,
            rigID=123
        )

    def test_invalid_get_graph_data_rigTooShort(self):
        api = ethos.EthOS_API(custompanel="ethos1")

        # rigID is 5 characters long instead of 6

        self.assertRaises(
            ValueError,
            api.get_graph_data,
            api_request=ethos.ETHOS_API_GRAPH_DATA_ROUTES.SYSLOAD,
            rigID="12345",
        )

    def test_invalid_get_graph_data_rigTooLong(self):
        api = ethos.EthOS_API(custompanel="ethos1")

        # rigID is 7 characters long instead of 6

        self.assertRaises(
            ValueError,
            api.get_graph_data,
            api_request=ethos.ETHOS_API_GRAPH_DATA_ROUTES.SYSLOAD,
            rigID="1234567",
        )

    def test_invalid_get_graph_data_rigNotHex(self):
        api = ethos.EthOS_API(custompanel="ethos1")

        self.assertRaises(
            ValueError,
            api.get_graph_data,
            api_request=ethos.ETHOS_API_GRAPH_DATA_ROUTES.SYSLOAD,
            rigID="9a704g",
        )

    def test_invalid_get_graph_data_requestNotExist(self):
        api = ethos.EthOS_API(custompanel="ethos1")
        self.assertRaises(
            ValueError,
            api.get_graph_data,
            api_request="systemload",
            rigID="9a704a"
        )

    def test_invalid_get_graph_data_requestNumeric(self):
        api = ethos.EthOS_API(custompanel="ethos1")
        self.assertRaises(
            ValueError,
            api.get_graph_data,
            api_request=132,
            rigID="9a704a"
        )

    def test_invalid_get_graph_data_requestNone(self):
        api = ethos.EthOS_API(custompanel="ethos1")
        self.assertRaises(
            ValueError,
            api.get_graph_data,
            rigID="9a704a"
        )

    def test_valid_get_graph_data(self):
        raised = False
        error  = ''

        try:
            api = ethos.EthOS_API(custompanel="ethos1")
            rig = api.rigs_list[0]

            for request in ethos.ETHOS_API_GRAPH_DATA_ROUTES.values():
                response = api.get_graph_data(request, rig)

                self.assertTrue(response["success"])

        except Exception as e:
            raised = True
            error  = "Rig:" + rig + 'type('+type(rig)+') || Error:' + str(e)

        self.assertFalse(raised, error)
