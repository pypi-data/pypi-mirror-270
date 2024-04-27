import json

from erp_connector.db.mssql_connector import MsSqlConnector
from erp_connector.db.mysql_connector import MySqlConnector
from erp_connector.db.postgresql_connector import PostgresSQLConnector


class ConfigLoader:
    def __init__(self, path):
        self.path = path

    def load(self):
        with open(self.path, 'r') as file:
            config = json.load(file)
        return config


class ConnectionLoader:
    @staticmethod
    def load_connector(custom_erp_connector_config):
        connector = ConnectorFactory.create_connector(custom_erp_connector_config)
        return connector


class ConnectorFactory:
    @staticmethod
    def create_connector(erp_connector_config):
        db_type = erp_connector_config.dbType
        connection_details = erp_connector_config.connectionDetails
        if db_type == 'mysql':
            print("creating mysql connector")
            return MySqlConnector(connection_details)
        elif db_type == 'postgresql':
            print("creating postgresql connector")
            return PostgresSQLConnector(connection_details)
        elif db_type == 'mssql':
            print("creating mssql connector")
            return MsSqlConnector(connection_details)
        else:
            raise ValueError("Invalid db connector config: dbName must be 'mysql' or 'postgresql'")
