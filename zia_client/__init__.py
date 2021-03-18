"""
This package contains the class that implements the API connector for the ZIA (Zscaler Internet Access) portal.

It is divided in various modules, being the main one the `session` module. In this module, the class mentioned above.

In the `custom` module you can find custom methods for specific actions that, at least I have found useful, automatizes
some processes for which the usage of the API is recommended.

The `exceptions` module contains the user-defined Exceptions that may be used when errors occur.
As of now, only one has been defined.

The `utils` module contains handy functions that can be called over and over in order to not repeat code.
"""