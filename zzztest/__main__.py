"""
Entrypoint script that gets installed with the package
"""
import datetime
import logging
import time

import humanize

from zzztest.hello import Hello


def main():
    """
    Main function that is the entypoint of the package
    """
    start = time.time()
    Hello()
    end = time.time()
    elapsed = end - start
    human_elapsed = humanize.naturaldelta(datetime.timedelta(seconds=elapsed))
    logging.info('Elapsed Time: %s seconds (%s)', elapsed, human_elapsed)
