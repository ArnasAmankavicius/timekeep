#!/usr/bin/python3
import json
import time
import logging

from pathlib import Path

import sql.sqlhandler as sqlh 
import sql.sqlquery as sqlquery
import parser

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

    args = parser.parse()
    if args.action[0].startswith('create'):
      sqlh.insert_order((args.so[0], args.company[0], args.title[0], 1, datetime, None, None))

    if args.action[0].startswith('get'):
      print(sqlquery.get_specific_so(args.so[0]))
      entries = sqlquery.get_all_entries_by_so(args.so[0])
      for entry in entries:
        print(entry)

    if args.action[0].startswith('entry'):
      sqlh.insert_entry((args.so[0], 1, datetime, datetime + 120, args.entry_text[0]))

    sqlh.commit()
    sqlh.close()
  else:
    logging.error('failed to load db into memory. exiting...')
    exit(2)

  logging.debug('execution complete...')
  exit(0)
