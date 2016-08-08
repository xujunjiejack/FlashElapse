
'''This init is to setup the path so that some modules in this package can talk to others'''
import os, sys
dirname = os.path.dirname(__file__)
sys.path.insert(0,dirname)
flashelapse, cur = os.path.split(dirname)
sys.path.insert(0,flashelapse)
