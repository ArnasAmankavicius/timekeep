from os import stat
from pathlib import Path
from logging import info
from json import dumps, load

# settings template
settings_template = { 'db_path':f'{Path.home()}/notes.db' }

# load the settings
settings_path = Path(f'{Path.home()}/.tkrc')

def init():
  if(settings_path.exists() == False or settings_path.stat().st_size <= 0):
    info('settings file missing, creating from template...')
    with open(settings_path.absolute(), 'w') as handle:
      handle.write(dumps(settings_template, indent=2)) # too much wrapping, fix
  
  with open(settings_path.absolute(), 'r') as handle:
    info(f'loading settings from {settings_path.absolute()}...')
    settings = load(handle)

  return settings
