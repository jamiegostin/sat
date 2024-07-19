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

    # Hide "log out" button if no user is logged in
    if not anvil.users.get_user():
      self.link_log_out.visible = False
  
  def button_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form(prev_form)

  def link_log_out_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    anvil.open_form('scr_login')

def set_prev_form(form):
  global prev_form
  prev_form = form
