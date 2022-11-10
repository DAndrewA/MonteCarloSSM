import numpy as np
from .Base import BaseState

class Velocity_nD(BaseState):
    '''Class to handle a state with an n-dimensional velocity vector.
    The velocity vector will determine the position, which we can measure. The velocity will be updated based on some noise.
    The position will be encoded in the first half of the state vector and the velocity will be encoded in the last half.
    '''

    def __init__(self,initP, initV, recordTrajectory):
        '''
        Inputs:
            initP [(nx1) ndarray] ; the initial position in real space for the state
            initV [(nx1) ndarray] ; the initial velocity in state-space
        '''

        self.n_dims_r = initP.shape[0]
        initS = np.hstack((initP,initV))
        print(initS)
        super().__init__(initS,recordTrajectory)

        return None

    def evolve_equation(self, **kwargs):
        '''Evolve the real-position of the state based on the velocity'''
        # in this instance, kwargs should contain the parameter dt.
        # if not, default to 0.1
        dt = 0.1
        if 'dt' in kwargs.keys():
            dt = kwargs['dt']

        s = self.S
        s[:self.n_dims_r] = s[:self.n_dims_r] + s[self.n_dims_r:]*dt
        return s

    def evolve_noise(self, **kwargs):
        dt = 0.1
        if 'dt' in kwargs.keys():
            dt = kwargs['dt']
        return super().evolve_noise(**kwargs) * dt

    def measurement_equation(self, **kwargs):
        '''Return the real-position of the state'''
        return self.S[:self.n_dims_r]

    def measurement_noise(self, **kwargs):
        '''Returns the noise on the measurement'''
        noise = np.random.normal(0,0.2,self.n_dims_r)
        return noise

