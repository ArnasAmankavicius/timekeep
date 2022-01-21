#!/usr/bin/python3

import json
import time
import logging
import sys

from os import stat
from pathlib import Path

import sql.sqlhandler as sqlh 
import sql.sqlquery as sqlquery

from config import init

logging.basicConfig(level=logging.DEBUG)

settings = init()
datetime = time.time()
db_path = Path(settings['db_path'])
cursor = sqlh.init(db_path)

def example():
  # Company Two
  sqlh.insert_order((678901, "Company 1", "Example Title", 1, datetime, None, None))
  sqlh.insert_entry((678901, 1, datetime, datetime + 120, "this is an entry 1"))
  sqlh.insert_entry((678901, 2, datetime + 320, datetime + 640, "this is another entry 2"))
  # Company One
  sqlh.insert_order((123456, "Company 1", "Example Title", 1, datetime, None, None))
  sqlh.insert_entry((123456, 1, datetime, datetime + 120, "this is an entry"))
  sqlh.insert_entry((123456, 2, datetime + 320, datetime + 640, "this is another entry"))

if __name__ == "__main__":
  if(cursor is not None):
    sqlquery.init(cursor)
    logging.debug('database loaded into memory!')
    
    sqlh.close()
  else:
    logging.error('failed to load db into memory. exiting...')
    exit(2)

  logging.debug('execution complete...')
  exit(0)
