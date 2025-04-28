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

