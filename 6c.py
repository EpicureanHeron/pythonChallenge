import os
import shutil
import re
import urllib.request
import collections
import numpy as np
import pandas as pd

def main():

    followNumbers()


def followNumbers():

    counter = 2
    number = '90052'
    commentsString = ''
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    continueLoop = True
    arrayTxt = []
    arrayUrl = []

    
    while continueLoop == True:
        # adds number to txt side 
        arrayTxt.append(number)
                #results = collections.Counter(fileRead)
        # gets number from URL side 
        query = '%s%s' % (url, number)
        response  = urllib.request.urlopen(query)
        html = str(response.read())
        pattern = re.compile(r'\d{1,10}')
        mo2 = pattern.search(html)
        number2 = mo2.group()
        # adds number to URL array 
        arrayUrl.append(number2)
        print('url number %s and text number %s' % (str(number), str(number2)))
        # arrayTxt.append(number)

        # tries to see if the number exists in the channel zip file and opens it
        # if it exists, it gets that number and the loop continues, if ti doesn't, the loop breaks
        filepath = os.path.join(os.getcwd(), 'channel', number+'.txt')
        file_1 = open(filepath, "r+") 
        fileRead = file_1.read()
        pattern = re.compile(r'\d{1,10}')

        mo = pattern.search(fileRead)
        try:
            number = mo.group()
           
        except:
            break

        
      
        


    
    npurl = np.array(arrayUrl)
    nptxt = np.array(arrayTxt)

    npzip =  np.array(list(zip(nptxt,npurl)))

    print(npzip)

    pd.DataFrame(npzip).to_csv("zippedArrays.csv")

if __name__ == "__main__":
    main()
