import requests
import validators
from .utils import raise_for_error, get_timestamp, enum, check_hex_value, check_hex_value

REQUEST_TYPES = enum('REQUEST_TYPES',
    RX_KBPS='rx_kbps',
    TX_KBPS='tx_kbps',
    SYSLOAD='load',
    CPU_LOAD='cpu_temp',
    HASHRATE='hash',
    GPU_CORECLOCK='core',
    GPU_MEMCLOCK='mem',
    GPU_FANRPM='fanrpm',
    GPU_TEMP='temp',
    GPU_HASHRATE='miner_hashes',
)

HTTP_METHODS = enum('HTTPMethod',
    GET='GET',
    POST='POST',
    PUT='PUT',
    DELETE='DELETE',
    PATCH='PATCH'
)

class API_Object(object):
    endpoint = None
    _error   = None
    debug    = False

    def __init__(self, endpoint=None, debug=False):
        if endpoint is None:
            raise ValueError("endpoint can't be of NoneType")

        try:
            validators.url(endpoint)
        except:
            raise ValueError("endpoint (%s) is not a valid url." % endpoint)

        if debug:
            print("DEBUG: endpoint = %s" % endpoint)

        self.endpoint = endpoint
        self.debug    = debug

    def make_request(self, method, path, data=None, params=None, headers=None, timeout=60):

        if headers is None:
            headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
        else:
            headers.update({'x-li-format': 'json', 'Content-Type': 'application/json'})

        if params is None:
            params = {}

        method = method.upper()

        if method not in HTTP_METHODS.enums.values():
            method = HTTP_METHODS.GET

        url = self.endpoint + path

        if self.debug:
            print("DEBUG: url => %s" % url)

        kw = dict(data=data, params=params, headers=headers, timeout=timeout)

        return requests.request(method, url, **kw)

    @property
    def last_error(self):
        return self._error

class EthOS_API(API_Object):
    custompanel = None

    def __init__(self, custompanel=None, debug=False):

        if custompanel is None:
            raise ValueError("custompanel is not defined. Please have look to http://########.ethosdistro.com")
        elif len(custompanel) != 6:
            raise ValueError("custompanel (%s) must have only 6 characters" % custompanel)

        self.custompanel  = custompanel
        endpoint          = "http://%s.ethosdistro.com/" % custompanel

        API_Object.__init__(self, endpoint=endpoint, debug=debug)

    def get_summary(self):
        params = dict()
        params.update({'json': 'yes'})

        response = self.make_request(HTTP_METHODS.GET, "", params=params)
        raise_for_error(response)

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        if response.text != "":
            payload["payload"] = response.json()
        else:
            payload["payload"] = dict()

        return payload

    def get_rig_ids(self):
        api_call = self.get_summary()

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        payload["rig_ids"] = list(api_call["payload"]["rigs"].keys())

        return payload

    def get_rig_status(self):
        api_call = self.get_summary()

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        rigs = list(api_call["payload"]["rigs"].keys())

        payload["payload"] = dict()

        for rig in rigs :
            payload["payload"][rig] = api_call["payload"]["rigs"][rig]["condition"]

        return payload

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

    def get_graph_data(self, request=None, rigID=None):
        if request is None:
            raise ValueError("request can't be of NoneType.")
        elif request not in REQUEST_TYPES.enums.values():
            raise ValueError("request must have one of the following values: ['core', 'temp', 'hash', 'miner_hashes', 'rx_kbps', 'fanrpm', 'cpu_temp', 'mem', 'load', 'tx_kbps']")

        if rigID is None:
            raise ValueError("rigID can't be of NoneType")

        elif len(rigID) != 6:
            raise ValueError("rigID (%s) must have only 6 characters" % rigID)

        elif not check_hex_value(rigID):
            raise ValueError("rigID (%s) is not a valid hexadecimal value" % rigID)

        elif rigID not in self.get_rig_ids()["rig_ids"]:
            raise Exception("rigID (%s) is unknown for the user: %s" % (rigID, self.custompanel))

        params = dict()
        params.update({'json': 'yes'})
        params.update({'type': request})
        params.update({'rig': rigID})

        response = self.make_request(HTTP_METHODS.GET, "graphs/", params=params)
        raise_for_error(response)

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        if response.text != "":
            payload["payload"] = response.json()
        else:
            payload["payload"] = dict()

        return payload

class Blockchain_API(API_Object):

    wallet_addr = None

    def __init__(self, wallet=None, debug=False):

        if wallet[:2] == "0x": # Remove prefixed "0x" value
            wallet = wallet[2:]

        if not check_hex_value(wallet):
            raise ValueError("wallet (0x%s) is not a valid hexadecimal value" % wallet)

        elif len(wallet) != 40:
            raise ValueError("wallet (%s) must have only 40 characters without the '0x' prefix" % custompanel)

        endpoint = "https://api.blockcypher.com/"

        API_Object.__init__(self, endpoint=endpoint, debug=debug)

        self.wallet_addr = wallet

    def get_account_balance(self):

        api_path = "v1/eth/main/addrs/%s/balance" % self.wallet_addr

        response = self.make_request(HTTP_METHODS.GET, api_path)
        raise_for_error(response)

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        if response.text != "":
            payload["payload"] = response.json()
        else:
            payload["payload"] = dict()

        return payload

class Ethermine_API(API_Object):

    wallet_addr = None

    def __init__(self, wallet=None, debug=False):

        if wallet[:2] == "0x": # Remove prefixed "0x" value
            wallet = wallet[2:]

        if not check_hex_value(wallet):
            raise ValueError("wallet (0x%s) is not a valid hexadecimal value" % wallet)

        elif len(wallet) != 40:
            raise ValueError("wallet (%s) must have only 40 characters without the '0x' prefix" % custompanel)

        endpoint = "https://ethermine.org/api/"

        API_Object.__init__(self, endpoint=endpoint, debug=debug)

        self.wallet_addr = wallet

    def get_account_stats(self):

        api_path = "miner_new/%s" % self.wallet_addr

        response = self.make_request(HTTP_METHODS.GET, api_path)
        raise_for_error(response)

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        if response.text != "":
            payload["payload"] = response.json()
        else:
            payload["payload"] = dict()

        return payload
