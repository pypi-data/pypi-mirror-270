import psycopg2
from erp_connector.db.db_connector import DBConnector


class PostgresSQLConnector(DBConnector):

    def __init__(self, connection_details):
        super().__init__(connection_details)
        self.connection = None

    def connect_db(self):
        try:
            self.connection = psycopg2.connect(
                host=self.connection_details['host'],
                user=self.connection_details['user'],
                password=self.connection_details['password'],
                database=self.connection_details['database']
            )
            print(f"Connected to PostgreSQL database: {self.connection_details['database']}")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL database: {e}")

    def fetch_data(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            return data
        except psycopg2.Error as e:
            print(f"Error fetching data from PostgreSQL database: {e}")

    def insert_data(self, update_query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query)
            self.connection.commit()
            cursor.close()
            print("Data inserted into PostgreSQL database successfully")
        except psycopg2.Error as e:
            self.connection.rollback()
            print(f"Error inserting data into PostgreSQL database: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to PostgreSQL database closed")
