from widget import FoodItemList

class LayoutCreator(object):
  
  def createListForJson(self, webResult):
    layout = FoodItemList(webResult)
    return layout