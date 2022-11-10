import numpy as np

class BaseState:
    '''Class to store the information about the real state, its evolution, and the measurement process
    
    Attributes:
        n_dims [int] ; the number of dimensions the state vector exists in.
        initS [(n_dims,) ndarray] ; the initial true state of the system from which to evolve the future states.
        S [(n_dims,) ndarray] ; the current state of the system.
        recordTrajectory [bool] ; flag for whether or not to record the historical trajectory, or whether we can just store the current state.
        trajectory [(n_dims, t) ; ndarray] the state for the t time steps that have been calculated. Only if recordTrajectory == True.


    Methods:
        __init__:
            initialise the state. This will take the inputs n_dims, initS, recordTrajectory.
        evolve:
            function to evolve the state based on some evolution function and a noise term.
        make_measurement:
            function to make a measurement on the current state vector, dependant on the measurement relation and some noise term.

        The following methods will change depending on the children class
        evolve_noise:
            function that determines the noise on the evolving state. return zeros for deterministic true evolution.
        evolve_equation:
            function that takes the current state, and returns the state evolved according purely to the equations of motion.
        measurement_equation:
            function that performs a measurement based on the current state vector.
        measurement_noise:
            function that returns the noise on the measurement.
    '''
    
    def __init__(self, initS, recordTrajectory):
        self.S = initS.flatten()
        self.n_dims = initS.shape[0]

        self.recordTrajectory = recordTrajectory

        if self.recordTrajectory:
            self.trajectory = initS.reshape((self.n_dims,1))
        
        return None

    def evolve(self,**kwargs):
        '''Evolves the state depending on a given function, with some noise applied too.
        
        In the base class, this will simply be no evolution with normally distributed Gaussian noise being applied.

        kwargs is used to allow the passing of information to the noise and evolution functions if the particular state requires it.
        '''
        noise = self.evolve_noise(**kwargs)#np.random.normal(0,1,self.n_dims)
        self.S = self.evolve_equation(**kwargs) + noise

        if self.recordTrajectory:
            self.trajectory = np.hstack((self.trajectory ,self.S.reshape((self.n_dims,1))))

        return None

    def make_measurement(self, **kwargs):
        '''Performs a measurement on the current state, with some noise applied too.
        
        In the base class, this will simply be a direct measurement with normally distributed Gaussian noise being applied.
        '''
        noise = self.measurement_noise(**kwargs)
        measurement = self.measurement_equation(**kwargs) + noise

        return measurement


    # State evolution functions, that should change between children classes.
    # Passing of kwargs allows for dynamic updating of the evolution based on some external parameters that can be set within the program.
    def evolve_noise(self, **kwargs):
        '''Returns the noise on the state evolution.
        In the BaseState class, this will simply return normally distributed Gaussian noise.
        '''
        n = np.random.normal(0,1,self.n_dims)
        return n

    def evolve_equation(self, **kwargs):
        '''Returns the new state vector, evolved from the self.S attribute.
        In the BaseState class, this will simply return the current state.
        '''
        return self.S

    def measurement_equation(self, **kwargs):
        '''Returns the measurement vector, determined by the current self.S value.
        In the BaseState class, this will simply be the state measured directly.
        '''
        return self.S

    def measurement_noise(self, **kwargs):
        '''Returns the noise on the measurement. The output must be the same dimensions as the measurement vector.
        In the BaseState class, this will be normally distributed Gaussian noise.
        '''
        return np.random.normal(0,1,self.n_dims)
