import sqlite3 as sql

from pathlib import Path
from logging import info, debug

__sql_create_order_table = 'CREATE TABLE IF NOT EXISTS service_orders (so INTEGER UNIQUE, customer TEXT NOT NULL, title TEXT NOT NULL, status INT NOT NULL, start_date LONG, end_date LONG, time_spend INT)'
__sql_create_entry_table = 'CREATE TABLE IF NOT EXISTS entry(so INTEGER NOT NULL, entry_id INT NOT NULL, start_date LONG NOT NULL, end_date LONG NOT NULL, data TEXT)'
__sql_insert_order = 'INSERT INTO service_orders VALUES(?, ?, ?, ?, ?, ?, ?)'
__sql_insert_entry = 'INSERT INTO entry VALUES(?, ?, ?, ?, ?)'

__sql_select_all_entries = 'SELECT * FROM entry'
__sql_select_all_orders = 'SELECT * FROM service_orders'

__sql_select_by_so = 'SELECT * FROM entry WHERE so=:so'

__sql_con = None
__sql_cur = None

def init(path: Path):
  global __sql_con
  global __sql_cur

  if(path.exists() == False):
    info('database not found, creating empty database...')
    path.touch()

  __sql_con = sql.connect(path)
  __sql_cur = __sql_con.cursor()

  __sql_cur.execute(__sql_create_order_table)
  __sql_cur.execute(__sql_create_entry_table)
  if __sql_con is not None and __sql_cur is not None:
    return __sql_cur
  return None

def insert_order(data: tuple):
  debug(f'executing {__sql_insert_order} : {data}')
  __sql_cur.execute(__sql_insert_order, data)

def insert_entry(data: tuple):
  debug(f'executing {__sql_insert_entry} : {data}')
  __sql_cur.execute(__sql_insert_entry, data)

def commit():
  debug('committing data...')
  __sql_con.commit()

def get_all_entries():
  return __sql_cur.execute(__sql_select_all_entries)

def get_all_orders():
  return __sql_cur.execute(__sql_select_all_orders)

def get_all_by_so(so: int):
  return __sql_cur.execute(__sql_select_by_so, {'so': so})

def close():
  debug('closing database...')
  __sql_con.close()
