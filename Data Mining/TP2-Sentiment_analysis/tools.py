# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 23:01:21 2014

@author: arda
"""
import codecs
import re
import numpy as np

def readAFile(nf):
    f = open(nf, 'rb')
    
    txt = f.readlines()
    txt = ' '.join(txt)

    f.close()
    return txt

def compteLignes(nf, fdl='\n', tbuf=16384):
    """Compte le nombre de lignes du fichier nf"""
    c = 0
    f = open(nf, 'rb')
    while True:
        buf = None
        buf = f.read(tbuf)
        if len(buf)==0:
            break
        c += buf.count(fdl)
    f.seek(-1, 2)
    car = f.read(1)
    if car != fdl:
        c += 1
    f.close()
    return c
    
def Data_munging(fname):
    
    nblignes = compteLignes(fname)
    print "nblignes = %d"%nblignes
    
    alltxts = []
    labs = np.ones(nblignes)
    s=codecs.open(fname, 'r','utf-8') # pour régler le codage
    
    cpt = 0
    for i in range(nblignes):
        txt = s.readline()
        #print txt
    
        lab = re.sub(r"<[0-9]*:[0-9]*:(.)>.*","\\1",txt)
        txt = re.sub(r"<[0-9]*:[0-9]*:.>(.*)","\\1",txt)
    
        #assert(lab == "C" or lab == "M")
    
        if lab.count('M') >0:
            labs[cpt] = -1
        alltxts.append(txt)
    
        cpt += 1
        return labs,alltxts 
        
        
def Bow(alltxts): 
    import gensim      
    from gensim import corpora
          
    stoplist = set('le la les de des à un une en au ne ce d l c s je tu il que qui mais quand'.split())
    stoplist.add('')
    
    ## DICO
    splitters = u'; |, |\*|\. | |\'|'
    
    dictionary = corpora.Dictionary(re.split(splitters, doc.lower()) for doc in alltxts)
    
    print len(dictionary)
    
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist   if stopword in dictionary.token2id]
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq < 10 ]
    dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
    dictionary.compactify() # remove gaps in id sequence after words that were removed
    
    print len(dictionary)
    
    ## PROJ
    
    texts = [[word for word in re.split(splitters, document.lower()) if word not in stoplist]  for document in alltxts]
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    ## exemple de doc
    # corpus[0]
    # avec les mots
    print [dictionary[i] for i,tmp in corpus[0]]
    
    # Transformation pour passer en matrice numpy
    dataSparse = gensim.matutils.corpus2csc(corpus)
    return dataSparse
    
def Export2txt(prediction):
    text_file = open("Output.txt", "w")
    for i in range(0,prediction.shape[0]):
        if prediction[i] == 1.0:
            text_file.write("C\n")
        else:
            text_file.write("M\n")
                
    text_file.close()
    
    
    #### tfidf
#import sklearn.feature_extraction.text as txtTools #.TfidfTransformer
#
#t = txtTools.TfidfTransformer()
#t.fit(dataSparse.T)
#data2 = t.transform(dataSparse.T)
    
    