import mysql.connector
from db.db_config import DB_CONFIG
import logging

class DBConnection:
    def __init__(self):
        self.cnx = None
        self.logger = logging.getLogger(__name__)

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**DB_CONFIG)
        except mysql.connector.Error as err:
            self.logger.error(f"Failed to connect to database: {err}")

    def get_cursor(self):
        if not self.cnx:
            self.connect()
        try:
            return self.cnx.cursor()
        except mysql.connector.Error as err:
            self.logger.error(f"Failed to get cursor: {err}")

    def commit(self):
        if self.cnx:
            try:
                self.cnx.commit()
            except mysql.connector.Error as err:
                self.logger.error(f"Failed to commit changes: {err}")

    def close(self):
        if self.cnx:
            try:
                self.cnx.close()
            except mysql.connector.Error as err:
                self.logger.error(f"Failed to close database connection: {err}")