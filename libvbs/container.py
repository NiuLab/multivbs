__all__ = ['CoreNetwork', 'BaseStation']

specific_keys = {
        'UHD_ADDR' : ['uhd_addr'],
        'BCC' : ['BaseStationColorCode', 'Base Station Color Code'],
        'LAC' : ['LocationAreaCode', 'Location Area Code'],
        'CID' : ['CellID', 'Cell ID']
        }

generic_keys = {
        'MCC' : ['MobileCountryCode', 'Mobile Country Code'],
        'MNC' : ['MobileNetworkCode', 'Mobile Network Code'],
        'NCC' : ['NetworkColorCode', 'Network Color Code']
        }

def dealias_values(Dict, Keys):
    NewDict = dict()
    for k, aliases in Keys.items():
        if k in Dict:
            NewDict[k] = Dict[k]
            continue
        else:
            for alias in aliases:
                if alias in Dict:
                    NewDict[k] = Dict[alias]
    return NewDict

class Container:
    """Basic Docker Container Wrapper"""
    def __init__(self, image, env):
        self.image = image
        self.env = env

    def __str__(self):
        return "Image: {0}\nEnvironments: {1}".format(str(self.image), str(self.env))


class CoreNetwork(Container):
    """Container for CoreNetwork"""
    def __init__(self, general_opt):
        super().__init__(general_opt['image']['sip'], {})


class BaseStation(Container):
    """Container for BaseStation"""
    def __init__(self, general_opt, specific_opt):
        general_settings = dealias_values(general_opt, generic_keys)
        specific_settings = dealias_values(specific_opt, specific_keys)
        env = dict(general_settings.items() | specific_settings.items())
        super().__init__(general_opt['image']['bts'], env)
