import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def set_write_perms(login, perms=False):
  '''
  Assigns a user write permissions by setting write_access flag in "Users" table
  login: email address of the desired user
  perms: database write permissions - defaults to False
  '''
  user = app_tables.users.get(email=login)
  user['write_access'] = perms

@anvil.server.callable
def get_write_perms():
  '''
  Checks the write_access status of the currently logged in user
  Returns True if the user has write permissions
  '''
  current_user = anvil.users.get_user()
  if current_user['write_access']:
    return True
  else:
    return False