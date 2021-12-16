"""
Hello module for telling the end user hello
"""
import logging

from zzztest import __version__


class Hello():
    """
    Hello class that handles calling hello
    """

    def __init__(self):
        """
        Initialize things needed for the class and call entrypoint function
        """
        logging.basicConfig(format='%(levelname)s: %(message)s',
                            level=logging.INFO)
        self.hello()

    @staticmethod
    def hello():
        """
        Say hello and the version
        """
        logging.info('Hi, this is version: %s', __version__)
