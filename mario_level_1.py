#!/usr/bin/env python
__author__ = 'justinarmstrong'

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.
"""

import os
os.chdir("C:\\Users\\rgiul\\Mario-Level-1")
print("hello")


import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    main()
    pg.quit()
    sys.exit()