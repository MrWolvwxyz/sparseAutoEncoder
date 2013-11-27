#This is the sentence class we will enter our training data into
import sys
import numpy as math
import scipy as sci
import string

nonalphanum = "~`!@#$%^&*()_'+=-\][|}{;:\"/.,?><\xe3\x81\xaf\xe3\x81\xa0\xe3\x81\x97\xe3\x81\xae\xe3\x82\xb2\xe3\x83\xb3"

class sentence:
    
    #Instantiation function
    def __init__( self, wiki_str ):
        self.words = wiki_str.translate( None, nonalphanum ).split()
        self.words = map( string.lower, self.words )
        self.size = len( self.words )
        print( self.words, self.size )