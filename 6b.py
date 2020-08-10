import os
import shutil
import re
import urllib.request
import collections

def main():

    followNumbers()


def followNumbers():

    counter = 2
    number = '90052'
    commentsString = ''
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    continueLoop = True

    while continueLoop == True:
        print(number)
        filepath = os.path.join(os.getcwd(), 'channel', number+'.txt')
        file_1 = open(filepath, "r+") 
        fileRead = file_1.read()
        pattern = re.compile(r'\d{1,10}')
        #pattern2 = re.compile(r'^[a-zA-Z]+$')
       # commentsString += fileRead.lower()
        print(fileRead)
        #results = collections.Counter(commentsString)
      #  print(results)

        print(number)

        mo = pattern.search(fileRead)
        number = mo.group()
        counter +=1
        #results = collections.Counter(fileRead)
       # print(results)
        query = '%s%s' % (url, number)
        response  = urllib.request.urlopen(query)
        html = str(response.read())
        print(html)
        print(number)
        # pattern = re.compile(r'\d{1,10}')
        # mo = pattern.search(html)
        
        # number = mo.group()

if __name__ == "__main__":
    main()
