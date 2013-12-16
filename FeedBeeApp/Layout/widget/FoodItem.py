from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *
from kivy.lang import Builder
from kivy.logger import Logger
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "foodItem.kv"))
class FoodItem(BoxLayout):
  list_index = NumericProperty()
  item_id = NumericProperty()
  name    = StringProperty()
  votes   = NumericProperty() 
  def __init__(self, item, list_index):
    super(FoodItem, self).__init__()
    self.list_index = list_index
    self.item_id = item["id"]
    self.name    = item["name"]
    self.votes   = item["votes"]
  def up_pressed(self):
    self.votes += 1
  def on_votes(self, instance, value):
    Logger.info("%s has %d votes"%(self.name, self.votes))
    try:
      print self.parent.redraw()
    except Exception, e:
      pass
    else:
      pass
  def __str__(self):
    return str(self.item_id) + " " + self.name
  
  