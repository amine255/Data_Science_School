# coding: utf-8

import numpy as np
from scipy.sparse import coo_matrix

def import_data_tain_test(train_db, test_db):
    # u.data  user id | item id | rating | timestamp.
    data_train = np.loadtxt(train_db)
    data_test = np.loadtxt(test_db)
    return data_train, data_test

train_db = "/users/Etu6/3402426/Documents/M2/Data Mining/TP3-recommender-sys/data/ml-100k/u1.base"
test_db = "/users/Etu6/3402426/Documents/M2/Data Mining/TP3-recommender-sys/data/ml-100k/u1.test"



def dunn():
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


def plot_dude():
	plt.figure()
	plt.subplot(211)
	plt.hist(user_bias, 100)
	plt.title('Utilisateur')
	plt.subplot(212)
	plt.hist(item_bias, 100)
	plt.title('Item')
	plt.savefig("recoBias.pdf")


def factorisation():
    # factorisation matricielle: on travaille de nouveau sur les triplets pour minimiser les hypothèses
    # sur les cases vides

    # paramétrage
    random = np.random.RandomState(0)
    epochs = 5  # nb de passage sur la base
    nZ = 10  # taille de l'espace latent
    l1_weight = 0.00  # contraintes de régularization L1 + L2
    l2_weight = 0.0001
    learning_rate = 0.001

    # pour cet exemple, je prends tous les indices en apprentissage...
    train_indexes = np.arange(len(data))

    # initialisation à moitié vide... randn + seuillage > 0
    user_latent = np.random.randn(nu, nZ)
    item_latent = np.random.randn(ni, nZ)
    # profils positifs sparses
    user_latent = np.where(user_latent > 0, user_latent, 0)
    item_latent = np.where(item_latent > 0, item_latent, 0)

    for epoch in xrange(epochs):
        print "epoch : %d" % epoch
        # Update
        random.shuffle(train_indexes)
        for index in train_indexes:
            # extraction des variables => lisibilité
            label, user, item = data[index, 2], data[index, 0], data[index, 1]
            gamma_u, gamma_i = user_latent[user, :], item_latent[item, :]
            # Optimisation
            delta_label = 2 * (label - np.dot(gamma_u, gamma_i))
            gradient_u = l2_weight * gamma_u + \
                l1_weight - delta_label * gamma_i
            gamma_u_prime = gamma_u - learning_rate * gradient_u
            user_latent[user, :] = np.where(
                gamma_u_prime * gamma_u > 0, gamma_u_prime, 0)  # MAJ user
            gradient_i = l2_weight * gamma_i + \
                l1_weight - delta_label * gamma_u
            gamma_i_prime = gamma_i - learning_rate * gradient_i
            item_latent[item, :] = np.where(
                gamma_i_prime * gamma_i > 0, gamma_i_prime, 0)  # MAJ item
