from kivy.logger import Logger
from widget import FoodItem
from widget import FoodItemList
import operator
class LayoutCreator(object):
  
  def createListForJson(self, webResult):
    webResult = sorted(webResult, key = operator.itemgetter('votes', "name"), reverse = True)
    layout = FoodItemList(orientation="vertical", canvas_size=(200,200))
    index = 0
    for item in webResult:
      widget = FoodItem(item, index)
      index += 1
      Logger.info(widget.__str__())
     # layout.add_widget(Button(text="Item "+str(item['id'])))
      layout.add_widget(widget)
    return layout
    