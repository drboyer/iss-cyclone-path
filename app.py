import os
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
	cherrypy.config.update({'server.socket_host': '0.0.0.0',})
	cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
	cherrypy.quickstart(WebServ())