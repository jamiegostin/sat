from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...scr_result import closest_matches as results

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_save_edits_click(self, **event_args):
    """Editing database validation"""
    # 1. Check user write perms
    if anvil.server.call('get_write_perms'):
      # 2. Existence check for all text boxes
      if self.text_box_edit_song.text and self.text_box_edit_artist.text and self.text_box_edit_album.text and self.text_box_edit_year.text and self.text_box_edit_tempo.text:
        # 3. Check numeric format of tempo and year text boxes
        if self.text_box_edit_year.text.strip().isdigit() and self.text_box_edit_tempo.text.strip().isdigit():

          # Check for duplicate entries
          titles = [r['Title'].lower() for r in anvil.server.call('get_songs')]
          artists = [r['Artist'].lower() for r in anvil.server.call('get_songs')]
          if self.text_box_edit_song.text.lower() not in titles and self.text_box_edit_artist.text.lower() not in artists:
          
            anvil.server.call('edit_song',
                              self.item,
                              title=self.text_box_edit_song.text,
                              artist=self.text_box_edit_artist.text,
                              album=self.text_box_edit_album.text,
                              year=int(self.text_box_edit_year.text),
                              tempo=int(self.text_box_edit_tempo.text),
                              genre = self.drop_down_edit_genre.selected_value)
            alert('Entry was edited successfully.')
          else:
            alert('A duplicate entry already exists.')
        else:
          alert('You must enter a valid number for tempo and release year values.')
      else:
        alert('Please make sure all boxes are filled.')
    else:
      alert('You do not have permission to edit the database.')
  
  def button_compare_song_click(self, **event_args):
    """This method is called when the button is clicked"""
    filtered = anvil.server.call('filter_by_genre', self.drop_down_edit_genre.selected_value)

    # Clear any pre-existing results and write new matches to list
    results.clear()
    for k in anvil.server.call('sort_by_tempo', filtered, int(self.text_box_edit_tempo.text)):
      if not k[0] == self.text_box_edit_song.text:
        results.append(k)

    anvil.open_form('scr_result')