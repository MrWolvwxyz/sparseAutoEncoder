import re
import sys

#def main( wiki_str ):

f = open( 'new_text.txt', 'w' )
f2 = open( 'wiki_01.txt', 'r' )
#string = f2.read()
#print string;

for matchedtext in re.findall(r'(?<=[A-Z]).*?(?=[.])', f2.read() ):
    f.write( matchedtext + '\n')
