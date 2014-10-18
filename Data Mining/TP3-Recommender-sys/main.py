# coding: utf-8

import numpy as np
from lib import bias_calculus

# import data 
train_db = "/home/arda-mint/Documents/M2/Data Mining/TP3-Recommender-sys/data/u1.base"
test_db = "/home/arda-mint/Documents/M2/Data Mining/TP3-Recommender-sys/data/u1.test"

data = np.loadtxt(train_db)
# train_db,test_db = import_data_tain_test(train_db, test_db)
print data.shape


user_bias,item_bias = bias_calculus(data)

print item_bias.shape
print user_bias.shape


