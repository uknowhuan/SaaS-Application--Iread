# coding=utf-8
'''
Created on 2014-12-19

@author: guan
'''
import urlparse
from gevent.pywsgi import WSGIServer
from urls import urls

def application(env, start_response):
    url = env["PATH_INFO"]
    if urls.get(url):
        params = urlparse.parse_qs(env["QUERY_STRING"])
        start_response('200 OK', [('Content-Type', 'text/html')])
        return urls[url](env, params)
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return ['<h1>Not Found</h1>']

if __name__ == '__main__':
    port = 5011
    print 'Initializing...'
    print 'Serving on %s...' % port
    WSGIServer(('', port), application).serve_forever()  #run server
