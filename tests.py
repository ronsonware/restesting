import http.client
import json

class Tests(object):

    # constructor
    def __init__(self, **kwargs):
        # Enables builder request settings
        self.urlBase = kwargs.get('urlBase', '')
        self.pathUri = kwargs.get('pathUri', '')
        self.method = kwargs.get('method', '')
        self.headers = kwargs.get('headers', {})
        self.body = json.dumps(kwargs.get('body', {}))
        self.verb = kwargs.get('verb', 'POST')
        self.timeout = int(kwargs.get('timeout', 10))
        self.port = int(kwargs.get('port', 80))
        self.https = kwargs.get('https', False)


    # Treats the arguments passed to the class
    def inputFilter(self, kwargs):
        # Treats urlBase var
        urlBase = kwargs.get('urlBase', '')
        if(urlBase != ''):  self.urlBase = urlBase
        # Treats pathUri var
        pathUri = kwargs.get('pathUri', '')
        if(pathUri != ''):  self.pathUri = pathUri
        # Treats method var
        method = kwargs.get('method', '')
        if(method != ''):  self.method = method
        # Treats headers var
        headers = kwargs.get('headers', {})
        if(headers != {}):  self.headers = headers
        # Treats body var
        body = json.dumps(kwargs.get('body', {}))
        if(body != {}):  self.body = body
        # Treats body var
        verb = kwargs.get('verb', '')
        if(verb != ''):  self.verb = verb
        # Treats timeout var
        timeout = int(kwargs.get('timeout', -1))
        if(timeout != -1):  self.timeout = timeout
        # Treats port var
        port = int(kwargs.get('port', -1))
        if(port != -1):  self.port = port
        # Treats https var
        https = kwargs.get('https', False)
        if(https != False):  self.https = https


    # Make request
    def call(self, **kwargs):
        # Call input filter method
        self.inputFilter(kwargs)

        if(self.https):
            self.connection = http.client.HTTPSConnection(self.urlBase, self.port, self.timeout)
        else:
            self.connection = http.client.HTTPConnection(self.urlBase, self.port, self.timeout)
        self.connection.request(self.verb, self.pathUri+'/'+self.method, self.body, self.headers)
        return self.connection.getresponse()
