from ._anvil_designer import scr_signupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class scr_signup(scr_signupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btn_hide_signup_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_pass.hide_text = not self.text_box_1.hide_text

  def btn_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('scr_login')

  def btn_signup_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.text_box_email.text
    password = self.text_box_pass.text
    # anvil.server.call('create_account', email, password)
    anvil.users.signup_with_email(email, password)
