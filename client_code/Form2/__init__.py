from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_pass.hide_text = not self.text_box_1.hide_text

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  def signup_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    email = self.text_box_email.text
    password = self.text_box_pass.text
    anvil.server.call('create_account', email, password)
