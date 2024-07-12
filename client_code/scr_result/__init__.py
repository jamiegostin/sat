from ._anvil_designer import scr_resultTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import datetime

closest_matches = []

class scr_result(scr_resultTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.lbl_match1.text = closest_matches[0][0]
    self.lbl_match2.text = closest_matches[1][0]
    self.lbl_match3.text = closest_matches[2][0]

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
