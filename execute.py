import argparse
from tools.file_utils import file_exists
from tools.mower_utils import process_mowing
import logging

# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initiate the logger
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="MowItNow Mower Program")
        parser.add_argument("file_path", help="Path to the input file containing mower instructions")
        args = parser.parse_args()
        file_path = args.file_path
        if file_exists(file_path):
            process_mowing(file_path)
        else:
            raise Exception(f"File not found: {file_path}")

    except Exception as e:
        logger.error(e)
