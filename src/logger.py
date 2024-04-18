import logging
import os 
import sys
from datetime import datetime

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_directory = os.path.join(os.getcwd(), 'logs')

os.makedirs(log_directory, exist_ok=True)

file_path = os.path.join(log_directory, log_file)

logging.basicConfig(filename=file_path, format="%(asctime)s***%(lineno)d***%(name)s***%(levelname)s***%(message)s", level=logging.INFO)
