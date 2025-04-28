# Reinforcement Learning

The basics of reinforcement learning are that we need to find of way to map from the state, s, of the actor to the desired action, a. Like reinforcement learning in human beings, we want to use a reward function that will act positive for good behavior and negative for bad behavior. This will act as an incentive for the actor to learn the desired behavior.

Some common applications for reinforcement learning are:

* Controlling robots
  * Mars rover
  * Boston Dynamics
  * Tesla cars
* Factory optimization
* financial trading
* games
  * Everything from chess to checkers to DOTA

The big thing with reinforcement learning is that the only thing that needs to be specified by you is the reward function which serves to guide the behavior of the actor.

Let's start with a simplified example of the Mars rover where one site has a reward of 40 and another site has a reward of 100. These states are referred to as **terminal states** because this is where the actions end. The actor (the rover) is incentivized to go to 100 terminal states as that is the larger reward.

![image](https://github.com/user-attachments/assets/38e53fc0-2f4b-42e3-833e-66b47ce837b5)

This leads to an issue however as the 100 is farther away than the 40 meaning that the actor will take more time to get to the 100. So is it worth it for the actor to take longer to get the larger reward? Well this depends on the reward function offered. 

In our example of the simplified mars rover, we use the concept of a **discoun factor**, denoted $\gamma$ which serves to diminish the reward the longer that it has to travel. A common choice for this discount factor is close to 1.

Adding a discount factor of .9 gives us $\text{Return} = 0 + (0.9)0 + (0.9)^2 0 + (0.9)^3 100 = 0.729 \times 100 = 72.9$

![image](https://github.com/user-attachments/assets/2e8788c5-4bbc-42b4-baaa-ef3ba8736978)

Now as you can see, if you start in different states you will get different rewards because you won't be hit as much with a discount factor.

![image](https://github.com/user-attachments/assets/55227c82-b406-4729-b87e-a75b1192f849)

A **policy**, denoted $\pi$, is a strategy or function that determines what action an agent should take in a given state. It's essentially the decision-making rule that maps states to actions. Most policies that we refer to are **deterministic** meaning they map each state to a specific action. A **stochastic policy** maps state to probability distributions giving the probability of taking action a when in state s.

Reinforcement Learning uses the mathematical framework of **Markov Decision Process (MDP)** where

The environment has states
An agent can take actions in each state
Actions lead to transitions between states with certain probabilities
Actions result in rewards
The future state depends only on the current state and action (the Markov property)

![image](https://github.com/user-attachments/assets/8ea156be-654b-48e5-a6f4-aca4e3315b01)
