#!/usr/bin/python
# coding: iso-8859-1

import sys
reload(sys)
sys.setdefaultencoding('iso-8859-1')
print sys.getdefaultencoding() 
import os 
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk.data
import string
path = os.path.join(os.path.expanduser('~'), 'Downloads','LAB', 'summaries','docs')


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    numberOfFiles = len(r)
    return r

fnames = list_files(path)
for fname in fnames:
    with open(fname, 'r') as fin:
        badWords = ['From:','Subject:','Lines:','Reply','Organization:','Article-I.D.:','@','Summary:','Keywords:','Expires:',':']
        new_file_name = fname+'NEW';
        with open(fname) as oldFile, open(new_file_name,'w') as newFile:
            for line in oldFile:
            	#line = line.lower()
                Str2='\n'

                if not any(badWord in line for badWord in badWords):

                    line = line.replace('\t',' ')
                    line = line.replace('\n',' ')
                    line = line.translate(None, "@#$%^&*+-()|\<[>],\"_/:'~`")
                    line = re.sub(' +', ' ', line)
                    newFile.write(line)
        newFile.close()


        with open(new_file_name,'r') as newFile:
            line = newFile.read()    

            sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
            Str2 = ('\n-----\n'.join(sent_detector.tokenize(line.strip())))
            Str2 = re.sub(' +', ' ', Str2)
                

            stop_words = set(stopwords.words('english'))
            tokens = nltk.word_tokenize(Str2)
            Str1 = " ".join(filter(lambda word: word not in stop_words, Str2.split()))
            Str1 = re.sub(r'[^\w\s]','',Str1)   
            Str1 = Str1.replace('  ','\n')
            #Str1 = Str1.lower()
            with open(new_file_name,'w') as newFile:
                newFile.write(Str1)
                    
        
