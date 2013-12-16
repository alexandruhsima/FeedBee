from threading import Thread
from kivy.logger import Logger
import json
import urllib2
class WebRequest(Thread):
    api_base = 'http://localhost/'
    result = None
    def __init__(self, url = False, data = False):
      Thread.__init__(self)
      self.url = self.api_base if url == "" or url == False else self.api_base + str(url)
      self.data = data if type(data) != bool else json.dumps({"d":"d"})
    def callback(self, val):
      try:
        jsonResponse = json.loads(val)
      except ValueError:
        # Invalid json!
        Logger.warning("WebRequest: invalid json received, quitting")
        raise
      except:
        raise
      return jsonResponse

    def run(self):
      try:
        req = urllib2.Request(self.url, self.data, {'Content-Type':'application/json'})
        f = urllib2.urlopen(req)
        ret = f.read()
        self.result = self.callback(ret)
        return self.result
      except Exception, e:
        Logger.warning("Warning: " + str(e))
        return False
      else:
        pass
      finally:
        pass
      
      
    
