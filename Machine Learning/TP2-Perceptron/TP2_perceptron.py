
# coding: utf-8

# TP2 : Programmation du Perceptron
# =======
# 
# Dans ce TP, nous allons principalement programmer un perceptron, et mettre en place une "architecture" de code nous permettant petit à petit d'implémenter des Deep Neural Networks. 

# In[1]:

import numpy as np
import pandas as pd


# Etape 1: Dataset
# ------
# 
# La première étape consiste à définir une classe permettant de stocker les données d'apprentissage, de validation et de test. Nous considérerons que les données tiennent en mémoire. Nous allons définir une classe permettant de stocker des couples $\{(x_1,y_1),...,(x_n,y_n)\}$. Les $x_i$ et $y_i$ seront des tableaux numpy 

# In[2]:

class LabeledSet:
    
    def __init__(self,x,y,input_dim,output_dim):
        self.x = x
        self.y = y 
        self.input_dim = x.shape
        self.output_dim = y.shape
        
    #Renvoie la dimension de l'espace d'entrée
    def getInputDimension(self):
        return self.input_dim
        
    #Renvoie la dimension de l'espace de sortie
    def getOutputDimension(self):
        return self.output_dim
        
    #Renvoie le nombre d'exemple dans le set
    def size(self):
        return self.x.size
    #Renvoie la valeur de x_i
    def getX(self,i):
        return self.x[i]
    
    #Renvouie la valeur de y_i
    def getY(self,i):
       return self.y[i]

        


# Nous allons pour l'instant nous intéresser à des datasets "jouet" généres selon des distributions choisies à la main. Commençons par un dataset en 2 dimensions (entrée) et 1 dimension (sortie): $x_i \in \mathbb{R}^2$, $y_i \in [-1;+1]$ telle que les données sont généres selon deux Gaussiennes. Pour cela, nous utiliserons la fonction numpy.random.multivariate_normal  - http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html -  ainsi que la méthode numpy.vstack  - http://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html - pour concaterner des vecteurs 

# In[3]:

def createGaussianDataset(positive_center_1,positive_center_2,positive_sigma,negative_center_1,negative_center_2,negative_sigma,nb_points):
    #Center of the two gaussian distribution
    mean1 = np.array([positive_center_1,positive_center_2])
    mean2 = np.array([negative_center_1,negative_center_2])
     
    #Covariance matrix of the two gaussian distribution
    cov1 = positive_sigma*np.eye(mean1.shape[0])
    cov2 = negative_sigma*np.eye(mean2.shape[0])
           
    #Generating gaussian data1 with corresponding label1 
    data1 = np.random.multivariate_normal(mean1,cov1,nb_points)
    label1 = np.ones((data1.shape[0],1))
        
    #Generating gaussian data2 with corresponding label2
    data2 = np.random.multivariate_normal(mean2,cov2,nb_points)
    label2 = -np.ones((data2.shape[0],1))
        
    x=np.vstack((data1,data2))
    y=np.vstack((label1,label2))
    
    set=LabeledSet(x,y,2,1)
    return set


# Le data set peut être affiché en utilisatn matplotlib (pour vérifier). Nous utiliserons la commande matplotlib.pyplot.scatter permettant de dessiner un nuage de points - http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.scatter -

# In[4]:

import matplotlib.pyplot as plt

def plot2DSet(set):
    plt.scatter(set.x[:,0],set.x[:,1], c=set.y)
    plt.legend()
    plt.show()
    return


# Maintenant, nous allons faire la même chose, mais en dessinant une frontière de décision donnée par une fonction $f : \mathbb{R}^2 \rightarrow \mathbb{R}^1$

# In[5]:

def plot_frontiere(x,f,step=20):
    mmax=x.max(0)
    mmin=x.min(0)
    x1grid,x2grid=np.meshgrid(np.linspace(mmin[0],mmax[0],step),np.linspace(mmin[1],mmax[1],step))
    grid=np.hstack((x1grid.reshape(x1grid.size,1),x2grid.reshape(x2grid.size,1)))
    
    # calcul de la prediction pour chaque point de la grille
    res=np.array([f(grid[i,:])[0] for i in range(len(grid)) ])
    res=res.reshape(x1grid.shape)
    # tracer des frontieres
    plt.contourf(x1grid,x2grid,res,colors=["orange","gray"],levels=[-1000,0,1000],linewidth=2)


def f(x):
    score=[x[0]+x[1]]
    return(score)

#set=createGaussianDataset(1,1,1,-2,-2,1,200)

#plot_frontiere(set.x,f)
#plot2DSet(set)





# Etape 2 : Le Perceptron
# --------

# Nous allons commencer par créer une classe permettant de définir un prédicteur. Basiquement, un prédicteur est une fonction qui prend un vecteur et produit un vecteur, et que l'on peut entrainer sur un "dataset"

# In[6]:

class Predictor:
    def __init__(self):
        raise NotImplementedError("Please Implement this method")

    
    #Permet de calculer la prediction sur x
    def predict(self,x):
        raise NotImplementedError("Please Implement this method")

    
    #Permet d'entrainer le modele
    def train(self,labeledSet):
        raise NotImplementedError("Please Implement this method")
    
    #Permet de calculer la qualité du système (en classification monolabel). ATTENTION, deux cas: outputDimension==1 et outputDimension>1
    def computeMonolabelAccuracy(self,labeledSet):
        prediction_raw = perceptron.predict(labeledSet.x)
        prediction = np.where( prediction_raw  > np.zeros(( labeledSet.x.shape[0],1)),1,-1) 
        
        accuracy = sum(np.where(prediction == labeledSet.y,1,0))*100/labeledSet.y.shape[0]    
        return "The accuracy is: ", accuracy
        
                


# Le premier classifieur à implémenter sera le classifieur perceptron vu en cours

# In[7]:

class Perceptron(Predictor):
    
    def __init__(self,gradient_step,nb_iterations):
        self.learning_rate = gradient_step
        self.nb_iterations = nb_iterations
        
        
        self.theta = 0
        
    def predict(self,x):
        #print theta.shape
        #print x.shape
        return [np.dot(x,self.theta)]
        
            
    def train(self,labeledSet):
              
        label = labeledSet.y
        data = labeledSet.x
        
        self.theta = np.zeros((data.shape[1],1))
        
        eta = self.learning_rate
        n = self.nb_iterations
    

        for i in range(n):
            self.computeMonolabelAccuracy(labeledSet)
            
            t =np.random.choice(data.shape[0])
            x = data[t,:]

            prediction = self.predict(x)
   
            expected = label[t,0]
            ypredit=prediction[0]

            if (ypredit*expected<=0):
                
                learning = eta*expected*x ; #print learning
                learning.shape = ((self.theta.shape[0],1))
                self.theta+=learning
        
        
        
        return self.theta     
     


# On va maintenant tester notre perceptron sur l'ensemble précédent, Visualiser la frontiere de décision obtenus

# In[9]:

#Sans ajout du bias, l'hyperplan est obliger de passer par zero: ax+by = 0

#trainset=createGaussianDataset(1,1,1,4,4,1,500)
#trainset=createGaussianDataset(-2,-2,1,3,3,1,100)
trainset=createGaussianDataset(-2,-2,0.5,1,1,0.5,100)
#plot2DSet(trainset)

perceptron=Perceptron(0.01,100)
theta  = perceptron.train(trainset)


#plot_frontiere(trainset.x,perceptron.predict)
#plot2DSet(trainset)



# In[9]:




# Etape 3 : Tester le Perceptron
# ------
# On va maintenant créer des ensembles de test et de train selon plusieurs distribution et tracer les courbes d'apprentissage (accuraacy) sur train et test dans le temps. Pouvez vous faire apparaitre un effet de sur-apprentissage? 

# In[9]:




# Pouvez vous faire apparaitre un cas ou le perceptron ne peut pas apprendre

# In[9]:




# Etape 4 : Kernel Trick
# -----
# On va transformer nos vecteurs d'entrée de la manière suivante: $(x_1,x_2) \rightarrow $(x_1,x_2,1)$. Apprenez le perceptron sur le nouvel ensemble et visualisez sa frontiere de décision. Que pouvez vous dire ? 

# In[10]:

def kernel_bias(x):
    n = x.shape[0]
    return np.hstack((x ,np.ones((n, 1))  ))
        
def kernel_poly(x):
    output = np.zeros((x.shape[0],6))
    
    output[:,0]=x[:,0]
    output[:,1]=x[:,1]
    output[:,2]=np.ones((x.shape[0]))
    output[:,3]=x[:,0]*x[:,0]
    output[:,4]=x[:,1]*x[:,1]
    output[:,5]=x[:,0]*x[:,1]

    
    return output  


# In[11]:

trainset = createGaussianDataset(4,4,1,9,9,1,200)


#trainset.x = kernel_bias(trainset.x)
trainset.x = kernel_poly(trainset.x)

perceptron = Perceptron(0.001, 600)

perceptron.train(trainset)

#print "ok"

def  plot_frontiere2(x, f, kernel, step=20):
    mmax = x.max(0)
    mmin = x.min(0)
    x1grid , x2grid = np.meshgrid(np.linspace(mmin[0], mmax[0], step),
                                  np.linspace(mmin[1], mmax[1], step))
    grid = np.hstack((x1grid.reshape(x1grid.size, 1),
                      x2grid.reshape(x2grid.size, 1)))
    # calcul de la prediction pour chaque point de la grille
    res = np.array([f(kernel(np.array([grid[i,:]]))[0])[0] for i in range(len(grid))])
    res = res.reshape(x1grid.shape)
    # tracer des frontieres
    plt.contourf(x1grid, x2grid, res,
                 colors=["orange","gray"], levels=[-1000, 0, 1000], linewidth=2)


#plot_frontiere2(trainset.x, perceptron.predict, kernel_poly)
#plot2DSet(trainset)


# In[11]:




# On va transformer nos vecteurs d'entrée de la manière suivante: $(x_1,x_2) \rightarrow $(x_1,x_2,1,x_1*x_1,x_2*x_2,x_1*x_2)$. Apprenez le perceptron sur le nouvel ensemble et visualisez sa frontiere de décision. Que pouvez vous dire ? Pourquoi observe-t-on cette frontière de décision ? 

# In[11]:




# Etape 5 : UCI
# -----
# 
# Plusieurs datasets sont téléchargeables ici:  http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/
# 
# * Implémentez une fonction permettant de les charger
# * Implémnetez une fonction permettant de les "splitter" en train et test
# * Lancer les différentes perceptrons la dessus et tracer les courbes de performance
# 
# (Datasets conseillés: sonar, jeart, breast-cancer et ionosphere)

# In[11]:




# In[ ]:



