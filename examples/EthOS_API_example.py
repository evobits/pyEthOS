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
