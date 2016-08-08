import os, sys

dirname = os.path.dirname(__file__)
sys.path.insert(0,dirname)
flashelapse, cur = os.path.split(dirname)
sys.path.insert(0,flashelapse)
