from kivy.network.urlrequest import UrlRequest

class DataGetter(object):
  def __init__ (self):
    pass
  def getInfo(self):
    self.req = UrlRequest('http://localhost/index.php', self.print_r) 
    try:
      self.req.run()
    except Exception, e:
      print e
    else:
      pass
    finally:
      pass
    
    
  def print_r(self, req, result):
    print "here I am"
    print result
  
    
  