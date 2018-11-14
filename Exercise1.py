import numpy as np
import matplotlib.pyplot as plt
#from scipy.stats import norm
from statsmodels.distributions.empirical_distribution import ECDF

class Propagation:
    #define parameters for parameter (theta1, theta2m theta3) - distribution
    p11 = 85    #for theta1
    p12 = 10    #for theta2
    p21 = 2    #for theta2
    p22 = 2    #for theta2
    p31 = 1    #for theta3
    p32= 1    #for theta3
    def __init__(self,timegrid=range(1,100),simnumber=10000):
        self.SimulationNumber = simnumber       #number of Monte-Carlo Simulations
        self.Timegrid = timegrid                #time grid for interpolation

    def results(self):
    #computes Monte-Carlo results for all times in time grid
        theta1 = np.random.normal(self.p11,self.p12,size=(self.SimulationNumber,))
        theta2 = np.random.uniform(self.p21,self.p22,size=(self.SimulationNumber,))
        theta3 = np.random.uniform(self.p31,self.p32,size=(self.SimulationNumber,))
        result=np.empty((len(self.Timegrid),self.SimulationNumber))
        for i in range(0,len(self.Timegrid)):
            result[i,:]=theta1/((self.Timegrid[i]/theta2+1)**theta3)
        return result

    def cdf(self,time):
    #computes cdf for a given time
        t = np.abs(np.array(self.Timegrid)-time).argmin()
        ecdf=ECDF(self.results()[t,:])
        plt.plot(ecdf.x,ecdf.y)
        return ecdf.x

    def statistics(self):
    #computes mean, 5% and 95% percentile for all times
        upper = np.percentile(self.results(),95,axis=1)
        lower = np.percentile(self.results(),5,axis=1)
        mean = np.median(self.results(),axis=1)
        return [mean,lower,upper]

    def plotstatistics(self):
    #plots
        mean, lower, upper = self.statistics()
        plt.plot(lower,'r')
        plt.plot(upper,'r')
        plt.plot(mean,'b')
        plt.xlabel('time t')
        plt.ylabel('concentration')
        plt.title('Concentration with 5% quantiles')

#Call
A = Propagation()
A.plotstatistics()
plt.figure()
A.cdf(10)
plt.figure()
A.cdf(100)
plt.show()
