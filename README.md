# MonteCarloSSM
(hopefully) A generalised framework for State-Space Modelling using Bayesian particle filtering.

## The plan:

The SSM allows for a complex system to be modelled allowing for a level of abstraction in measurement. I will allow for Bayes' principle to be implemented through Importance Sampling (IS) in a Monte Carlo particle distribution.

I will need to implement a system to allow for the true state to be evolved given an equation of motion. I will also need to allow for the evolution of simulated particles, possibly by a different function. I need to allow for the modelling of the measurements of the true state, and then working back to the bayesian description of the particles (filtering).

As the simulation continues, I want to implement resampling, culling the most unlikely particles, and generating new trajectories from a distribution within the non-culled trajectories.

I would also like to allow for plotting of the trajectories.

## To Do

+ Implement a way to evolve the true system state. From this, I should be able to implement a similar system to evolve the particles.
+ Implement a way to take measurements from the true state, subject to noise.
+ Reverse engineer this to allow for the likelihood of the trajectories to be inferred from the measurements.

+ Monte Carlo particle generation and particle evolution.
+ Calculating the relative weighting of the particle trajectories.
+ Resampling based on likely trajectories. This could be done by uniformly sampling a cdf of the trajectory weights (higher weighted trajectories more likely, but all possible).

+ Implement the matplotlib FuncAnim class to allow the trajectories to be plotted.
+ For a fixed plot history (for the trajectories), could have lists of a fixed length, and an alpha list of the same length. As frame (index) increases, the frame%length element can be updated, and the alpha for all the points can be decreased by some value.
