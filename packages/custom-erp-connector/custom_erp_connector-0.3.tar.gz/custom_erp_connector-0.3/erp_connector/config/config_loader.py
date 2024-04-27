import json

from erp_connector.utils.singleton import SingletonMeta


class CustomErpConnectorConfig(metaclass=SingletonMeta):
    def __init__(self, config_dict):
        self._config = config_dict

    @property
    def dbType(self):
        return self._config.get("dbType")

    @property
    def connectionDetails(self):
        return self._config.get("connectionDetails")

    @property
    def env(self):
        return self._config.get("env")

    @property
    def authToken(self):
        return self._config.get("authToken")

    @property
    def erpInstanceId(self):
        return self._config.get("erpInstanceId")


class ConfigLoader(metaclass=SingletonMeta):

    def __init__(self, config_path):
        self.config_path = config_path

    def load(self):
        with open(self.config_path, 'r') as file:
            config_dict = json.load(file)
        return CustomErpConnectorConfig(config_dict)
