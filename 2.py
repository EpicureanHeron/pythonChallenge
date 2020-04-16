import collections

file_1 = open("2.txt", "r+") 

fileRead = file_1.read()

print collections.Counter(fileRead)

    