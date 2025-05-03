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

# State Value Function

$Q(s,a($ is referred to as the state value function and in our simplified rover example is calculated for both the left and right action for each state based on what the reward would be if it arrives at the terminal state.

![image](https://github.com/user-attachments/assets/60723b6b-e7fe-4912-bad6-1a36ac0c4136)

Based on the above screenshot, you can see that when you're in a state less that 5, you're better off going left whereas if you're in state 5 or 6, you're better off going right. Mathimatically and more generally, the way for the actor to choose the best possible action is given by $\max_{a} Q(s, a)$. So if you think of the policy as the roadmap that guides the actor, this will be influenced by computing $Q(s, a)$

Let's look at some code to generate a visualization for this state action value

```py
import numpy as np
import matplotlib.pyplot as plt

def generate_rewards(num_states, each_step_reward, terminal_left_reward, terminal_right_reward):

    rewards = [each_step_reward] * num_states
    rewards[0] = terminal_left_reward
    rewards[-1] = terminal_right_reward
    
    return rewards 

def generate_transition_prob(num_states, num_actions, misstep_prob = 0):
    # 0 is left, 1 is right 
    
    p = np.zeros((num_states, num_actions, num_states))
    
    for i in range(num_states):        
        if i != 0:
            p[i, 0, i-1] = 1 - misstep_prob
            p[i, 1, i-1] = misstep_prob
            
        if i != num_states - 1:
            p[i, 1, i+1] = 1  - misstep_prob
            p[i, 0, i+1] = misstep_prob
        
    # Terminal States    
    p[0] = np.zeros((num_actions, num_states))
    p[-1] = np.zeros((num_actions, num_states))
    
    return p

def calculate_Q_value(num_states, rewards, transition_prob, gamma, V_states, state, action):
    q_sa = rewards[state] + gamma * sum([transition_prob[state, action, sp] * V_states[sp] for sp in range(num_states)])
    return q_sa

def evaluate_policy(num_states, rewards, transition_prob, gamma, policy):
    max_policy_eval = 10000 
    threshold = 1e-10
    
    V = np.zeros(num_states)
    
    for i in range(max_policy_eval):
        delta = 0
        for s in range(num_states):
            v = V[s]
            V[s] = calculate_Q_value(num_states, rewards, transition_prob, gamma, V, s, policy[s])
            delta = max(delta, abs(v - V[s]))
                       
        if delta < threshold:
            break
            
    return V

def improve_policy(num_states, num_actions, rewards, transition_prob, gamma, V, policy):
    policy_stable = True
    
    for s in range(num_states):
        q_best = V[s]
        for a in range(num_actions):
            q_sa = calculate_Q_value(num_states, rewards, transition_prob, gamma, V, s, a)
            if q_sa > q_best and policy[s] != a:
                policy[s] = a
                q_best = q_sa
                policy_stable = False
    
    return policy, policy_stable


def get_optimal_policy(num_states, num_actions, rewards, transition_prob, gamma):
    optimal_policy = np.zeros(num_states, dtype=int)
    max_policy_iter = 10000 

    for i in range(max_policy_iter):
        policy_stable = True

        V = evaluate_policy(num_states, rewards, transition_prob, gamma, optimal_policy)
        optimal_policy, policy_stable = improve_policy(num_states, num_actions, rewards, transition_prob, gamma, V, optimal_policy)

        if policy_stable:
            break
            
    return optimal_policy, V

def calculate_Q_values(num_states, rewards, transition_prob, gamma, optimal_policy):
    # Left and then optimal policy
    q_left_star = np.zeros(num_states)

    # Right and optimal policy
    q_right_star = np.zeros(num_states)
    
    V_star =  evaluate_policy(num_states, rewards, transition_prob, gamma, optimal_policy)

    for s in range(num_states):
        q_left_star[s] = calculate_Q_value(num_states, rewards, transition_prob, gamma, V_star, s, 0)
        q_right_star[s] = calculate_Q_value(num_states, rewards, transition_prob, gamma, V_star, s, 1)
        
    return q_left_star, q_right_star


def plot_optimal_policy_return(num_states, optimal_policy, rewards, V):
    actions = [r"$\leftarrow$" if a == 0 else r"$\rightarrow$" for a in optimal_policy]
    actions[0] = ""
    actions[-1] = ""
    
    fig, ax = plt.subplots(figsize=(2*num_states,2))

    for i in range(num_states):
        ax.text(i+0.5, 0.5, actions[i], fontsize=32, ha="center", va="center", color="orange")
        ax.text(i+0.5, 0.25, rewards[i], fontsize=16, ha="center", va="center", color="black")
        ax.text(i+0.5, 0.75, round(V[i],2), fontsize=16, ha="center", va="center", color="firebrick")
        ax.axvline(i, color="black")
    ax.set_xlim([0, num_states])
    ax.set_ylim([0, 1])

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(axis='both', which='both', length=0)
    ax.set_title("Optimal policy",fontsize = 16)

def plot_q_values(num_states, q_left_star, q_right_star, rewards):
    fig, ax = plt.subplots(figsize=(3*num_states,2))

    for i in range(num_states):
        ax.text(i+0.2, 0.6, round(q_left_star[i],2), fontsize=16, ha="center", va="center", color="firebrick")
        ax.text(i+0.8, 0.6, round(q_right_star[i],2), fontsize=16, ha="center", va="center", color="firebrick")

        ax.text(i+0.5, 0.25, rewards[i], fontsize=20, ha="center", va="center", color="black")
        ax.axvline(i, color="black")
    ax.set_xlim([0, num_states])
    ax.set_ylim([0, 1])

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(axis='both', which='both', length=0)
    ax.set_title("Q(s,a)",fontsize = 16)

def generate_visualization(terminal_left_reward, terminal_right_reward, each_step_reward, gamma, misstep_prob):
    num_states = 6
    num_actions = 2
    
    rewards = generate_rewards(num_states, each_step_reward, terminal_left_reward, terminal_right_reward)
    transition_prob = generate_transition_prob(num_states, num_actions, misstep_prob)
    
    optimal_policy, V = get_optimal_policy(num_states, num_actions, rewards, transition_prob, gamma)
    q_left_star, q_right_star = calculate_Q_values(num_states, rewards, transition_prob, gamma, optimal_policy)
    
    plot_optimal_policy_return(num_states, optimal_policy, rewards, V)
    plot_q_values(num_states, q_left_star, q_right_star, rewards)

num_states = 6
num_actions = 2

terminal_left_reward = 100
terminal_right_reward = 40
each_step_reward = 0

# Discount factor
gamma = 0.5

# Probability of going in the wrong direction
misstep_prob = 0

generate_visualization(terminal_left_reward, terminal_right_reward, each_step_reward, gamma, misstep_prob)
```

With these default values, you will see a visualization like this

![image](https://github.com/user-attachments/assets/03be604f-37df-41c6-ba9d-2268ad113916)

If we change the misstep probability to .2, we'll see

![image](https://github.com/user-attachments/assets/525d0e06-1ead-4180-b736-7014411b8014)

The misstep prob is saying that if we're telling the rover to go right, there's an 80% chance it'll go right and a 20% chance it'll go left

## Bellman Equation

## $Q(s,a) = R(s) + \gamma \max_{a'} Q(s',a')$

* $Q(s,a)$ is the value of taking action a in state s
* $R(s)$ is the reward received in state s
* $\gamma$ is the discount factor for future rewards
* $max_{a'} Q(s',a')$ is the maximum Q-value possible in the next state $s'$

One note is that if you're in the terminal state, then there is no next state so $(Q(s,a)=R(s)$

![image](https://github.com/user-attachments/assets/b3c1f029-3d0a-4352-830f-17e0aed6c727)

Note that you can also factor out gamma to make the equation a little bit easier.

$$
R_1 + r R_2 + r^2 R_3 + r^3 R_4 + \cdots \\
R_1 + (r)[R_2 + r R_3 + r^2 R_4 + \cdots]
$$

![image](https://github.com/user-attachments/assets/68c34ad8-8726-48bb-a30f-00972871ed09)

Starting at state 5, we take action ← (left) to move to state 4, getting reward 0
After that, we follow the optimal policy:

From state 4, the optimal action is → (right), returning to state 5, with reward 0 discounted by 0.25²
From state 5, the optimal action is → (right), going to state 6, with reward 40 discounted by 0.25³

So the complete calculation is:
Q(5,←) = 0 + 0 × 0.25² + 40 × 0.25³ = 0 + 0 + 0.625 = 0.625

## Continuous State Value

A discrete state is used when something can only be in one distinct state at a time where a **continuous state** indicates that the object can be in a vector of states.

![image](https://github.com/user-attachments/assets/5f5d9128-41a9-4bc8-95d7-f1b49f257ed5)

The following is an example of the continuous state space for a lunar lander simulation

$$
s = \begin{bmatrix}
x \\
y \\
x' \\
y' \\
\theta \\
\phi \\
l \\
r
\end{bmatrix}
$$

where x and y are the horrizontal and vertical positions, %x'$ and $y'$ are speeds, %\theta$ is the angle, %\phi$ is the angular velocity. l and r correspond to the legs being touched down and will only correspond to a 1 or 0.

![image](https://github.com/user-attachments/assets/730ffd5f-6f2b-474c-b48f-5803ffebe881)

We also want to incorporate a reward function for the lunar lander as follows.

* Success Reward: You receive between 100-140 points for successfully reaching the landing pad
* Navigation Incentive: You get additional points for moving in the correct direction (toward the pad) and lose points for moving away from it
* Failure Penalty: Crashing results in a significant penalty of -100 points
* Successful Landing: A soft landing earns you +100 points
* Partial Success: Just getting the landing legs on the ground gives +10 points
* Fuel Efficiency:
 * Using the main engine costs -0.3 points per use
 * Using side thrusters costs -0.03 points per use

In cases where both the state and action space are discrete we can estimate the action-value function iteratively by using the Bellman equation. But when the state spaces are continuous, it becomes practically impossible to gradually estimate Q(s,a) unit it converges to the optional action-value function. to solver this and get an estimate for the optimal action-value function, we'll want to use a neural network architecture. This network will take our state vector as an input layer, use two hidden layers of 64 units, and have 1 output layer of 1 unit to generate Q(s,a)

![image](https://github.com/user-attachments/assets/59108de1-891c-4ae6-80ed-e288e5aecdfc)

The Q(s,a) with the maximum value will be the action that we take.

However, we see that it can be inefficient to use a new neural network each time. Let's instead refine this by defining one neural network to define all actions.

![image](https://github.com/user-attachments/assets/b306e3c9-0d95-40c7-a5d6-71eaf4f7ba14)


![image](https://github.com/user-attachments/assets/5f733b4e-cf39-4767-aace-c5ff08a76c43)

In reinforcement learning, you have the concept of taking greedy actions and taking exploration actions. Greedy actions are what has a higher probability of occuring. The computer picks this because it thinks it is the best move based on what it has learned so far. Exploration actions have a lower probability of occuring and the computer will pick it because, even though it seems worse, it may provide the computer something useful to know later. By providing the algorithm something usefult to know later, we mean that the accuracy of the estimates for Q(s,a) will be improved.

How this is used in reinforcement learning is that we have a value, $\epsilon$ which can be sets and passes to the algorithm to ensure that it expplores a little bit to find out new information. The exploratory action will be a completely random number so that the computer seems to act randomly. A common tactic is to start $\epsilon$ high and then gradually decrease it.

![image](https://github.com/user-attachments/assets/42482bde-9912-42f8-9871-b78e0e490f87)

Because of the high amount of computation, reinforcement learning algorithms are ecspecially sensative to hyperparameter tuning. Choosing the wrong params could mean that learning takes up to 10x as long.

## Lunar Lander Code

A deque is used which is a python data structure that adds/removes from both sides. 

```py
import time
from collections import deque, namedtuple

import gymnasium as gym
import numpy as np
import PIL.Image
import tensorflow as tf
import utils

from pyvirtualdisplay import Display
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.losses import MSE
from tensorflow.keras.optimizers import Adam

# Set up a virtual display to render the Lunar Lander environment.
Display(visible=0, size=(840, 480)).start();

# Set the random seed for TensorFlow
tf.random.set_seed(utils.SEED)

### HYPERPARAMS
MEMORY_SIZE = 100_000     # size of memory buffer
GAMMA = 0.995             # discount factor
ALPHA = 1e-3              # learning rate  
NUM_STEPS_FOR_UPDATE = 4  # perform a learning update every C time steps


```

The agent has four discrete actions available:

Do nothing.
Fire right engine.
Fire main engine.
Fire left engine.
Each action has a corresponding numerical value:

Do nothing = 0
Fire right engine = 1
Fire main engine = 2
Fire left engine = 3

```py
env = gym.make('LunarLander-v2')

# Reset the environment to the initial state
current_state = env.reset()
PIL.Image.fromarray(env.render(mode='rgb_array'))
```

![image](https://github.com/user-attachments/assets/b2028d39-36c9-472e-91d5-9c4113417e9d)

```py
# Select an action
action = 0

# Run a single time step of the environment's dynamics with the given action.
next_state, reward, done, _ = env.step(action)

# Display table with values.
utils.display_table(current_state, action, next_state, reward, done)

# Replace the `current_state` with the state after the action is taken
current_state = next_state
```

Now we'll create two neural networks

```py
# Create the Q-Network
q_network = Sequential([
    ### START CODE HERE ### 
    Input(state_size),
    Dense(64, activation="relu"),
    Dense(64, activation="relu"),
    Dense(num_actions, activation="linear")
    
    ### END CODE HERE ### 
    ])

# Create the target Q^-Network
target_q_network = Sequential([
    ### START CODE HERE ### 
    Input(state_size),
    Dense(64, activation="relu"),
    Dense(64, activation="relu"),
    Dense(num_actions, activation="linear")
    ### END CODE HERE ###
    ])

### START CODE HERE ### 
optimizer = Adam(learning_rate=ALPHA)
### END CODE HERE ###
```

Now we'll add the experience buffer as a named tuple

```py
# Store experiences as named tuples
experience = namedtuple("Experience", field_names=["state", "action", "reward", "next_state", "done"])
```

Next we compute a loss function between the neural network and our estimates

```py
def compute_loss(experiences, gamma, q_network, target_q_network):
    """ 
    Calculates the loss.
    
    Args:
      experiences: (tuple) tuple of ["state", "action", "reward", "next_state", "done"] namedtuples
      gamma: (float) The discount factor.
      q_network: (tf.keras.Sequential) Keras model for predicting the q_values
      target_q_network: (tf.keras.Sequential) Keras model for predicting the targets
          
    Returns:
      loss: (TensorFlow Tensor(shape=(0,), dtype=int32)) the Mean-Squared Error between
            the y targets and the Q(s,a) values.
    """

    # Unpack the mini-batch of experience tuples
    states, actions, rewards, next_states, done_vals = experiences
    
    # Compute max Q^(s,a)
    max_qsa = tf.reduce_max(target_q_network(next_states), axis=-1)
    
    # Set y = R if episode terminates, otherwise set y = R + γ max Q^(s,a).
    ### START CODE HERE ### 
    y_targets = rewards + (1-done_vals) * gamma * max_qsa
    ### END CODE HERE ###
    
    # Get the q_values and reshape to match y_targets
    q_values = q_network(states)
    q_values = tf.gather_nd(q_values, tf.stack([tf.range(q_values.shape[0]),
                                                tf.cast(actions, tf.int32)], axis=1))
        
    # Compute the loss
    ### START CODE HERE ### 
    loss = MSE(y_targets, q_values) 
    ### END CODE HERE ### 
    
    return loss
```

Next, the following function will update the weights of the target network

```py
@tf.function
def agent_learn(experiences, gamma):
    """
    Updates the weights of the Q networks.
    
    Args:
      experiences: (tuple) tuple of ["state", "action", "reward", "next_state", "done"] namedtuples
      gamma: (float) The discount factor.
    
    """
    
    # Calculate the loss
    with tf.GradientTape() as tape:
        loss = compute_loss(experiences, gamma, q_network, target_q_network)

    # Get the gradients of the loss with respect to the weights.
    gradients = tape.gradient(loss, q_network.trainable_variables)
    
    # Update the weights of the q_network.
    optimizer.apply_gradients(zip(gradients, q_network.trainable_variables))
```

Now, we can implement the full algorithm that uses 2000 episodes to try to increase accuracy.

```py
start = time.time()

num_episodes = 2000
max_num_timesteps = 1000

total_point_history = []

num_p_av = 100    # number of total points to use for averaging
epsilon = 1.0     # initial ε value for ε-greedy policy

# Create a memory buffer D with capacity N
memory_buffer = deque(maxlen=MEMORY_SIZE)

# Set the target network weights equal to the Q-Network weights
target_q_network.set_weights(q_network.get_weights())

for i in range(num_episodes):
    
    # Reset the environment to the initial state and get the initial state
    state = env.reset()
    total_points = 0
    
    for t in range(max_num_timesteps):
        
        # From the current state S choose an action A using an ε-greedy policy
        state_qn = np.expand_dims(state, axis=0)  # state needs to be the right shape for the q_network
        q_values = q_network(state_qn)
        action = utils.get_action(q_values, epsilon)
        
        # Take action A and receive reward R and the next state S'
        next_state, reward, done, _ = env.step(action)
        
        # Store experience tuple (S,A,R,S') in the memory buffer.
        # We store the done variable as well for convenience.
        memory_buffer.append(experience(state, action, reward, next_state, done))
        
        # Only update the network every NUM_STEPS_FOR_UPDATE time steps.
        update = utils.check_update_conditions(t, NUM_STEPS_FOR_UPDATE, memory_buffer)
        
        if update:
            # Sample random mini-batch of experience tuples (S,A,R,S') from D
            experiences = utils.get_experiences(memory_buffer)
            
            # Set the y targets, perform a gradient descent step,
            # and update the network weights.
            agent_learn(experiences, GAMMA)
        
        state = next_state.copy()
        total_points += reward
        
        if done:
            break
            
    total_point_history.append(total_points)
    av_latest_points = np.mean(total_point_history[-num_p_av:])
    
    # Update the ε value
    epsilon = utils.get_new_eps(epsilon)

    print(f"\rEpisode {i+1} | Total point average of the last {num_p_av} episodes: {av_latest_points:.2f}", end="")

    if (i+1) % num_p_av == 0:
        print(f"\rEpisode {i+1} | Total point average of the last {num_p_av} episodes: {av_latest_points:.2f}")

    # We will consider that the environment is solved if we get an
    # average of 200 points in the last 100 episodes.
    if av_latest_points >= 200.0:
        print(f"\n\nEnvironment solved in {i+1} episodes!")
        q_network.save('lunar_lander_model.h5')
        break
        
tot_time = time.time() - start

print(f"\nTotal Runtime: {tot_time:.2f} s ({(tot_time/60):.2f} min)")
```
