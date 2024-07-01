import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_songs():
  return app_tables.metadata.search()

@anvil.server.callable
def search_songs(query):
  result= app_tables.metadata.search()
  if query.lower():
    result = [
      x for x in result
      if query in x['Title'].lower()
      or query in x['Artist'].lower()
      or query in x['Album'].lower()
      or query in x['Genre'].lower()
      or query in str(x['Year'])
      or query in str(x['BPM'])
    ]
    return result