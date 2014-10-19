
# coding: utf-8

# In[2]:

import numpy as np
import scipy.linalg as lin
import matplotlib.pyplot as plt


# In[151]:




def import_data_tain_test(train_db, test_db):
    # u.data  user id | item id | rating | timestamp.
    data_train = np.loadtxt(train_db)
    data_test = np.loadtxt(test_db)
    return data_train, data_test


def bias_calculus(data):
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


def plot_distribution(user_bias,item_bias):
    
    plt.figure()
    plt.subplot(211)
    plt.hist(user_bias,100)
    plt.title('Utilisateur')    
    plt.subplot(212)
    plt.hist(item_bias,100)
    plt.title('Item')
    plt.savefig("recoBias.pdf")


def matrix_facotisation(data):
    # factorisation matricielle: on travaille de nouveau sur les triplets pour minimiser les hypothèses
    # sur les cases vides
    maxs = data.max(0)  # extraction des nb d'utilisateurs et d'item
    nu = maxs[0] + 1
    ni = maxs[1] + 1

    # paramétrage
    random = np.random.RandomState(0)
    epochs = 5 # nb de passage sur la base
    nZ = 10 # taille de l'espace latent
    l1_weight = 0.00 # contraintes de régularization L1 + L2
    l2_weight = 0.0001
    learning_rate = 0.001

    train_indexes = np.arange(len(data)) # pour cet exemple, je prends tous les indices en apprentissage...

    # initialisation à moitié vide... randn + seuillage > 0
    user_latent = np.random.randn(nu, nZ)
    item_latent = np.random.randn(ni, nZ)
    user_latent = np.where(user_latent > 0, user_latent, 0) # profils positifs sparses
    item_latent = np.where(item_latent > 0, item_latent, 0)

    for epoch in xrange(epochs):
        print "epoch : %d"%epoch
        # Update
        random.shuffle(train_indexes)
        for index in train_indexes:
            # extraction des variables => lisibilité
            label, user, item = data[index,2], data[index,0], data[index,1]
            gamma_u, gamma_i = user_latent[user, :], item_latent[item, :]
            # Optimisation
            delta_label = 2 * (label - np.dot(gamma_u, gamma_i))
            gradient_u = l2_weight * gamma_u + l1_weight - delta_label * gamma_i
            gamma_u_prime = gamma_u - learning_rate * gradient_u
            user_latent[user, :] = np.where(gamma_u_prime * gamma_u > 0, gamma_u_prime, 0) # MAJ user
            gradient_i = l2_weight * gamma_i + l1_weight - delta_label * gamma_u
            gamma_i_prime = gamma_i - learning_rate * gradient_i
            item_latent[item, :] = np.where(gamma_i_prime * gamma_i > 0, gamma_i_prime, 0) # MAJ item
    return user_latent, item_latent


def user_visualisation(user_latent):
    # visualisation des users
    plt.figure()
    plt.imshow(user_latent[:100,:], interpolation="nearest") # 100 premiers utilisateurs
    plt.colorbar()
    #plt.savefig("userLatent.pdf")
    
def item_visualisation(item_latent):
    # visualisation des users
    code,sig,dico = lin.svd(item_latent)
    item2d = code[:,:2] # deux premieres colonnes = 2 premières valeurs singulières (les plus fortes)

    plt.figure()
    plt.scatter(item2d[:,0], item2d[:,1])
    #plt.savefig("itemLatent.pdf")
    
def Sparse(data):
    nu = max(data[:,0]) ; #print "nu :", nu
    ni = max(data[:,1]) ; #print "ni :", ni
    row = data[:,0]
    col = data[:,1] 
    rat = data[:,2]
    A  = coo_matrix((rat,(row,col))).todense()
    return A[1:,1:]


# In[696]:

# import data 
train_db = "/home/arda-mint/Documents/M2/Data Mining/TP3-Recommender-sys/data/u1.base"
test_db = "/home/arda-mint/Documents/M2/Data Mining/TP3-Recommender-sys/data/u1.test"

data = np.loadtxt(train_db)
print data.shape

urs = Sparse(data) ; print "user_row_sparse.shape :", user_row_sparse.shape
irs = urs.T ; print "item_row_sparse.shape :", item_row_sparse.shape





# In[696]:




# In[712]:

ub = np.zeros(urs[:,0].shape)
for i in range(urs.shape[0]):
    one = urs[i,:]                          #getting one user rating vector
    none_zero_length = one[one!=0].shape[1] #retaining only non zero value
    bias = one.sum()/none_zero_length       #getting bias(average) of this vector
    ub[i,0] = bias
    
ib = np.zeros(irs[:,0].shape)

for i in range(irs.shape[0]):
    
    one = irs[i,:]
    none_zero_length = one[one!=0].shape[1]
    #print none_zero_length
    if none_zero_length==0:
        ib[i,0] = 2.5
    else:
        bias = one.sum()/none_zero_length
        ib[i,0] = bias 


# In[682]:

for i in range(ib.shape[0]):
    #print ib[i].shape
    #print i
    #print ib[i]
    if ib[i].shape[0]==0:
        print ib


# In[714]:

ib[710,:]


# In[715]:

print ub.shape
print ib.shape
print urs.shape


# In[275]:

for i in range(urs.shape[0]):
    urs[i,:]= np.where(urs[i,:]==0,ub[i],urs[i,:])
    
for i in range(irs.shape[0]):
    irs[i,:]= np.where(irs[i,:]==0,ib[i],irs[i,:])


# In[705]:

ib[710]


# In[716]:

data_test = np.loadtxt(test_db)

urs_t = Sparse(data_test) ; print "user_row_sparse.shape :", urs_t.shape
irs_t = urs_t.T ; print "item_row_sparse.shape :", irs_t.shape


# In[717]:

MSE = 0
count = 0

for i in range(urs_t.shape[0]):
    temp = urs_t[i,:]
    pos = temp[temp!=0]
    
    length = pos.shape[1]
    
    if length>0:
        diff = ub[i]-pos
        MSE += np.square(diff).sum()/length
        count+=1
print MSE/count


# In[720]:

MSE = 0
count = 0

for i in range(irs_t.shape[0]):
    temp = irs_t[i,:]
    pos = temp[temp!=0]
    
    length = pos.shape[1]
    
    if length>0:
        #print pos
        #print ib[i]
        diff = ib[i]-pos
        MSE += np.square(diff).sum()/length
        count+=1
print MSE/count


# In[582]:




# In[574]:

print ib.shape
print irs_t.shape


# In[632]:

count = 0

for k in range(irs_t.shape[0]):
    temp = irs_t[k,:]
    pos = temp[temp!=0]
    
    length = pos.shape[1]
    #print length
    if length != 0:
        count+=1
print count


# In[644]:

irs_t[1590,:]


# In[ ]:



