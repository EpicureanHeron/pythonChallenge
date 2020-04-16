import urllib.request
import re

def linkedlist():
    
    counter = 0
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    number = '12345'

    while counter < 400:
        counter += 1
        query = '%s%s' % (url, number)
        response  = urllib.request.urlopen(query)
        html = str(response.read())
        print(html)
        pattern = re.compile(r'\d{1,10}')
        mo = pattern.search(html)
        
        number = mo.group()

    
linkedlist()