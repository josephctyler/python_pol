# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 21:59:08 2016

@author: Joseph
"""
import nltk

# import and process Hillary's speech
from nltk.tokenize import word_tokenize
f1 = open("/Users/Joseph/Desktop/Professional/Learning/Python/hillary_transcript.txt", encoding="utf-8")
raw1 = f1.read()
tokens1 = word_tokenize(raw1)
ctokens1 = [w.lower() for w in tokens1 if len(w) > 4 and w != "Applause"]
fdist1 = nltk.FreqDist(ctokens1)
hcomm = fdist1.most_common(20)
khcomm = [i[0] for i in hcomm] # a list of the keys

# import and process Trump's speech
f2 = open("/Users/Joseph/Desktop/Professional/Learning/Python/trump_transcript.txt", encoding="utf-8")
raw2 = f2.read()
tokens2 = word_tokenize(raw2)
ctokens2 = [w.lower() for w in tokens2 if len(w) > 4 and w != "APPLAUSE"]
fdist2 = nltk.FreqDist(ctokens2)
tcomm = (fdist2.most_common(20))
ktcomm = [i[0] for i in tcomm] # a list of the keys

# create lists of words they share and are unique to each
hnott = [w for w in set(ctokens1) if w not in ctokens2]
tnoth = [w for w in set(ctokens2) if w not in ctokens1]
both = [w for w in set(ctokens1) if w in ctokens2]

print("\n Top words common to both: \n")
for w in hcomm:
    if w[0] in ktcomm:
        print(w)
        
print("\n Hillary's common words: \n")
for w in hcomm:
    if w[0] not in ktcomm:
        print(w)
        
print("\n Trump's common words: \n")
for w in tcomm:
    if w[0] not in khcomm:
        print(w)