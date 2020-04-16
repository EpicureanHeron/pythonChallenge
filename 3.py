import urllib.request
import re


response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')

data = str(response.read())

# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides. 

pattern = re.compile(r'[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]')

mo = pattern.findall(data)

print(mo)

clue = ''

for word in mo:
   clue =  clue + word[4] 

print(clue)

