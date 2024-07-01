from ._anvil_designer import scr_mainTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class scr_main(scr_mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Initialise test dataset
    self.repeating_panel_metadata.items = anvil.server.call('get_songs')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    open_form('scr_login')

  def filter_table(self, **event_args):
    self.repeating_panel_metadata.items = anvil.server.call(
      'search_songs',
      self.text_box_filter_table.text
    )