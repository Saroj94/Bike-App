import os
import logging 
from logging.handlers import RotatingFileHandler
from pathlib import Path
from datetime import datetime

## dynamically the project root directory path
BASE_DIR = Path(__file__).resolve().parent.parent

## store all the logs in the "log" folder
LOGS_DIR = "logs"

## files should be store in the chronological manner
## Format: YYYY-MM-DD
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
MAX_LOG_SIZE = 5*1024*1024
BACKUP_COUNT = 3

## join the root directory and the log folder to make a complete log folder directory path
log_dir_path = BASE_DIR/LOGS_DIR
## create the log folder, even if parent folder is missing it will create that too
log_dir_path.mkdir(parents=True, exist_ok=True)
## create the log file
log_file_path = log_dir_path/LOG_FILE

def configure_logger():
    "Configure logging with file handler and console handler"

    ## create a custom logger 
    logger = logging.getLogger("BikeApp")
    ## set the logging levels which inculcate
    logger.setLevel(logging.DEBUG)

    ## prevent duplicate logging handlers if it is runs multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    ## define the line number, add the file name to the formatter
    formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(filename)s - %(levelname)s - %(message)s")

    ## create handler that decides where the log messages go 
    file_handler = RotatingFileHandler(log_file_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)


    # strem handler because of continuous logging
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    ## add both handler 
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

## configure and expose the logger objects
configure_logger()

if __name__=="__main__":
    print("Done✅")



