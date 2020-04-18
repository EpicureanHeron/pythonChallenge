import pandas as pd
object = pd.read_pickle(r'banner.p')

print(object)

string = ''

for x in object:
    
    for y in x:
        i = 0
        while i < y[1]:
            string+= y[0]
            i+=1
    string += '\n'

print(string)
