#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os
import logging
from my_logger import astar_logger
from my_logger import test_logger
astar_logger.setLevel(logging.WARNING)  
test_logger.setLevel(logging.WARNING)

loader = unittest.TestLoader()
start_dir = os.getcwd()
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)

input("Press enter to exit...")