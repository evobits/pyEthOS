# PyEthOS

[![Build Status](https://travis-ci.org/DEKHTIARJonathan/pyEthOS.svg?branch=master)](https://travis-ci.org/DEKHTIARJonathan/pyEthOS)
[![PyPI version](https://badge.fury.io/py/pyEthOS.svg)](https://badge.fury.io/py/pyEthOS)

Python 2 and 3 interface to the EthOS custom Dashboard API

This library provides a pure Python interface to the EthOS Custom Dashboard REST APIs.

## Maintainer
[Jonathan Dekhtiar](https://github.com/DEKHTIARJonathan)

## Documentation is available here:
https://dekhtiarjonathan.github.io/pyEthOS/

## Installation

The library is available with PIP:

```shell
pip install PyEthOS
```

If prefered, the library can be compiled with following commands:

```shell
## First clone the repository
git clone https://github.com/DEKHTIARJonathan/pyEthOS.git

## Then install the library
python setup.py install
```

## Docuementation

### 1. EthOS API Documentation

```python
import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':

    PANEL_NAME = "ethos1"
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.EthOS_API(PANEL_NAME, debug=DEBUG)

    print (api.get_summary())

    '''
    {
        "rigs": {
            "######": {
                "condition": "######",
                "version": "######",
                "miner": "######",
                "gpus": "######",
                "miner_instance": "######",
                "miner_hashes": "######",
                "bioses": "######",
                "meminfo": "######",
                "vramsize": "######",
                "drive_name": "######",
                "mobo": "######",
                "lan_chip": "R######",
                "connected_displays": "",
                "ram": "######",
                "rack_loc": "######",
                "ip": "######",
                "driver": "######",
                "server_time": 0,
                "uptime": "######",
                "miner_secs": 0,
                "rx_kbps": "######",
                "tx_kbps": "######",
                "load": "######",
                "cpu_temp": "######",
                "freespace": 0,
                "hash": 0,
                "pool": "######",
                "temp": "######",
                "powertune": "######",
                "fanrpm": "######",
                "core": "######",
                "mem": "######"
            }
        },
        "total_hash": 0,
        "alive_gpus": 0,
        "total_gpus": 0,
        "alive_rigs": 0,
        "total_rigs": 0,
        "current_version": "######",
        "avg_temp": 0,
        "capacity": "######",
        "per_info": {
            "claymore": {
                "hash": 0,
                "per_alive_gpus": 0,
                "per_total_gpus": 0,
                "per_alive_rigs": 0,
                "per_total_rigs": 0,
                "per_hash-gpu": "######",
                "per_hash-rig": "######"
            }
        }
    }
    '''

    print(api.get_rig_status())
    '''
    {
        "success": "True",
        "timestamp": "2017-06-12 12:51:15",
        "payload": {
            "######": "unreachable",
            "######": "mining",
            "######": "mining",
            "######": "unreachable",
        }
    }
    '''

    print(api.get_rig_ids())
    '''
    {
        "success": "True",
        "rig_ids": [
            "######",
            "######",
            "######"
        ],
        "timestamp": "2017-06-12 12:54:15"
    }
    '''
    #####################
    # Available routes:
    ######################

    # ethos.REQUEST_TYPES.RX_KBPS
    # ethos.REQUEST_TYPES.TX_KBPS
    # ethos.REQUEST_TYPES.SYSLOAD
    # ethos.REQUEST_TYPES.CPU_LOAD
    # ethos.REQUEST_TYPES.HASHRATE
    # ethos.REQUEST_TYPES.GPU_CORECLOCK
    # ethos.REQUEST_TYPES.GPU_MEMCLOCK
    # ethos.REQUEST_TYPES.GPU_FANRPM
    # ethos.REQUEST_TYPES.GPU_TEMP
    # ethos.REQUEST_TYPES.GPU_HASHRATE

    print(api.get_graph_data(ethos.REQUEST_TYPES.SYSLOAD, "e057d6"))
    '''
    {
        "success": "True",
        "payload": {
            "e057d6 sysload": [
                "1494859237000 0.30",
                "1494859529000 0.30",
                "1494859835000 0.27",
                "1494860134000 0.27",
                "1494860439000 0.28"
            ]
        },
        "timestamp": "2017-06-12 13:37:22"
    }
    '''
```

### 2. Blockchain API Documentation

```python
import pyEthOS.pyEthOS as ethos

if __name__ == '__main__':
    wallet_addr = "eb090e55b3d0cb2544d5b4fb6f485845068bd932" # The API is able to handle address with the prefix "0x" or no prefix.
    DEBUG = False # Allow development debug infos to be printed on the console

    api = ethos.Blockchain_API(wallet_addr, debug=DEBUG)

    print(api.get_account_balance())
    '''
    {
    	"payload": {
    		"balance": 0,
    		"final_balance": 0,
    		"total_sent": 0,
    		"address": "260e285b113b8be32a5141c35d18257792c757db",
    		"total_received": 0,
    		"final_n_tx": 0,
    		"n_tx": 0,
    		"unconfirmed_balance": 0,
    		"unconfirmed_n_tx": 0
    	},
    	"timestamp": "2017-06-12 15:51:15",
    	"success": "True"
    }
    '''
```

### 3. Ethermine Pool API Documentation

```python
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
```

## Disclaimer
This Python Package is not affiliated with EthOS distribution available on [ethosdistro.com](http://ethosdistro.com/).

The Author expressly disclaims any warranty for this product, including all descriptions, documentation, and on-line documentation. This Software is provided 'AS IS' without warranty of any kind, including without limitation, any implied warranties of fitness for a particular purpose or result. You agree to assume the entire risk for any damage or result arising from its download, installation and use, including the license process. In no event will the Author (or his agents and/or associates) be liable to you for any incidental or consequential damages or losses whatsoever, including without limitation, damage to data, property or profits, arising from any use, or from any inability to use said Software.
