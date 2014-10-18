import sys
sys.path.append("..")
del sys
from libvbs.config import Config
from libvbs.container import *

def run():
    config = Config("vbs.yaml")
    print(config)
    corenetwork = CoreNetwork(config.general)
    print(corenetwork)
    bts = BaseStation(config.general, config.bts_list[0])
    print(bts)
