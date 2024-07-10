from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_save_edits_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('edit_song',
                     self.item,
                     title=self.text_box_edit_song.text,
                     artist=self.text_box_edit_artist.text,
                     album=self.text_box_edit_album.text,
                     year=int(self.text_box_edit_year.text),
                     tempo=int(self.text_box_edit_tempo.text),
                     genre = self.drop_down_edit_genre.selected_value)

  def button_compare_song_click(self, **event_args):
    """This method is called when the button is clicked"""
    songs_by_genre = [[
        r['Title'],
        r['Artist'],
        r['Album'],
        r['Year'],
        r['BPM'],
        r['Genre'],
    ]
      for r in anvil.server.call('sort', self.drop_down_edit_genre.selected_value)
    ]
    # DEBUG
    print(sort_by_tempo(songs_by_genre, int(self.text_box_edit_tempo.text)))
    
def sort_by_tempo(array, selected_tempo):
  songs_by_tempo = sorted(array, key=lambda x: abs(x[4] - selected_tempo))
  return songs_by_tempo