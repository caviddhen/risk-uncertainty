# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:02:57 2018

@author: SRG
"""
import numpy as np
import scipy
import matplotlib.pyplot as plt

class Bayes():
    
    def __init__(self,samples, prior, x):
        self.prior = prior  #prior probabilities
        self.x=x   #hypothesis
        self.samples = samples #samples as matrix (each sample in another row of the type (k,n))
    
    def update(self):
        #Bayes update
        posterior = self.prior
        i=0
        for i in range(0,np.alen(self.samples)):
            n = self.samples[i,1]
            k = self.samples[i,0]
            nominator = scipy.math.factorial(n)/(scipy.math.factorial(k)*scipy.math.factorial(n-k))*(1-self.x)**(n-k)*self.x**k * posterior
            denominator = np.sum(nominator)
            posterior = nominator/ denominator

        #plt.figure()
        #plt.plot(x,posterior)
        #plt.ylabel('density')
        #plt.xlabel('possible probability')
        #plt.show()
        return posterior
    
    
#samples = np.concatenate((np.ones((100,1)),np.ones((100,1))*10),axis=1) #see the learning!
samples=np.array([[22,149]])        #sample from class
x = np.arange(0,1,1/1000)           #hypothesis
prior = np.ones(x.shape)/1000       #prior

A = Bayes(samples,prior,x)       
posterior = A.update()
plt.figure()
plt.plot(x,posterior)
plt.ylabel('density')
plt.xlabel('possible probability')
plt.show()        
