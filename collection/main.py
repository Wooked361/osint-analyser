#!/usr/bin/env python3

import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

from telegram import TelegramCollector
from collector import CollectionException

try:
    tc = TelegramCollector()
    tc.connect()
    tc.main()
    tc.disconnect()
except CollectionException as err:
    logging.error(f"Collection error: {err}")
    sys.exit(1)
except Exception as err:
    logging.error(f"Unexpected error: {err}")
    sys.exit(1)
