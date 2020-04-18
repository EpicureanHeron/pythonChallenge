import os
import shutil
import re
import urllib.request
import collections

def main():

    #followNumbers()

    # readMe()
    # all()
    justComments()

def justComments():
    filepath = os.path.join(os.getcwd(), 'channel')
    commentList = ['readme.txt', '46145.txt']
    commentsString = ''

    for file in commentList:
        file_1 = open(os.path.join(os.getcwd(), 'channel', file), "r+") 
        fileRead = file_1.read()
        pattern = re.compile(r'\d{1,10}')
        #pattern2 = re.compile(r'^[a-zA-Z]+$')
        commentsString += fileRead.lower()
        print(fileRead)

    results = collections.Counter(commentsString)

   # print(list(results.elements()))

    print(list(results.most_common()))



def all():

    filepath = os.path.join(os.getcwd(), 'channel')
    onlyfiles = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))]
    commentsString = ''

    for file in onlyfiles:
       
        file_1 = open(os.path.join(os.getcwd(), 'channel', file), "r+") 
        fileRead = file_1.read()
        commentsString += fileRead.lower()
        print(fileRead)

    print(collections.Counter(commentsString))


def followNumbers():

    counter = 2
    number = '90052'
    commentsString = ''

    continueLoop = True

    while continueLoop == True:

        filepath = os.path.join(os.getcwd(), 'channel', number+'.txt')
        file_1 = open(filepath, "r+") 
        fileRead = file_1.read()
        pattern = re.compile(r'\d{1,10}')
        #pattern2 = re.compile(r'^[a-zA-Z]+$')
        commentsString += fileRead.lower()
        print(fileRead)
             
        results = collections.Counter(commentsString)
        print(results)

        mo = pattern.search(fileRead)
        #mo2 = pattern2.search(fileRead)
        #print(mo.group())
       # print(mo2.group())

        number = mo.group()
        counter +=1

        # collect the comments
            

        #results = collections.Counter(fileRead)
       # print(results)

def readMe():
    filepath = os.path.join(os.getcwd(), 'channel','readme'+'.txt')
    file_1 = open(filepath, "r+") 
    fileRead = file_1.read()
    results = collections.Counter(fileRead)

    print(results)


if __name__ == "__main__":
    main()
