import os
import logging

def validate_file_path(file_path):
    logger = logging.getLogger(__name__)
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} not found")
        raise FileNotFoundError(f"File {file_path} not found")
    if not os.path.isfile(file_path):
        logger.error(f"{file_path} is not a file")
        raise ValueError(f"{file_path} is not a file")