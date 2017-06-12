import pyEthOS.pyEthOS as pyeth

if __name__ == '__main__':

    PANEL_NAME = "ethos1"

    api = pyeth.EthOSApplication(PANEL_NAME)

    print (api.get_summary())
