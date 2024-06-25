from ._anvil_designer import scr_loginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class scr_login(scr_loginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.

  def btn_hide_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_pass.hide_text = not self.text_box_pass.hide_text
    if self.text_box_pass.hide_text:
      self.button_1.icon = 'fa:eye-slash'
    else:
      self.button_1.icon = 'fa:eye'

  def btn_signup_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('scr_signup')

  def btn_login_click(self, **event_args):
    """This method is called when the 'log in' button is clicked"""
    if self.text_box_email.text == '' or self.text_box_pass.text == '':
      alert('You must enter a username and box_password.')
    else:
      email = self.text_box_email.text
      password = self.text_box_pass.text
      remember = self.chk_remember.checked
      try:
        anvil.users.login_with_email(email, password, remember)
        open_form('scr_main')
      except anvil.users.AuthenticationFailed:
        alert('The username or password is incorrect.')
