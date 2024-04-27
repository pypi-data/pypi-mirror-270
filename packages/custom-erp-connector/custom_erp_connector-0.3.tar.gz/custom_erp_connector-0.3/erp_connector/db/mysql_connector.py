import json
from datetime import date
from decimal import Decimal

import mysql.connector
from erp_connector.db.db_connector import DBConnector
from erp_connector.utils.mysql_query_utils import generate_data_query


class MySqlConnector(DBConnector):

    def __init__(self, connection_details):
        super().__init__(connection_details)
        self.connection = None

    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.connection_details['host'],
                user=self.connection_details['user'],
                password=self.connection_details['password'],
                database=self.connection_details['database']
            )
            print(f"Connected to MySQL database: {self.connection_details['database']}")
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

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
        except mysql.connector.Error as e:
            print(f"Error fetching data from MySQL database: {e}")
            return None  # Return None if there's an error

    def insert_data(self, update_query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query)
            self.connection.commit()
            cursor.close()
            print("Data inserted into MySQL database successfully")
        except mysql.connector.Error as e:
            self.connection.rollback()
            print(f"Error inserting data into MySQL database: {e}")

    def generate_query(self, json_data):
        return generate_data_query(json_data)

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to MySQL database closed")
