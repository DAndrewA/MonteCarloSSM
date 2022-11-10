import numpy as np

class Gaussian_independant:
    '''Class to handle Gaussian noise in n dimensions that is independant in each dimension.
    
    The class will take a vector for the centre of the noise distribution, and a vector for the standard deviations along each axis.
    '''

    def __init__(self, centre, sd):
        '''This class requires that centre and sd have the same dimensions'''
        self.centre = centre
        self.sd = sd
        self.n_dims = sd.size

        self.normalisation = np.power(2*np.pi, -0.5*self.n_dims) / np.prod(self.sd)

    def sample(self):
        return np.random.normal(self.centre,self.sd,self.n_dims)

    def pdf(self,x):
        gauss = np.exp( -0.5 * np.power((x - self.centre),2)/np.power(self.sd,2) )
        return gauss * self.normalisation