# Import required libraries
import json
import csv
from db.db_connection import DBConnection
from models.user import User
from utils.common_utils import set_default_values
import logging

# Define the UserService class
class UserService:
    # Initialize the class with a DBConnection object and a logger
    def __init__(self):
        self.db_connection = DBConnection()
        self.logger = logging.getLogger(__name__)

    # Method to create a new user in the database
    def create_user(self, user):
        # Get a cursor object from the DBConnection
        cursor = self.db_connection.get_cursor()
        if cursor:
            try:
                # Define the SQL query to insert a new user
                query = ("INSERT INTO users "
                          "(user_id, first_name, last_name, personal_email, phone, password_hash, profile_picture, created_dt, modified_dt) "
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                # Execute the SQL query with the user data
                cursor.execute(query, (user.user_id, user.first_name, user.last_name, user.personal_email, user.phone, user.password_hash, user.profile_picture, user.created_dt, user.modified_dt))
                # Commit the changes to the database
                self.db_connection.commit()
                # Return True to indicate success
                return True
            except mysql.connector.Error as err:
                # Log any errors that occur during the execution
                self.logger.error(f"Failed to create user: {err}")
                # Return False to indicate failure
                return False
            finally:
                # Close the cursor object
                cursor.close()

    # Method to bulk insert users from a JSON or CSV file
    def bulk_insert_users(self, file_path, file_type):
        try:
            # Check the file type and perform the corresponding action
            if file_type == 'json':
                # Open the JSON file and load the data
                with open(file_path, 'r') as file:
                    users = json.load(file)
                    # Iterate over the users and create each one in the database
                    for user in users:
                        # Set the default values for the user (created_dt and modified_dt)
                        user = set_default_values(user)
                        # Create the user in the database
                        self.create_user(User(**user))
            elif file_type == 'csv':
                # Import the csv_to_json function from the utils module
                from utils.csv_to_json import csv_to_json
                # Convert the CSV file to JSON data
                users = csv_to_json(file_path)
                # Iterate over the users and create each one in the database
                for user in users:
                    # Set the default values for the user (created_dt and modified_dt)
                    user = set_default_values(user)
                    # Create the user in the database
                    self.create_user(User(**user))
        except Exception as err:
            # Log any errors that occur during the execution
            self.logger.error(f"Failed to bulk insert users: {err}")

    # Method to retrieve all users from the database
    def get_users_from_db(self):
        # Get a cursor object from the DBConnection
        cursor = self.db_connection.get_cursor()
        if cursor:
            try:
                # Define the SQL query to select all users
                query = ("SELECT * FROM users")
                # Execute the SQL query
                cursor.execute(query)
                # Fetch all the rows from the query
                users = cursor.fetchall()
                # Return the list of users
                return users
            except mysql.connector.Error as err:
                # Log any errors that occur during the execution
                self.logger.error(f"Failed to get users from db: {err}")
                # Return an empty list to indicate failure
                return []
            finally:
                # Close the cursor object
                cursor.close()

   # Method to generate a reconciliation report
def generate_reconciliation_report(self, file_path, file_type):
    try:
        # Check the file type and perform the corresponding action
        if file_type == 'json':
            # Open the JSON file and load the data
            with open(file_path, 'r') as file:
                users = json.load(file)
                # Retrieve all users from the database
                db_users = self.get_users_from_db()
                # Compare the users and generate a report
                report = self.compare_users(users, db_users)
                # Return the report
                return report
        elif file_type == 'csv':
            # Import the csv_to_json function from the utils module
            from utils.csv_to_json import csv_to_json
            # Convert the CSV file to JSON data
            users = csv_to_json(file_path)
            # Retrieve all users from the database
            db_users = self.get_users_from_db()
            # Compare the users and generate a report
            report = self.compare_users(users, db_users)
            # Return the report
            return report
    except Exception as err:
        # Log any errors that occur during the execution
        self.logger.error(f"Failed to generate reconciliation report: {err}")

# Method to compare users and generate a report
def compare_users(self, users, db_users):
    report = []
    # Iterate over the users and compare with the database users
    for user in users:
        found = False
        for db_user in db_users:
            if user['user_id'] == db_user[0]:
                found = True
                break
        if not found:
            # If the user is not found, add it to the report
            report.append(f"User {user['user_id']} not found in db")
    return report