import urllib2 as net
import xml.dom.minidom as xDom
class weather:
    api = "http://www.google.com/ig/api?weather="
    stats = {}
    lastError = None
    wData = None
    def __init__(self,location):
        self.api = self.api + location
        self.wData = net.urlopen(self.api).read()
		
		
    def showXML(self):
        print self.wData
		
		
    def parse(self):
        try:
            xData = xDom.parseString(self.wData)
        except:
            lastError = "Unable to parse XML data."
            return False
		
        # Collect data from XML
        current_conditions = xData.getElementsByTagName('current_conditions')[0]
        
        # Child nodes
        conditions = current_conditions.childNodes[0].getAttribute('data')
        temp_f = current_conditions.childNodes[1].getAttribute('data')
        humidity = current_conditions.childNodes[3].getAttribute('data')
        icon = current_conditions.childNodes[4].getAttribute('data')
        wind = current_conditions.childNodes[5].getAttribute('data')
        
        # Build our dictionary
        self.stats = {"current_temp":temp_f,
                      "conditions":conditions,
                      "humidity":humidity,
                      "icon":icon,
                      "wind":wind
                     }
        return True
		
		
	def get_temp(self):
		return self.stats['current_temp']
	
	
	def get_all(self):
		return self.stats