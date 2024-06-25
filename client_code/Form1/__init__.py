from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_pass.hide_text = not self.text_box_pass.hide_text
    if self.text_box_pass.hide_text:
      self.button_1.icon = 'fa:eye-slash'
    else:
      self.button_1.icon = 'fa:eye'

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form2')

  def login_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_email.text == '' or self.text_box_box_pass.text == '':
      alert('You must enter a username and box_password.')
    else:
      email = self.text_box_email.text
    box_password = self.text_box_box_pass.text
    remember = self.check_box_remember
    try:
      anvil.users.login_with_email(email, box_password, remember)
      open_form('Form3')
    except anvil.users.AuthenticationFailed:
      alert('The username or box_password is incorrect.')