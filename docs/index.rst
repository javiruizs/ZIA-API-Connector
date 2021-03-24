.. ZIA-API-Connector documentation master file, created by
   sphinx-quickstart on Wed Mar 24 19:32:36 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ZIA-API-Connector's documentation!
=============================================

The ZIA-API-Connector is basically a Python-CLI script which you can use to interact with any Zscaler Internet Access
(ZIA) tennant, as long as it has the API functionality activated and an active API key.

This project is composed on three basic pilars:

*  The script which you can run as a program: :code:`ziaclient.py`
*  The package where the API calls and the session class have been implemented: :code:`zia_client`
*  The package where the argument parser has been built and the mapping of the different subparsers and their arguments
   to the methods of the package above.

None of the three pilars are complete. It's still a work in progress.

The script will let you work with location, user and VPN management.
The package has much more functionality defined. You can see how far I have gone by seeing the tables defined in the
README file on the GitHub repository.


**Please, be advised** that this is a small project on which only I have worked. As mentioned on the license,
I guarantee no absolute correct behavior. Not all functionality has been tested nor implemented. I do have worked a lot
of the time with the :code:`user` and :code:`location` functionality for both script and package.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Contents:

   script
   modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
