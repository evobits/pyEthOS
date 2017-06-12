import os, time, requests
import validators

from .utils import get_timestamp, enum, check_hex_value, get_exception_for_error_code

is_travis = 'TRAVIS' in os.environ

ETHOS_API_GRAPH_DATA_ROUTES = enum('ETHOS_API_GRAPH_DATA_ROUTES',
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
    debug    = False

    def __init__(self, endpoint=None, debug=False):

        if endpoint is None:
            raise ValueError("endpoint can't be of NoneType")

        elif not isinstance(endpoint, str):
            raise ValueError("endpoint must be a string")

        elif not validators.url(endpoint):
            raise ValueError("endpoint (%s) is not a valid url." % endpoint)

        elif not isinstance(debug, bool):
            raise ValueError("debug must be a bool")

        if debug:
            print("DEBUG: endpoint = %s" % endpoint)

        self.endpoint = endpoint
        self.debug    = debug

    def make_request(self, method, path, data=None, params=None, headers=None, timeout=60):

        # Method Validation

        if not isinstance(method, str):
            raise ValueError("method must be a string")

        elif method not in HTTP_METHODS.enums.values():
            raise ValueError("The method value (%s) is not supported, please use one of the following ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']" % method)

        else:
            method = method.upper()

        # Headers Validation

        if headers is None:
            headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
        else:
            if not isinstance(headers, dict):
                raise ValueError("headers must be a dict")
            else:
                headers.update({'x-li-format': 'json', 'Content-Type': 'application/json'})

        # Params Validation

        if params is None:
            params = dict()

        elif not isinstance(params, dict):
            raise ValueError("params must be a dict")


        # PATH and URL Validation

        if not isinstance(path, str):
            raise ValueError("path must be a string")

        elif len(path) > 0 and path[0] == "/":
            path = path[1:]

        else:
            url = self.endpoint + path

        if not validators.url(url):
            raise ValueError("url (%s) is not a valid url." % url)

        ############# Sending the Request #############

        kw = dict(data=data, params=params, headers=headers, timeout=timeout)

        if self.debug:
            print("DEBUG: url => %s" % url)

        if is_travis:
            time.sleep(1) # Temporisation to avoid HTTP 429 : Too Many Requests

        response = requests.request(method, url, **kw)

        try:
            response.raise_for_status()
            return response
        except:
            raise RuntimeError(get_exception_for_error_code(response.status_code))

class Eth_Wallet_API_Object(API_Object):
    wallet_addr = None

    def __init__(self, wallet=None, debug=False, endpoint=None):

        if wallet is None:
            raise ValueError("wallet can't be of NoneType.")

        if not isinstance(wallet, str):
            raise ValueError("wallet must be a string")

        elif wallet[:2] == "0x": # Remove prefixed "0x" value
                wallet = wallet[2:]

        if not check_hex_value(wallet):
            raise ValueError("wallet (0x%s) is not a valid hexadecimal value" % wallet)

        elif len(wallet) != 40:
            raise ValueError("wallet (%s) must have only 40 characters without the '0x' prefix" % wallet)

        self.wallet_addr = wallet

        API_Object.__init__(self, endpoint=endpoint, debug=debug)

class EthOS_API(API_Object):
    custompanel = None
    rigs_list   = None

    def __init__(self, custompanel=None, debug=False):

        if custompanel is None:
            raise ValueError("custompanel is not defined. Please have look to http://########.ethosdistro.com")

        elif not isinstance(custompanel, str):
            raise ValueError("custompanel must be a string")

        elif len(custompanel) != 6:
            raise ValueError("custompanel (%s) must have only 6 characters" % custompanel)

        self.custompanel  = custompanel
        endpoint          = "http://%s.ethosdistro.com/" % custompanel

        API_Object.__init__(self, endpoint=endpoint, debug=debug)

        self.reload_rigs_list()

    def get_summary(self):
        params = dict()
        params.update({'json': 'yes'})

        response = self.make_request(HTTP_METHODS.GET, "", params=params)

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

        self.rigs_list = payload["rig_ids"] # We update the list

        return payload

    def reload_rigs_list(self):
        self.get_rig_ids()

    def get_rig_status(self):
        api_call = self.get_summary()

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        rigs = list(api_call["payload"]["rigs"].keys())
        self.rigs_list = rigs # We update the list

        payload["payload"] = dict()

        for rig in rigs :
            payload["payload"][rig] = api_call["payload"]["rigs"][rig]["condition"]

        return payload

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

    def get_graph_data(self, api_request=None, rigID=None):

        # api_request Validation

        if api_request is None:
            raise ValueError("api_request can't be of NoneType.")

        elif not isinstance(api_request, str):
            raise ValueError("api_request must be a string")

        elif api_request not in ETHOS_API_GRAPH_DATA_ROUTES.enums.values():
            raise ValueError("api_request must have one of the following values: ['core', 'temp', 'hash', 'miner_hashes', 'rx_kbps', 'fanrpm', 'cpu_temp', 'mem', 'load', 'tx_kbps']")

        # rigID Validation

        if rigID is None:
            raise ValueError("rigID can't be of NoneType")

        elif not isinstance(rigID, str):
            raise ValueError("rigID must be a string")

        elif len(rigID) != 6:
            raise ValueError("rigID (%s) must have only 6 characters" % rigID)

        elif not check_hex_value(rigID):
            raise ValueError("rigID (%s) is not a valid hexadecimal value" % rigID)

        elif rigID not in self.rigs_list:
            raise RuntimeError("rigID (%s) is unknown for the user: %s" % (rigID, self.custompanel))

        params = dict()
        params.update({'json': 'yes'})
        params.update({'type': api_request})
        params.update({'rig': rigID})

        response = self.make_request(HTTP_METHODS.GET, "graphs/", params=params)

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        if response.text != "":
            payload["payload"] = response.json()
        else:
            payload["payload"] = dict()

        return payload

class Blockchain_API(Eth_Wallet_API_Object):

    def __init__(self, wallet=None, debug=False):

        endpoint = "https://api.blockcypher.com/"

        Eth_Wallet_API_Object.__init__(self, wallet=wallet, endpoint=endpoint, debug=debug)

    def get_account_balance(self):

        api_path = "v1/eth/main/addrs/%s/balance" % self.wallet_addr

        response = self.make_request(HTTP_METHODS.GET, api_path)

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        if response.text != "":
            payload["payload"] = response.json()
        else:
            payload["payload"] = dict()

        return payload

class Ethermine_API(Eth_Wallet_API_Object):

    def __init__(self, wallet=None, debug=False):

        endpoint = "https://ethermine.org/api/"

        Eth_Wallet_API_Object.__init__(self, wallet=wallet, endpoint=endpoint, debug=debug)

    def get_account_stats(self):

        api_path = "miner_new/%s" % self.wallet_addr

        response = self.make_request(HTTP_METHODS.GET, api_path)

        payload = dict()

        payload["success"] = True
        payload ["timestamp"] = get_timestamp()

        if response.text != "":
            payload["payload"] = response.json()
        else:
            payload["payload"] = dict()

        return payload
