from kivy.uix.boxlayout import BoxLayout
from kivy.logger import Logger
from FoodItem import FoodItem

class FoodItemList(BoxLayout):
  def __init__(self, webResult):
    super(FoodItemList, self).__init__(orientation='vertical', canvas_size=(200,200))
    for item in webResult:
      widget = FoodItem(item)
      widget.bind(votes=self.votes_changes)
      self.add_widget(widget, widget.votes)
  def votes_changes(self, instance, value):
    print instance 
    print value
    Logger.info('Votes have changed')
      