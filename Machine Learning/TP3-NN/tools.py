
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt


# In[2]:

class Loss:
    
    #Calcule la valeur du loss étant données les valeurs prédites et désirées
    def getLossValue(self,predicted_output,desired_output):
        pass
    
    #Calcule le gradient (pour chaque celllule d'entrée) du coût
    def backward(self, predicted_output,desired_output):
        pass 


# In[3]:

class SquareLoss(Loss):
    
    def getLossValue(self,predicted_output,desired_output):
        y_pred = predicted_output
        y = desired_output
        
        return sum( np.square(y_pred-y) )
          
    def backward(self, predicted_output,desired_output):
        y_pred = predicted_output
        y = desired_output
        delta_out = 2*(y_pred-y)/y.shape[0]
        return delta_out


# In[4]:

class HingeLoss(Loss): #L = max(0,-y_pred*y)

    def getLossValue(self,predicted_output,desired_output):
        y_pred = predicted_output
        y = desired_output
        loss = sum(np.where(y_pred*y >= 0,0,-y_pred*y))
        return loss
          
    def backward(self, predicted_output,desired_output):
        y_pred = predicted_output
        y = desired_output
        delta_out = np.where(y_pred*y > 0,0,-y)/y.shape[0]
        return delta_out


# In[5]:

class Module:
    
    #Permet le calcul de la sortie du module
    def forward(self,input):
        pass
    
    #Permet le calcul du gradient des cellules d'entrée
    def backward_delta(self,input,delta_module_suivant):
        pass
    
    #Permet d'initialiser le gradient du module
    def init_gradient(self):
        pass
    
    #Permet la mise à jour des parmaètres du module avcec la valeur courante di gradient
    def update_parameters(self,gradient_step):
        pass
    
    #Permet de mettre à jour la valeur courante du gradient par addition
    def backward_update_gradient(self,input,delta_module_suivant):
        pass
    
    #Permet de faire les deux backwar simultanément
    def backward(self,input,delta_module_suivant):
        self.backward_update_gradient(input,delta_module_suivant)
        return self.backward_delta(input,delta_module_suivant)

    #Retourne les paramètres du module
    def get_parameters(self):
        pass
    
    #Initialize aléatoirement les paramètres du module
    def randomize_parameters(self, variance):
        pass
    


# In[6]:

class LinearModule(Module):
    
    def __init__(self,input_dimension,output_dimension):
        self.input_dimension = input_dimension
        self.output_dimension = output_dimension 
        self.theta=np.zeros((self.input_dimension,self.output_dimension))
        self.gradient = np.ones((self.input_dimension,self.output_dimension))
    
    #Permet le calcul de la sortie du module
    def forward(self,input):
        out = np.dot(input,self.theta)
        return out
    
    #Permet le calcul du gradient des cellules d'entrée
    def backward_delta(self,input,delta_module_suivant):
        
        delta_in = np.dot(input,delta_module_suivant)
        return delta_in
    
    #Permet d'initialiser le gradient du module
    def init_gradient(self):
        self.gradient = np.zeros((self.input_dimension,self.output_dimension))
    
    #Permet la mise à jour des parmaètres du module avcec la valeur courante di gradient
    def update_parameters(self,gradient_step):
        self.theta += -gradient_step*self.gradient
    
    #Permet de mettre à jour la valeur courante du gradient par addition
    def backward_update_gradient(self,input,delta_module_suivant):
        
        input.shape = (input.shape[0],1)
        delta_module_suivant.shape = (1,delta_module_suivant.shape[0])
        self.gradient += np.dot(input,delta_module_suivant)
        
    #Retourne les paramètres du module
    def get_parameters(self):
        return self.theta
    
    #Initialize aléatoirement les p$aramètres du module
    def randomize_parameters(self, variance):
        #self.theta=np.random.randint(0,1,(self.input_dimension,self.output_dimension))
        #self.theta=np.random.randint(-variance,variance,(self.input_dimension,self.output_dimension))
        self.theta=np.zeros((self.input_dimension,self.output_dimension))


# In[7]:

class TanHModule( Module ) :
    def __init_(self,dimension) :
        self.X = dimension
    def forward(self,x):
        return np.tanh(x) 


# In[8]:

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


## Fonction pour plotter les classifier

# In[9]:

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

def plot2DSet(set):
    plt.scatter(set.x[:,0],set.x[:,1], c=set.y)
    plt.legend()
    plt.show()
    return


## Use this function if using kernel trick

# In[10]:

def plot_frontiere2(x, f, kernel, step=20):
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


## CREATE RANDOM DATASET

# In[11]:

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


# In[11]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



