
# coding: utf-8

# In[1]:

import numpy as np
import gensim      
from gensim import corpora
from tools import *
import os.path
import sklearn.feature_extraction.text as txtTools #.TfidfTransformes
import codecs
import re


# In[1]:




# In[102]:

def get_data_from_folder(path):
    
    alltxts = [] # init vide
    labs = []
    cpt = -1
    for cl in os.listdir(path): # parcours des fichiers d'un répertoire
        print cl
        for f in os.listdir(path+cl):
            txt = readAFile(path+cl+'/'+f)
            alltxts.append(txt)
            labs.append(cpt)

        cpt += 2
    return alltxts, labs



def create_dictionary(alltxts,labs):
    print "Creating Bag of Words..."  
    
    
    
    
#    stoplist = set(u'more,good,much,first,over,--,few,a,able,out,?,even,story,-,character,see,up,:,time,characters,two,\n,",s,(,),movie,!,film,one,t,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'.split(","))
   
    #stoplist = set('one,more,even,time,much,characters,character,really,never,films,scenes,little,way,s,film,t,movie,out,story,good,two,t,up,.,;,\,(,),*,=,&,-,:,--,", ,?,a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your'.split(','))
    #stopwords_path ="/home/arda/Documents/Data_Science_School/Data Mining/TP2-sentiment_analysis/stopwords/"
    #stoplist= get_stopwords(stopwords_path)
    #stoplist = set(u'most,story,first,people,does,way,where,-, ,characters,them,two,see,after,had,make,plot,much,good,life,any,other,if,more,no,only,we,than,time,been,would,!,get,do,also,will,its,than,character,so,or,when,she,their,him,into,just,up,can,even,some,with,he,t,not,they,all,?,there,her,which,like,about,out,ot,what,:,(,),",&,,the,a,and,of,to,is,in,s,as,that,it,i,on,are,his,this,for,on,by,who,hewith,film,but,one,be,an,at,was,have,has,movie,you,from'.split(','))
#    stoplist.add(u'')
    ## DICO
    stoplist = set(u'_,of_the,\n_the,)_,in_the,_but,the_film,,_the,\n_it'.split())
    splitters = u'; |, |\*|\. | |\'|'
   

    # remplacement de la ligne:
    # dictionary = corpora.Dictionary(re.split(splitters, doc.lower()) for doc in alltxts)

    liste = (re.split(splitters, doc.lower()) for doc in alltxts) # generator = pas de place en memoire
    dictionary = corpora.Dictionary([u"{0}_{1}".format(l[i],l[i+1]) for i in xrange(len(l)-1)] for l in liste) # bigrams

    print len(dictionary)

    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist   if stopword in dictionary.token2id]
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq < 3]
    dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
    dictionary.compactify() # remove gaps in id sequence after words that were removed

    print len(dictionary)

    return stoplist,splitters,dictionary


def create_corpus(stoplist,splitters,dictionary,alltxts):
    
#    texts = [[word for word in re.split(splitters, document.lower()) if word not in stoplist]  for document in alltxts]
#    corpus = [dictionary.doc2bow(text) for text in texts]
    
    # projection des documents:
    liste = (re.split(splitters, doc.lower()) for doc in alltxts) # ATTENTION: quand le générator a déjà servi, il ne se remet pas au début => le re-créer pour plus de sécurité 
    alltxtsBig = ([u"{0}_{1}".format(l[i],l[i+1]) for i in xrange(len(l)-1)] for l in liste)
    corpus = [dictionary.doc2bow(text) for text in alltxtsBig]
    


    # Transformation pour passer en matrice numpy
    dataSparse = gensim.matutils.corpus2csc(corpus)
    dataSparse = dataSparse.T

        ### tfidf
    t = txtTools.TfidfTransformer()
    t.fit(dataSparse.T)
    data2 = t.transform(dataSparse.T)
    data2 = data2.T

    return dataSparse,data2
    
    
def get_test_data(path,delimiter):   
    alltxts = [] # init vide
    for cl in os.listdir(path): # parcours des fichiers d'un répertoire
        print cl
        for f in os.listdir(path+cl):
            txt = readAFile(path+cl+'/'+f)
            
            alltxts += txt.split(delimiter)            
    return alltxts



#IMPORTING DATA

path_train = "/home/arda/Documents/Data_Science_School/Data Mining/TP2-sentiment_analysis/data/trainset/"
path_test = "/home/arda/Documents/Data_Science_School/Data Mining/TP2-sentiment_analysis/data/testset/"


alltxts_train,labs = get_data_from_folder(path_train)
alltxts_test= get_test_data(path_test,"\n")


stoplist,splitters,dictionary = create_dictionary(alltxts_train,labs)
dataSparse_train,data2_train = create_corpus(stoplist,splitters,dictionary,alltxts_train)
dataSparse_test,data2_test = create_corpus(stoplist,splitters,dictionary,alltxts_test)



print "dataSparse_train.shape :", dataSparse_train.shape
print "dataSparse_test.shape :", dataSparse_test.shape

print "data2_train.shape :", data2_train.shape
print "data2_test.shape :", data2_test.shape



#DEFINE CLASSIFIER

from sklearn.naive_bayes import MultinomialNB, GaussianNB,BernoulliNB
from sklearn import linear_model
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

#clf = svm.LinearSVC(C=0.0001,class_weight = )  # definition du classifieur
#clf = svm.LinearSVC(C=1,class_weight ='auto' )  # definition du classifieur

clf = MultinomialNB(alpha=4,class_prior=np.array([1,10]))


print "Training parameters"
clf.fit(dataSparse_train,labs)   # apprentissage



#EVALUATE CROSS VALIDATION

#from sklearn import svm
from sklearn import cross_validation

scores = cross_validation.cross_val_score( clf, dataSparse_train, labs, cv=5)
print scores



#PREDICTION
prediction = clf.predict(dataSparse_test)

#WRITING TO TEXTFILE

text_file = open("prediction", "w")
for i in range(0,prediction.shape[0]-1):
    if prediction[i] == -1.0:
        text_file.write("C\n")
    else:
        text_file.write("M\n")
            
text_file.close()




## In[96]:
#
#important = clf.coef_
#
#print important.shape
#print important[0,10]
#ranking = np.chararray( ((100,1)),10 )
#print ranking.shape[0]
#for i in range(important.shape[1]):
#    ranking[i] = dictionary[important.argmax()]
#    important[0,important.argmax()] = 0
#
#
#
## In[87]:
#
#
#
#
## In[56]:
#
important = clf.feature_log_prob_
importance1 = important[0,:]
importance2 = important[1,:]

ranking = np.chararray(((100,2)),10)
for i in range(len(ranking)):
    Mitt = dictionary[importance1.argmax()]
    Chirac = dictionary[importance2.argmax()]
    ranking[i,0] = Mitt
    ranking[i,1] = Chirac

    importance1[importance1.argmax()] = -100
    importance2[importance2.argmax()] = -100
    
print ranking
#
#
## In[143]:
#
#import matplotlib.pyplot as plt
#nombre = clf.feature_count_
#nombre1 = nombre[0,:]
#nombre2 = nombre[1,:]
#
#print nombre1.argmax()
#print nombre2.argmax()
#print dictionary[nombre1.argmax()]
#
#ranking1 = np.chararray(((100,2)),10)
#for i in range(len(ranking1)):
#    Mitt = dictionary[nombre1.argmax()]
#    Chirac = dictionary[nombre2.argmax()]
#    ranking1[i,0] = Mitt
#    ranking1[i,1] = Chirac
#
#    nombre1[nombre1.argmax()] = -100
#    nombre2[nombre2.argmax()] = -100
#
#ranking1
##plt.scatter([1,2,3,4,5],nombre1[0:5])
##plt.show()
#
#
## In[ ]:



