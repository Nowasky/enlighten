# Copyright 2019 Avram Lubkin, All Rights Reserved

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Demo of Enlighten's features
"""

import platform
import random
import time

import enlighten

from multicolored import run_tests, load
from multiple_logging import process_files, win_time_granularity


def initialize(manager, initials=15):
    """
    Simple progress bar example
    """

    # Simulated preparation
    pbar = manager.counter(total=initials, desc='Initializing:', unit='initials')
    for num in range(initials):  # pylint: disable=unused-variable
        time.sleep(random.uniform(0.1, 0.5))  # Random processing time
        pbar.update()
    pbar.close()


def main():
    """
    Main function
    """

    with enlighten.get_manager() as manager:
        status = manager.status_bar(status_format=u'Current demo: {demo}', color='red',
                                    justify=enlighten.Justify.CENTER, demo='Initialize')
        initialize(manager, 15)
        status.update(demo='Load')
        load(manager, 80)
        status.update(demo='Testing')
        run_tests(manager, 40)
        status.update(demo='File Processing')
        process_files(manager)


if __name__ == '__main__':

    if platform.system() == 'Windows':
        with win_time_granularity(1):
            main()
    else:
        main()
