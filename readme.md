# Jobs Data Processor

## Overview
This repository contains a Python application that processes job data from JSON and CSV files, creating users in a MySQL database and generating reconciliation reports.

## Requirements
- Python 3.8+
- MySQL Connector/Python 8.0+
- json
- csv

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/jobs-data-processor.git
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Linux/Mac:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
4. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

Create a `db_config.py` file in the `db` directory with the following format:

```python
DB_CONFIG = {
    'host': 'your_host',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database',
    'raise_on_warnings': True
}
```

## Usage

1. Run the application:
   ```sh
   python main.py
   ```
2. Follow the prompts to select the file type (JSON or CSV) and file path.
3. The application will create users in the database and generate a reconciliation report.

## Troubleshooting

- Check the `error.log` file for any error messages.
- Verify that the database connection settings are correct in `db_config.py`.
- Ensure that the JSON or CSV file is in the correct format and location.

## Contributing

Contributions are welcome! Please submit a pull request with your changes.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for details.
