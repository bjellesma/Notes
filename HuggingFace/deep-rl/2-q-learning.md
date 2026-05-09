# RL Recap

A short recap of reinforcement learning is that a policy, $/pi$ will be used to move the agent from a state to an action. The goal of an RL policy is to maximize its expected cumulative reward.

<img width="1416" height="813" alt="image" src="https://github.com/user-attachments/assets/f562c942-0591-41f5-9f8f-56f74e1b7472" />

There are two main types of RL methods to find the optimal policy:

**Policy based methods**: train the policy directly to learn which action to take given the state. This learns from trial and error. These use **gradient ascent** to redefine the policy after each trial. An example application of this would be poker where the optimal strategy would be to be unpredictable. The output of a policy is an action answering the question of what to do next.
**Value based methods**: Train a value function to learn which state is more valuable and use this value function to take the action that leads to it. These learn the future states/values first and then derives behavior from there. In this, you don't train the policy as your policy is just a predefined function. The output of a value function is just a number that simply answers how well the model did. The agent will use this output to determine the next steps.

In the analogy of chess, policy based learns by playing the game a lot while value based spends time to build a map first.

The value of a state is expected discounted return the agent can get it starts at that state and then acts according to our policy. In the following, V is the value function, E is the expected discounted return, and s is starting at state 1.

Note that the above equation is not a conditional probability. The pipe character just means "given that"

$$v_{\pi}(s) = \mathbb{E}_{\pi}\left[R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \ldots \mid S_t = s\right]$$

**Exploration** and **Exploitation** are two concepts where your next move can value learning (exploration) more than just picking the next best value (exploitation).

**greedy policy** is a value based method where we just always choose the action with the highest known value. No exploration, just exploitation.

There are two types of value based functions

## State Value Function

For each state, the state-value function outputs the expected return if the agent starts at that state and then follows the policy forever afterward

$$V_{\pi}(s) = \mathbb{E}_{\pi}\left[G_t \mid S_t = s\right]$$

G is the discounted cumulative return that we saw earlier where we use a discount coefficient for each future.

## Action Value Function

The action is also taken into account. The advantage of this over state value is that you don't need a model beforehand

$$Q_{\pi}(s, a) = \mathbb{E}_{\pi}\left[G_t \mid S_t = s, A_t = a\right]$$

Given that action value based methods don't require a model, this is more practical than state value alone.

<img width="1352" height="793" alt="image" src="https://github.com/user-attachments/assets/a41ea13d-29ef-4d81-ab51-37c6822ad2db" />

# Bellman

The **Bellman Equation** expresses the value of a state as the immediate reward plus the discounted value of the next state, allowing value to be computed recursively.

In the below screenshots, we're calculating the value at each state.

<img width="1370" height="768" alt="image" src="https://github.com/user-attachments/assets/4435439f-61ca-4feb-8735-5f2d1cec7802" />

<img width="1388" height="798" alt="image" src="https://github.com/user-attachments/assets/b0ce2423-5fbb-4095-ae58-14c95dde9b09" />

<img width="1363" height="785" alt="image" src="https://github.com/user-attachments/assets/0912c574-f3b7-45f5-b61b-6749dc8e19cc" />

The Bellman equation simplifies this so that we can instead have this in one neat function

$$V_{\pi}(s) = \mathbb{E}_{\pi}\left[R_{t+1} + \gamma * V_{\pi}(S_{t+1}) \mid S_t = s\right]$$

Going back to the mouse example, we can calculate the value at state 1 <img width="1354" height="768" alt="image" src="https://github.com/user-attachments/assets/f0074727-bc41-4f6c-96c2-0b4eba202e53" />

# Monte Carlo and Temporal Displacement

The **Monte Carlo** approach updates the value function after each episode of the program. An episode is the RL concept of one full run through the environment.

## Monte Carlo: learning at the end of an episode

At the end of the episodes, we have a list of state, actions, rewards, and new states. The agent will sum the total rewards (G) to see how it did and it will use that to update the value function.

<img width="1341" height="757" alt="image" src="https://github.com/user-attachments/assets/5ba2da4a-c11b-4ef3-9642-a4f74de27a94" />

Monte Carlo is high variance and unbiased.

## Temporal Difference Learning: learning at each step

**Temporal Difference** waits for one step, S, to update value function V

But because we didn’t experience an entire episode, we don’t have G (expected return). Instead, we estimate G by adding $R_{t+1}$ and the discounted value of the next state.

Temporal Difference is low variance and some bias

<img width="1302" height="741" alt="image" src="https://github.com/user-attachments/assets/fc10cc25-2fbd-4ff0-accb-62dd4c44e950" />

## Choosing between the two

Temporal Difference is low variance and some bias whereas Monte Carlo is high variance and unbiased. This is a tradeoff to be considered

# Q learning

**Quality Learning** (often referred to as q learning) is an algorithm that is an action value based method


