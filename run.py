from tests import Tests
from routine import ROUTINE
from colors import Color


def main():

    urlBase = '127.0.0.1'
    port = 8080

    url = None
    for testing in ROUTINE:
        verb = testing.get('verb')
        pathUri = testing.get('path')
        method = testing.get('method')
        headers = testing.get('headers')
        body = testing.get('body')

        test = Tests(urlBase=urlBase, port=port, pathUri=pathUri, method=method, headers=headers, body=body, verb=verb)
        response = test.call()
        #print(response.code)
        #print(response.headers)
        #print(response.reason)
        #print(response.read().decode('utf-8'))
        # self.dictionary = self.response.read().decode('utf-8')
        # return json.loads(self.dictionary)
        if(url == None or url != pathUri+method):
            url = pathUri+method
            print(Color.SUCCESS_BLUE+url+Color.NORMAL)
            
        if(response.code == testing.get('return_code')):
            print(Color.SUCCESS_GREEN+'[OK] '+str(testing.get('return_code'))+' >> '+testing.get('description')+Color.NORMAL)
        else:
            print(Color.FAIL+'[FAIL] '+str(testing.get('return_code'))+' >> '+testing.get('description')+Color.NORMAL)
        #print(response.read().decode('utf-8'))

if(__name__ == '__main__'):
    main()
