# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.DEBUG)
astar_logger = logging.getLogger('AStar')
test_logger = logging.getLogger('test')

def setupAStarLogger():
    astar_logger.setLevel(logging.WARNING)  
#    astar_logger.setLevel(logging.DEBUG)          

def setupTestLogger():
    test_logger.setLevel(logging.WARNING)    
#    test_logger.setLevel(logging.INFO)  
#    test_logger.setLevel(logging.DEBUG)
    
setupAStarLogger()
setupTestLogger()