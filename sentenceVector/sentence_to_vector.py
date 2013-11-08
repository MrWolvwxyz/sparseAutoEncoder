import os
import sys

#def produceVec(dictionary)

text = open("helper.txt", 'r')
sentences = text.readlines()

#this is just a temp dictionary for testing, we will use the
#real dictionary for our implementation
testHash = {'I':1, 'am' :2, 'a' :3, 'boy' :4, 'yo' :5 }

#list of list of words
listOfLines = []

#list of list of dictionary indices that correspond to words
listOfLineIndices = []
for line in sentences[0 : ]:
    tempLine = line.split()
    tempLineIndices = []
    for i in tempLine:
        if i in testHash:
            tempLineIndices.append(testHash[i])
        else:
            #-1 indicates that the word is not in the dictionary
            tempLineIndices.append(-1)
    listOfLines.append(tempLine)
    listOfLineIndices.append(tempLineIndices)

print listOfLines
print listOfLineIndices

#return (listOfLines, listOfLineIndices)
#function returns a tuple instead of a struct;
#assign the tuples as follows: mainListOfLines, mainListOfLineIndices = produceVec(dictionary)

#print stringVec[1]
