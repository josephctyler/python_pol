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

# import and process Trump's speech
f2 = open("/Users/Joseph/Desktop/Professional/Learning/Python/trump_transcript.txt", encoding="utf-8")
raw2 = f2.read()
tokens2 = word_tokenize(raw2)
ctokens2 = [w.lower() for w in tokens2 if len(w) > 4 and w != "APPLAUSE"]

# create lists of words they share and are unique to each
hnott = [w for w in set(ctokens1) if w not in ctokens2]
tnotc = [w for w in set(ctokens2) if w not in ctokens1]
both = [w for w in set(ctokens1) if w in ctokens2]

# prompt for word and algorithm to return
inword = input("Choose a word: ").lower()
if inword in both:
    print("Both used it!")
elif inword in hnott:
    print("Hillary only!")
elif inword in tnotc:
    print("Trump only!")
else:
    print("Neither used it!")