from ._anvil_designer import scr_resultTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
import anvil.media
from ..scr_help import set_prev_form

closest_matches = []

class scr_result(scr_resultTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.lbl_match1.text = "1. " + closest_matches[0][0]
    self.lbl_match2.text = "2. " + closest_matches[1][0]
    self.lbl_match3.text = "3. " + closest_matches[2][0]

    self.lbl_artist1.text = closest_matches[0][1]
    self.lbl_artist2.text = closest_matches[1][1]
    self.lbl_artist3.text = closest_matches[2][1]

    self.lbl_album1.text = closest_matches[0][2] + " (" + str(closest_matches[0][3]) + ")"
    self.lbl_album2.text = closest_matches[1][2] + " (" + str(closest_matches[1][3]) + ")"
    self.lbl_album3.text = closest_matches[2][2] + " (" + str(closest_matches[2][3]) + ")"

  def btn_head_log_out_click(self, **event_args):
    """This method is called when the link is clicked"""
    log_out()

  def btn_head_help_click(self, **event_args):
    """This method is called when the link is clicked"""
    set_prev_form('scr_result')
    anvil.open_form('scr_help')

  def btn_return_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('scr_main')

  def btn_log_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    log_out()

  def create_text_file(self):
    file_name = 'output_songs_' + datetime.today().strftime('%Y-%m-%d') + '.txt'
    file_contents = b""
    for i in range(0, 3):
      file_contents += b'Title: ' + bytes(closest_matches[i][0], 'utf-8') + b'\n'
      file_contents += b'Artist: ' + bytes(closest_matches[i][1], 'utf-8') + b'\n'
      file_contents += b'Album: ' + bytes(closest_matches[i][2], 'utf-8') + b'\n'
      file_contents += b'Year: ' + bytes(str(closest_matches[i][3]), 'utf-8') + b'\n'
      file_contents += b'Tempo: ' + bytes(str(closest_matches[i][4]), 'utf-8') + b'\n'
      file_contents += b'Genre: ' + bytes(closest_matches[i][5], 'utf-8')+ b'\n\n'
    out_file = anvil.BlobMedia('text/plain', file_contents, name=file_name)
    anvil.media.download(out_file)

  def btn_save_file_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.create_text_file()

def log_out():
  anvil.users.logout()
  anvil.open_form('scr_login')