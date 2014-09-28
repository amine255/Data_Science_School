# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 19:19:52 2014

@author: arda
"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')   


a = 2 # variable contenant la valeur 2
m0 = np.array([[1, 2], [3, 4]])     # matrice
                                    # matrice = vecteur de vecteurs
v1 = np.arange(0, 10, 1) # create a range
                         # arguments: start, stop, step
v1 = np.arange(0, 10)    # with default arg
v2 = np.linspace(0, 10, 15) # avec linspace, le début et la fin SONT inclus
m1 = np.ones((10,2))  # matrice de 1, argument = nuplet avec les dimensions
                      # ATTENTION np.ones(10,2) ne marche pas
m2 = np.ones((5,4))   # matrice de 0
m3 = np.eye(4)        # matrice identité carrée, arg = dimension
m4 = np.random.rand(5,6)  # matrice de nombres aléatoires indépendants, args = dimensions
m5 = np.random.randn(5,6) # tirages selon une gaussienne(mu=0,var=1), args = dimensions

m6 = m5.T          # pour la transposée
m5.transpose();    # ou bien
np.transpose(m5);  # ou bien

i=1
j=10
print 'toto %2d blabla' % i
print 'toto %2d blabla' % j

i=1
j=10.6758765
print 'toto %2d %5.2f blabla' % (i,j) # toto  1 10.68 blabla


from numpy import random
m5 = random.randn(5,6) # tirages selon une gaussienne(mu=0,var=1), args = dimensions



# une matrice d'entier
matInt   = np.zeros((5,6), int) # matrice 5x6 de 0 (entiers)
matBool  = np.zeros((5,6), bool) # matrice 5x6 de False (booléens)
matBool2 = np.ones((5,6), bool) # matrice 5x6 de True (booléens)