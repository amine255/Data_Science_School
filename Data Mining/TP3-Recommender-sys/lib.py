# coding: utf-8
import numpy as np

def import_data_tain_test(train_db, test_db):
    # u.data  user id | item id | rating | timestamp.
    data_train = np.loadtxt(train_db)
    data_test = np.loadtxt(test_db)
    return data_train, data_test


def bias_calculus(data):
    print "okokok"
    maxs = data.max(0)  # extraction des nb d'utilisateurs et d'item
    nu = maxs[0] + 1
    ni = maxs[1] + 1
    user_bias = np.zeros(nu)
    item_bias = np.zeros(ni)
    user_count = np.zeros(nu)
    item_count = np.zeros(ni)
    # systeme basique: plus simple de travailler sur les triplets
    for iteration in xrange(len(data)):
        u = data[iteration, 0]
        i = data[iteration, 1]
        r = data[iteration, 2]
        user_bias[u] += r
        item_bias[i] += r
        user_count[u] += 1
        item_count[i] += 1
    
    # ATTENTION AUX DIVISIONS PAR 0 !!
    user_bias /= np.where(user_count == 0, 1, user_count)
    item_bias /= np.where(item_count == 0, 1, item_count)
    print u"user and item biases computed."    


    return user_bias,item_bias
	


