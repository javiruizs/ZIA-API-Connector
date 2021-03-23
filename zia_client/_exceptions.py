"""
Module where custom exceptions are defined.
"""


class ResponseException(Exception):
    """
    Exception raised when any Response error occurred.
    """

    def __init__(self, message='The response had error status.'):
        """
        Generic response exception. Useful for this purpose.

        Args:
            message: Message to display.
        """
        super().__init__(message)
