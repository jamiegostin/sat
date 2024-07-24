import anvil.email
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_songs():
  '''Returns all rows from "Metadata" data table'''
  return app_tables.metadata.search()

@anvil.server.callable
def sort_songs(sortby, ascending):
  '''
  Returns all rows, sortd from "Metadata" data table
  sortby: row to sort by (e.g "Album")
  ascending: boolean, sort results in ascending order
  '''
  return app_tables.metadata.search(
    tables.order_by(sortby, ascending=ascending)
  )

@anvil.server.callable
def search_songs(query):
  '''
  Returns all results from "Metadata" data table matching a certain query
  query: search term to filter databse by
  '''
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

@anvil.server.callable
def add_song(title, artist, album, year, tempo, genre):
  '''
  Creates a new row in "Metadata" data table
  title: corresponds to "Title" in data table
  artist: corresponds to Artist" in data table
  album: corresponds to "Album" in data table
  year: corresponds to "Year" in data table
  tempo: corresponds to "BPM" in data table
  genre: corresponds to "Genre" in data table
  '''
  app_tables.metadata.add_row(Title=title, Artist=artist, Album=album, Year=year, BPM=tempo, Genre=genre)

@anvil.server.callable
def edit_song(song, title, artist, album, year, tempo, genre):
  '''
  Edits an existing row in "Metadata" data table
  title: corresponds to "Title" in data table
  artist: corresponds to Artist" in data table
  album: corresponds to "Album" in data table
  year: corresponds to "Year" in data table
  tempo: corresponds to "BPM" in data table
  genre: corresponds to "Genre" in data table
  '''
  song.update(Title=title, Artist=artist, Album=album, Year=year, BPM=tempo, Genre=genre)

@anvil.server.callable
def filter_by_genre(genre):
  '''
  Returns all results from "Metadata" data table from a certain genre
  genre: genre to filter by
  '''
  songs_by_genre = [[
        r['Title'],
        r['Artist'],
        r['Album'],
        r['Year'],
        r['BPM'],
        r['Genre'],
    ]
      for r in app_tables.metadata.search(Genre=genre)
    ]
  return songs_by_genre

@anvil.server.callable
def sort_by_tempo(array, selected_tempo):
  '''
  Returns a sorted list of songs from in order of most similar tempo
  array: the array to sort
  selected_tempo: comparison tempo to sort most similar items
  '''
  songs_by_tempo = sorted(array, key=lambda x: abs(x[4] - selected_tempo))
  return songs_by_tempo