import yaml
try:
    from yaml import Cloader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class Config:
    def __init__(self, path):
        """VBS configuration parser"""
        self.general = {}
        self.bts_lists = []
        self.filepath = path
        self.read_file()

    def read_file(self):
        """Read contents from self.filepath"""
        with open(self.filepath, 'r') as config_file:
            section = yaml.load(config_file, Loader=Loader)
            self.general = section['general']
            self.bts_lists = section['bts_lists']

    def __str__(self):
        return "General settings:\n{0}\nBTS Lists:\n{1}".format(self.general, self.bts_lists)
