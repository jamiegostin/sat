from ._anvil_designer import scr_mainTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime
from ..scr_help import set_prev_form


class scr_main(scr_mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Initialise the dataset
    self.repeating_panel_metadata.items = anvil.server.call('get_songs')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    open_form('scr_login')

  def filter_table(self, **event_args):
    if self.text_box_filter_table.text:
      self.repeating_panel_metadata.items = anvil.server.call(
        'search_songs',
        self.text_box_filter_table.text
      )
    else:
      alert('Please enter a search term.')

  def btn_new_record_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_new_album.text and self.text_box_new_artist and self.text_box_new_song and self.text_box_new_tempo and self.text_box_new_year:
      if self.text_box_new_tempo.text.strip().isdigit() and self.text_box_new_year.text.strip().isdigit():
        if anvil.server.call('get_write_perms'):
          title = self.text_box_new_song.text
          artist = self.text_box_new_artist.text
          album = self.text_box_new_album.text
          year = int(self.text_box_new_year.text)
          tempo = int(self.text_box_new_tempo.text)
          genre = self.drop_down_new_genre.selected_value
    
          anvil.server.call('add_song',
                          title=title,
                          artist=artist,
                          album=album,
                          year=year,
                          tempo=tempo,
                          genre=genre)
    
          self.repeating_panel_metadata.items = anvil.server.call('get_songs')
        else:
          alert('You do not have permission to edit the database.')
    
        self.text_box_new_song.text = ''
        self.text_box_new_artist.text = ''
        self.text_box_new_album.text = ''
        self.text_box_new_year.text = ''
        self.text_box_new_tempo.text = ''
        self.drop_down_new_genre.selected_value = 'Alternative'
      else:
        alert('You must enter a valid number for tempo and release year values.')
        self.text_box_new_tempo.text = ''
        self.text_box_new_year.text = ''
    else:
      alert('Please make sure all boxes are filled.')

  def link_help_click(self, **event_args):
    """This method is called when the link is clicked"""
    set_prev_form('scr_main')
    anvil.open_form('scr_help')
