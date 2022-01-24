import argparse
import logging

parser = argparse.ArgumentParser(description='Ticketing tracker')

parser.add_argument('action', choices=['create','edit', 'delete', 'get', 'entry'], type=str, nargs=1, help='type of action to execute (create, edit, delete, get, entry)')
parser.add_argument('so', type=int, nargs=1, help='service order number')
parser.add_argument('-c', '--company', type=str, nargs=1, help='company name (used when creating new SOs)')
parser.add_argument('-t', '--title', type=str, nargs=1, help='title of the ticket (used when creating new SOs)')
parser.add_argument('-e', '--entry-text', type=str, nargs='+', help='entry data (used when creating a new entry)')

def parse():
  args = parser.parse_args()
  print(args)
  if args.action[0].startswith('create') and (args.company == None or args.title == None):
    logging.error('did not supply correct arguments')
    exit(4)
  return args
