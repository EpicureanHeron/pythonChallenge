import os
import shutil
import re
import urllib.request

def main():

    #mypath = os.path.join(os.getcwd(), 'channel')

    counter = 2
    number = '90052'
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

    while counter < 400:

        if counter%2 == 0:
            print('file')
            filepath = os.path.join(os.getcwd(), 'channel', number+'.txt')
            file_1 = open(filepath, "r+") 
            fileRead = file_1.read()
            pattern = re.compile(r'\d{1,10}')
            print(fileRead)
            mo = pattern.search(fileRead)

            number = mo.group()
            counter +=1

        else:
           # print('url')
            query = '%s%s' % (url, number)
            response  = urllib.request.urlopen(query)
            html = str(response.read())
            print('url')
            print(html)
            pattern = re.compile(r'\d{1,10}')
            mo = pattern.search(html)
        
            number = mo.group()
            counter +=1
    

if __name__ == "__main__":
    main()