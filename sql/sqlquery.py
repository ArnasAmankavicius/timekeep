import sqlite3 as sql

from logging import info, debug

# Static Queries
__sql_select_all_entries = 'SELECT * FROM entry'
__sql_select_all_orders = 'SELECT * FROM service_orders'
# ---------

# Dynamic Queries
__sql_select_entries_by_so = 'SELECT * FROM entry WHERE so=:so'
# ---------

__sql_cur = None

def init(cursor):
    global __sql_cur
    __sql_cur = cursor

def get_all_entries():
    return __sql_cur.execute(__sql_select_all_entries)

def get_all_orders():
    return __sql_cur.execute(__sql_select_all_orders)

def get_all_entries_by_so(so: int):
    return __sql_cur.execute(__sql_select_entries_by_so, {'so': so})