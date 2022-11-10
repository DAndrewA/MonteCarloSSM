class BaseNoise:
    '''Base class for the Noise objects
    Each noise object will have two universal methods,

    METHODS:
        ~~~universal
        sample(): function that returns a random noise vector based on the distribution
        pdf(x): function that returns the probability density of the given noise vector x
    '''

    def sample():
        '''function that returns a random noise vector based on the distribution.'''
        # in the Base case, return a None object
        return None

    def pdf(x):
        '''Return the probability density of attaining the vector x in the random noise process'''
        # in the Base case, return a None object
        return None