from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.app import App
from kivy.logger import Logger
from FeedBeeApp.DataGetter.WebRequest import WebRequest
from FeedBeeApp.Layout.LayoutCreator import LayoutCreator
from kivy.config import Config
from kivy.lang import Builder
import pprint
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), "feedbeekivy.kv"))


class feedBeeKivy(App):
    def on_start(self):
      Logger.info('App: Hello sir!')  
      self.req = WebRequest()
      self.result = self.req.run()
      self.layout = LayoutCreator().createListForJson(self.result) if self.result != False else Label(text="something whent wrong!")
      self.root.content = self.layout
    def build(self):
      Config.set('kivy','desktop',1)
      Config.set('kivy','exit_on_escape',1)
      Config.set('kivy','log_level','info')
      Config.set('graphics','width',"200")
      Config.set('graphics','height',"300")
      Config.set('graphics','fullscreen', 0)
      Config.set('graphics','position', "custom")
      Config.set('graphics','top', 800)
      Config.set('graphics','left', 1700)
      self.root = Popup(title="FeedBee - Food Items", size=(200, 300), size_hint=(None, None))
      return  self.root

feedBeeKivy().run()