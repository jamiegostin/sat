from ._anvil_designer import scr_signupTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..scr_help import set_prev_form

class scr_signup(scr_signupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def btn_hide_signup_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_pass.hide_text = not self.text_box_pass.hide_text
    if self.text_box_pass.hide_text:
      self.btn_hide_signup.icon = 'fa:eye-slash'
    else:
      self.btn_hide_signup.icon = 'fa:eye'

  def btn_back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('scr_login')

  def btn_signup_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_email.text == '' or self.text_box_pass.text == '':
      alert('You must enter an email and password.')
    else:
      if not self.radio_class_artist.selected and not self.radio_class_user.selected:
        alert('You must select a user type.')
      else:
        email = self.text_box_email.text
        password = self.text_box_pass.text
    
        # Attempt to create account with provided details if not exists
        try:
          anvil.users.signup_with_email(email, password)
    
          # Set user write permissions
          anvil.server.call('set_write_perms', email, self.radio_class_artist.selected)
          
          alert('Thank you for signing up! Please check your email for a confirmation link.')
          open_form('scr_login')
        
        except anvil.users.UserExists:
          alert('The email is already in use!')

  def radio_class_user_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def radio_class_artist_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

  def link_help_click(self, **event_args):
    """This method is called when the link is clicked"""
    set_prev_form('scr_signup')
    anvil.open_form('scr_help')
