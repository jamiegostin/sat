from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import custom_signup.login_flow

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.hide_text = not self.text_box_1.hide_text
    if self.text_box_1.hide_text:
      self.button_1.icon = 'fa:eye-slash'
    else:
      self.button_1.icon = 'fa:eye'

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form2')

  def login_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_username.text == '' or self.text_box_1.text == '':
      alert('You must enter a username and password.')
    else:
      open_form('Form3')

    # Login
    custom_signup.login_flow.login_with_form()

# Update login status
def update_login_status(self):
  