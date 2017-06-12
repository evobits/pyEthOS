PyEthOS
=======

|Build Status| |PyPI version|

Python 2 and 3 interface to the EthOS custom Dashboard API

This library provides a pure Python interface to the EthOS Custom
Dashboard REST APIs.

Maintainer
----------

`Jonathan Dekhtiar <https://github.com/DEKHTIARJonathan>`__

Documentation is available here:
--------------------------------

https://dekhtiarjonathan.github.io/pyEthOS/

Installation
------------

The library is available with PIP:

.. code:: shell

    pip install PyEthOS

If prefered, the library can be compiled with following commands:

.. code:: shell

    ## First clone the repository
    git clone https://github.com/DEKHTIARJonathan/pyEthOS.git

    ## Then install the library
    python setup.py install

Example
-------

.. code:: python

    import pyEthOS.pyEthOS as pyeth

    if __name__ == '__main__':

        PANEL_NAME = "ethos1"

        api = pyeth.EthOSApplication(PANEL_NAME)

        print (api.get_summary())

Disclaimer
----------

This Python Package is not affiliated with EthOS distribution available
on `ethosdistro.com <http://ethosdistro.com/>`__.

The Author expressly disclaims any warranty for this product, including
all descriptions, documentation, and on-line documentation. This
Software is provided 'AS IS' without warranty of any kind, including
without limitation, any implied warranties of fitness for a particular
purpose or result. You agree to assume the entire risk for any damage or
result arising from its download, installation and use, including the
license process. In no event will the Author (or his agents and/or
associates) be liable to you for any incidental or consequential damages
or losses whatsoever, including without limitation, damage to data,
property or profits, arising from any use, or from any inability to use
said Software.

.. |Build Status| image:: https://travis-ci.org/DEKHTIARJonathan/pyEthOS.svg?branch=master
   :target: https://travis-ci.org/DEKHTIARJonathan/pyEthOS
.. |PyPI version| image:: https://badge.fury.io/py/pyEthOS.svg
   :target: https://badge.fury.io/py/pyEthOS
