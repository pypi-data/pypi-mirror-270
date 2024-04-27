import json
from datetime import date
from decimal import Decimal

import pyodbc
from erp_connector.db.db_connector import DBConnector
from erp_connector.utils.mysql_query_utils import generate_data_query


class MsSqlConnector(DBConnector):

    def __init__(self, connection_details):
        super().__init__(connection_details)
        self.connection = None

    def connect_db(self):
        try:
            conn_str = (
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={self.connection_details['host']},{self.connection_details['port']};"
                f"DATABASE={self.connection_details['database']};"
                f"UID={self.connection_details['user']};"
                f"PWD={self.connection_details['password']}"
            )
            self.connection = pyodbc.connect(conn_str)
            print(f"Connected to MSSQL Server database: {self.connection_details['database']}")
        except pyodbc.Error as e:
            print(f"Error connecting to MSSQL Server database: {e}")

    def fetch_data(self, query):
        try:
            cursor = self.connection.cursor(dictionary=True)  # Use dictionary cursor to fetch rows as dictionaries
            cursor.execute(query)
            data = cursor.fetchall()

            # Convert Decimal objects to float
            for row in data:
                for key, value in row.items():
                    if isinstance(value, Decimal):
                        row[key] = float(value)
                    elif isinstance(value, date):
                        row[key] = value.strftime('%Y-%m-%d')

            cursor.close()
            return json.dumps(data)  # Convert data to JSON string
        except pyodbc.Error as e:
            print(f"Error fetching data from MSSQL Server database: {e}")
            return None

    def insert_data(self, update_query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query)
            self.connection.commit()
            cursor.close()
            print("Data inserted into MSSQL Server database successfully")
        except pyodbc.Error as e:
            self.connection.rollback()
            print(f"Error inserting data into MSSQL Server database: {e}")

    def generate_query(self, json_data):
        return generate_data_query(json_data)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to MSSQL database closed")
