import sys
sys.path.append("..")
del sys
from libvbs.config import Config

def run():
    config = Config("vbs.yaml")
    print(config)
