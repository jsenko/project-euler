#!/usr/bin/python3
__author__ = 'jsenko'

import logging

logging.basicConfig(level=logging.DEBUG)

def arithmetic_progression_sum(a, b, step):
    """
    sum from 1 to 5, step 1:
    1+2+3+4+5
    5+4+3+2+1
    ---------
    sum=6*5 / 2
    
    3 +6+9+12
    12+9+6+ 3
    ---------
    sum=15*4 / 2
    
    sum = (a + b) * steps / 2, steps = (b - a) / step + 1
    sum = (a + b) * ((b - a) / step + 1) / 2    
    """
    return (a + b) * ((b - a) / step + 1) / 2
    

if __name__ == "__main__":
    logging.debug(arithmetic_progression_sum(3, 9, 3))
    logging.debug(arithmetic_progression_sum(5, 5, 5))
    print(arithmetic_progression_sum(3, 999, 3) + arithmetic_progression_sum(5, 995, 5) - arithmetic_progression_sum(15, 990, 15))
    