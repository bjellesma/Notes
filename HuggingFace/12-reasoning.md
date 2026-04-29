Google's "Attention is all you need" paper introduced attention in the transformer architecture which let models pay attention to certain patterns. This completely replaced recurrent architectures for use in an LLM entirely.

Deepseek in 2025 changed how LLMs work because its use of reinforcement learning showed how training can be done a lot cheaper. 

**Exploration** is making random actions to find more information about the environment.
**Exploitation** is just using the usual path.
**Policy** dictates the action that you take which is either exploration or exploration.

**Policy based actions** can be **Deterministic** where a policy at a given state will always return the same action. It can slo be **stochastic** where a policy will output a probability distribution.

**Value based method** involves thinking about an expected future value that you think will be worth more. This is akin to you staying at a job longer because you think you'll get a bigger reward.
<img width="638" height="175" alt="image" src="https://github.com/user-attachments/assets/72c9cfe0-b2c8-42c8-a0d4-40de51b06bf8" />

When we turn on extended thinking in an LLM, we force the agent to go more into chain of thought reasoning. Chain of thinking is where the model works through the intermediate steps more explicitly.

The **Bellman Equation** expresses the value of a state as the immediate reward plus the discounted value of the next state, allowing value to be computed recursively.

The **Monte Carlo** approach updates the value function after each episode of the program. An episode is the RL concept of one full run through the environment.

