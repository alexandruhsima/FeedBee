from kivy.uix.widget import Widget
from kivy.app import App
from kivy.network.urlrequest import UrlRequest

class kivyApp(App):
    def success(self, event, msg):
        print event
        print msg

    #this version fails the most consistently, the naked urlrequest
    def build(self):
        self.q = UrlRequest("http://localhost/", self.success)
        return Widget()

kivyApp().run()