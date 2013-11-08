import sys
import os

text = open( "word_vectors.txt",'r' )
lines = text.readlines()

num_words = int( lines[ 0 ].split()[ 0 ] )
vec_size = int( lines[ 0 ].split()[ 0 ] )

dicVec = []
word_vectors = []
#hash initialization
dictionary = {}

index = 0
for line in lines[ 1 : ]:
    word = line.split()[0]
    dicVec += [ word ]
    #hashmap that maps word(string) to index(int)(starts from 0)
    dictionary[word] = index

    #word_vectors can be indexed as an array using index[dictionary[word]]
    word_vectors += [ map( float, line.split()[ 1 : ] ) ]
    index = index + 1

dict_sort = sorted( dicVec )
#print( dict_sort )

#if __name__ == '__main__':
#    wordvec_parse()
