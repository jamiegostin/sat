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

  def link_logout_click(self, **event_args):
    """Log out the current user and return to login screen"""
    anvil.users.logout()
    open_form('scr_login')

  def filter_table(self, **event_args):
    '''
    Filter repeating panel results according to search textbox term
    '''
    if self.text_box_filter_table.text:
      self.repeating_panel_metadata.items = anvil.server.call(
        'search_songs',
        self.text_box_filter_table.text.lower()
      )
    else:
      # Display all items if blank input is searched
      self.repeating_panel_metadata.items = anvil.server.call('get_songs')

  def btn_new_record_click(self, **event_args):
    '''
    Attempt to create a new record in the database according to text box values
    '''
    # Ensure existence of input
    if self.text_box_new_album.text and self.text_box_new_artist.text and self.text_box_new_song.text and self.text_box_new_tempo.text and self.text_box_new_year.text:

      # Make sure year and tempo inputs are number
      if self.text_box_new_tempo.text.strip().isdigit() and self.text_box_new_year.text.strip().isdigit():

        # Check current user has write perms
        if anvil.server.call('get_write_perms'):

          # Check that a duplicate entry does not already exist
          titles = [r['Title'].lower() for r in anvil.server.call('get_songs')]
          artists = [r['Artist'].lower() for r in anvil.server.call('get_songs')]
          if self.text_box_new_song.text.lower() not in titles and self.text_box_new_artist.text.lower() not in artists:
            
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
  
            alert('New entry was successfully created.')
            self.repeating_panel_metadata.items = anvil.server.call('get_songs')
          else:
            alert('A matching record already exists!')
        else:
          alert('You do not have permission to edit the database.')

        # Clear invalid text boxes
        self.text_box_new_song.text = ''
        self.text_box_new_artist.text = ''
        self.text_box_new_album.text = ''
        self.text_box_new_year.text = ''
        self.text_box_new_tempo.text = ''
        self.drop_down_new_genre.selected_value = 'Alternative'
      else:
        alert('You must enter a valid number for tempo and release year values.')

        # Clear invalid text boxes
        self.text_box_new_tempo.text = ''
        self.text_box_new_year.text = ''
    else:
      alert('Please make sure all boxes are filled.')

  def link_help_click(self, **event_args):
    '''Opens the help screen'''
    set_prev_form('scr_main')
    anvil.open_form('scr_help')

  def sort_change(self, **event_args):
    """This method is called when either of the "sort by" dropdowns are modified"""
    if self.drop_down_ascend.selected_value == 'Ascending':
      ascending = True
    else:
      ascending = False
    
    self.repeating_panel_metadata.items = anvil.server.call('sort_songs', self.drop_down_sort.selected_value, ascending)
