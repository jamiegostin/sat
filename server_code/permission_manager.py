import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def set_write_perms(login, perms=False):
  user = app_tables.users.get(email=login)
  user['write_access'] = perms

@anvil.server.callable
def get_write_perms():
  current_user = anvil.users.get_user()
  if current_user['write_access']:
    return True
  else:
    return False