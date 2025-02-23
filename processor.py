from services.user_service import UserService
from utils.files import validate_file_path
import logging

# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

def main():
    user_service = UserService()
    file_path = input("Enter the file path: ")
    try:
        validate_file_path(file_path)
        file_type = input("Enter the file type (json/csv): ")
        user_service.bulk_insert_users(file_path, file_type)
        report = user_service.generate_reconciliation_report(file_path, file_type)
        print("Reconciliation Report:")
        for line in report:
            print(line)
    except Exception as err:
        logging.error(f"An error occurred: {err}")

if __name__ == "__main__":
    main()