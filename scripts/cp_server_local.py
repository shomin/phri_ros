#!/usr/bin/env python
import os.path
import cherrypy

current_dir = os.path.dirname(os.path.abspath(__file__))

cherrypy.config.update({'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080})

conf = {'/': {'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(current_dir,'html')}}

class Root:
    @cherrypy.expose
    def index(self):
            raise cherrypy.HTTPRedirect("phri_web_local.html")
            #return open('html/test.html')

cherrypy.quickstart(Root(), '/', config=conf)
