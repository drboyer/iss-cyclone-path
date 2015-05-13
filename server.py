from datetime import datetime

import cherrypy

class WebServ(object):
	@cherrypy.expose
	def index(self):
		dt = datetime.now()  # current timestamp
		output = "Sample Webserver test"
		output += dt.strftime('%y-%m-%d %H:%M')
		return output
		
if __name__ == '__main__':
	cherrypy.quickstart(WebServ())