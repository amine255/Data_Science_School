
# coding: utf-8

## TP1 - SENTENCE CLASSIFICATION

# In[4]:
import numpy as np
import gensim      
from gensim import corpora
from tools import *
import os.path
import sklearn.feature_extraction.text as txtTools #.TfidfTransformes
import codecs
import re


def get_parse_data(path):  
    nblignes = compteLignes(path)
    print "nblignes = %d"%nblignes

    alltxts = []
    labs = np.ones(nblignes)
    s=codecs.open(path, 'r','utf-8') # pour régler le codage
    #s=codecs.open(path, 'r','ascii') # pour régler le codage
    
    cpt = 0
    for i in range(nblignes):
        txt = s.readline()
        #print txt

        lab = re.sub(r"<[0-9]*:[0-9]*:(.)>.*","\\1",txt)
        txt = re.sub(r"<[0-9]*:[0-9]*:.>(.*)","\\1",txt)
        #print txt
        #assert(lab == "C" or lab == "M")

        if lab.count('M') >0:
            labs[cpt] = -1
        alltxts.append(txt)

        cpt += 1
    return alltxts,labs



def create_dictionary(alltxts,labs):
    print "Creating Bag of Words..."  
    
    
#    stoplist = set(u'le du qu on la a dans les de des à un une est en au ne ce d l c s je tu il que qui mais quand et pas pour vous nous'.split())
    stoplist = set(u'de_la,la_france,c_est,de_l'.split(","))
#    stoplist = set(''.split())
#    stoplist = set('le la les de des à un une en au ne ce d l c s je tu il que qui mais quand'.split())
#    stoplist = set(' '.split())
    stoplist.add(u' ')
    
    ## DICO
    splitters = u'; |, |\*|\. | |\'|'
    
##     remplacement de la ligne:
#    dictionary = corpora.Dictionary(re.split(splitters, doc.lower()) for doc in alltxts)
#
    liste = (re.split(splitters, doc.lower()) for doc in alltxts) # generator = pas de place en memoire
    dictionary = corpora.Dictionary([u"{0}_{1}".format(l[i],l[i+1]) for i in xrange(len(l)-1)] for l in liste) # bigrams

    
    print len(dictionary)

    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist   if stopword in dictionary.token2id]
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq < 2]
    dictionary.filter_tokens(stop_ids+once_ids) # remove stop words and words that appear only once
    dictionary.compactify() # remove gaps in id sequence after words that were removed

    print len(dictionary)

    return stoplist,splitters,dictionary


def create_corpus(stoplist,splitters,dictionary,alltxts):
    
#    texts = [[word for word in re.split(splitters, document.lower()) if word not in stoplist]  for document in alltxts]
#    
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


def get_parse_data_test(path):  
    nblignes = compteLignes(path)
    print "nblignes = %d"%nblignes

    alltxts = []
    labs = np.ones(nblignes)
    s=codecs.open(path, 'r','utf-8') # pour régler le codage
    #s=codecs.open(path, 'r','iso-8859-1') # pour régler le codage

    cpt = 0
    for i in range(nblignes):
        txt = s.readline()
   
        txt = re.sub(r"<[0-9]*:[0-9]*>(.*)","\\1",txt)

        alltxts.append(txt)

        cpt += 1
    return alltxts



#IMPORTING DATA

path_train = "/home/arda/Documents/Data_Science_School/Data Mining/TP1-Sentence_classification/Data/corpus.tache1.learn.utf8"
path_test = "/home/arda/Documents/Data_Science_School/Data Mining/TP1-Sentence_classification/Data/corpus.tache1.test.utf8"

stopwords_path = "/home/arda/Documents/Data_Science_School/Data Mining/TP1-Sentence_classification/stopword/stop-words_french_1_fr.txt"

alltxts_train,labs = get_parse_data(path_train)
alltxts_test= get_parse_data_test(path_test)
#alltxts_test= get_parse_daMEHRANIta(path_test)


stoplist,splitters,dictionary = create_dictionary(alltxts_train,labs)
dataSparse_train,data2_train = create_corpus(stoplist,splitters,dictionary,alltxts_train)

dataSparse_test,data2_test = create_corpus(stoplist,splitters,dictionary,alltxts_test)
print "len(alltxts_test)", len(alltxts_test)


print "dataSparse_train.shape :", dataSparse_train.shape
print "dataSparse_test.shape :", dataSparse_test.shape

print "data2_train.shape :", data2_train.shape
print "data2_test.shape :", data2_test.shape

#dataSparse_train = data2_train
#dataSparse_test = data2_test

#DEFINE CLASSIFIER

from sklearn.naive_bayes import MultinomialNB
from sklearn import svm


#clf = svm.SVC(C=1,kernel='linear',class_weight ='auto')  # definition du classifieur
#clf = svm.LinearSVC(C=1e3) # definition du classifieur
clf = MultinomialNB(alpha=0.4,class_prior=np.array([1,6]))
#clf = MultinomialNB(alpha=0.5)
#clf = linear_model.SGDClassifier( )
print "Training parameters"

clf.fit(dataSparse_train,labs)   # apprentissage


#EVALUATE CROSS VALIDATION

#from sklearn import svm
from sklearn import cross_validation
from sklearn.metrics import f1_score

## usage basique: split train/test
#X_train, X_test, y_train, y_test = cross_validation.train_test_split( dataSparse_train, labs, test_size=0.4, random_state=0)
y_pred = clf.predict(dataSparse_train)
print "F1 predicted score", f1_score(y_pred,labs,pos_label=-1)

scores = cross_validation.cross_val_score( clf, dataSparse_train, labs, cv=5)
scores



#PREDICTION
prediction = clf.predict(dataSparse_test)
#
prediction1 = np.where(prediction==-1,-3,1)

for i in range(5,prediction1.shape[0]-6):
    for k in range(1,5):
        prediction1[i]+= (prediction1[i-k]+prediction1[i+k])/8.0
        
prediction2 = np.where(prediction1<0,-1,1)

prediction = prediction2    


    
#
for i in range(prediction.shape[0]):
    if prediction[i] == prediction[i-2] == -1:
        prediction[i-1]=-1

#        
for i in range(prediction.shape[0]):
    if prediction[i] == prediction[i-3] == -1:
        prediction[i-1]= -1
        prediction[i-2]= -1
#        
#for i in range(prediction.shape[0]):
#    if prediction[i] == prediction[i-3] == 1:
#        prediction[i-1]= 1
#        prediction[i-2]= 1

#        
for i in range(prediction.shape[0]):
    if prediction[i] == prediction[i-2] == 1:
        prediction[i-1]= 1


#WRITING TO TEXTFILE

text_file = open("sentence_prediction.txt", "w")
for i in range(0,prediction.shape[0]):
    if prediction[i] == 1.0:
        text_file.write("C\n")
    else:
        text_file.write("M\n")
            
text_file.close()


#PRINTING RANKING WORDS
important = clf.feature_log_prob_
importance1 = important[0,:]
importance2 = important[1,:]

ranking = np.chararray(((10,2)),10)

for i in range(len(ranking)):
    Mitt = dictionary[importance1.argmax()]
    Chirac = dictionary[importance2.argmax()]
    ranking[i,0] = Mitt
    ranking[i,1] = Chirac

    importance1[importance1.argmax()] = -100
    importance2[importance2.argmax()] = -100
    
print ranking


