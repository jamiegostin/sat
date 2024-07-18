from ._anvil_designer import scr_helpTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class scr_help(scr_helpTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def button_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form(prev_form)

def set_prev_form(form):
  global prev_form
  prev_form = form
