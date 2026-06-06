# Intro

Reasoning models are needed when your task involves complexity like math and involves more compute. Don't confuse this with extended thinking. Most modern models like deepseek, chatgpt o models are reasoning models which you can see by the fact that it uses chain of thought before it comes up with an answer. When you turn on extended thinking, you're just telling the model to use more tokens in chain of thought before it responds. You would want to do this if you have a complex reasoning problem like math. If what you're doing is just retrieving a definition like asking what gradient descent is, you don't need extended thinking.

* This book will help us to understand when we need extended thinking.

## Defining

Reasoning can be visible steps you see in claude or they may be enclosed in `<think>` internally. These are not HTML but special tokens that some models use in their API responses to denote steps. The model knows to use this as a scratchpad and not have it in final output. 

The `<think>` tag is interesting because it can lead to the area of prompt injection. LLMs are usually sophisticated enough to recognize this

Conventional LLMs won't show how they came up with an answer so chain of thought on a reasoning model allows the user to essentially show their work. Think of it like teachers asking us to show our work whenever doing a math problem because they wanted to make sure that the method that we chose to use is correct and will work on other problems.

It's important to keep in mind that this reasoning follows the same principles as the LLM meaning the tokens that it generates is a stochastic process and is subject to the same mistakes. However chain of thought can help to correct this as its own steps can help to course correct the overall thinking. It's also worth noting that it's equally likely that a model can double down on a false assumption. Chain of thought raises the probability of correctness on complex tasks but doesn't eliminate the stochastic risk. It's a better bet, not a guarantee.

In contrast, humans can be trained to apply deterministic mental models like when your math teacher teaches you the rules for taking derivatives or expanding polynomials.

## LLM Training

Convential LLMs work by breaking down text into tokens and then using stochastic processes to predict the next token. 

### Pretraining

It's pretained on several terabytes of data equating to trillions of tokens. This process of pretraining has also revealed **emergent properties** such as the LLM being to do tasks like translation which it wasn't explicitly trained to do. Because of the expenses of pretraining (months of GPUs running equation to millions of dollars in electricity), some of these are made available as the set of weights that you can download.

For example, BERT is pretrained from google on thousands of books and wikipedia. You could grab this pretained model from the internet and then post train it to your specific domain (like legal documents) and then use that at your company/firm to search documentation.

### Post training

Post training is when you take the pretrained model and attempt to apply it to your domain. There are two stages.

#### Supervised fine tuning

Produce a factual (still stochastic) summary of the information that you have. No emotion.

#### Preference tuning

Produce the summary in the preference that the user is looking for. This could be in a warm tone if the user prefers. This is done using reinforcement learning with human feedback (RLHF) where a human picks output that is supposedly more helpful. The problem with this approach is that it's subject to the bias of the human that picks the output.

From brief looking online, this has led to reinforcement learning with AI feedback (RLAIF) where you have AI picking output for the preference tuning. RLHF is also expensive because you pay people to label data for the AI whereas having AI do it is a lot cheaper.

Deepseek has improved on this further with reinforcement learning with verifiable rewards. I don't quite understand this but this is just using objective answers based on math to find the best labeling.

#### Chatbot

After post training, the LLM will still need things like a prompt box for the user, the context window, and the system prompt to guide its responses.

The context window is the entire history of prompts and responses with the user. It's what exists in one session with Claude or ChatGPT. 

The system prompt can be what anthropic or openai has built into the LLM to give instructions like "don't tell them how to make poison" as well as your own instructions you can give in the settings such as "I am an aspiring data scientist".

## Improving reasoning

Advances in LLM capabilities with reasoning and extended thinking came in late 2024 and early 2025. There are three main methods for reasoning training that occur after pre and post training. All of these methods are discussed more in depth later in the book.

### Inference Compute Scaling

Traditionally, the only way to improve model performance was to train a bigger model on more data. Inference compute scaling is a different idea: spend more compute at the moment of generating a response to improve output quality, without changing the model's weights at all.

So as long as the model has already been trained to reason, we can use this technique and avoid retraining entirely.

At inference time, this reasoning capability is activated when you enable extended thinking — the model applies its trained reasoning ability to your specific prompt by exploring and extending its reasoning chain, potentially backtracking and self-correcting before committing to a final answer.

### Reinforcement Learning

This is additional training that happens after post training where you use additional RL to reason more deeply. This is different from RL used during preference tuning in post training.

Post-training RL makes the model behave well. Reasoning RL makes the model think well.

### Distillation

This where we take a freshly trained post trained model and have it trained from a larger model with reasoning capabilities so instead of the model using RL to relearn how to reason (which can be costly with both time and money), the new model learns to just imitate the actions of a larger model that has already done this. It's like just learning to reason from a college professor rather than just reading a bunch of books.

## Pattern Matching vs Logical Reasoning

Traditionally LLMs learn **pattern matching** and simply predict the text word by strong statistical associations. For instance, if you ask "What is the capital of germany", the LLM is recalling a strong statical correlation between those words and the answer "Berlin"

**Logical Reasoning** is when the model derives the answer from a set of fact based rules. This is where the chain of thought comes into play and creates intermediate steps where the model can draw implications based on these intermediate steps.

Traditionally, an LLM will be **closed world** and only use the prompt to determine the answer. So if the prompt is "All penguins can fly. A penguin is a bird. Can a bird fly?", The answer would be yes if we use that closed world setting.

The difference with reasoning models is that it is an **open world setting** and brings in external facts. The external fact is that penguins cannot fly. If this external fact is added as an intermediate step when determining off the prompt, the LLM will arrive at a contridiction. 

The author also offers an example the GPT4.0, not an explicit reasoning model, will still arrive at the conclusion that penguins cannot fly. This is a good example because it speaks to the fact that these models have still built statistical associations in its training data that penguins are a flightless bird.

## Why build reasoning models

Since Deepseek R1 in January 2025, developing reasoning models has become the top priority for many companies.

There is a good case to be made that reasoning models are not necessary for everyday tasks. They are best for complex tasks involving chain of thought like planning in coding agents. However, they are more expensive to use because of the higher token usage. They can also be more prone to error due to overthinking, therefore they can be inefficient to use for simple tasks like text summerization and translations. 

This brings up the thought that people may treat extended thinking like it gives a better answer in every situation and just apply it to everything. I had claude give me an analogy that I think illustrates this:

### Hiring a consultant to decide what to eat for lunch.

A consultant is genuinely valuable for problems with complexity, stakeholder tradeoffs, and non-obvious structure. But for "should I get the sandwich or the salad" — the bottleneck isn't analytical firepower, it's just a quick personal preference check. The consultant doesn't give you a better lunch. They give you a 40-slide deck about your lunch, and now you're late and still hungry.

The consultant's time and hours would better used for more complex tasks like are we utilizing AI to the best of our abilities.

Since an LLM uses the transformer neural network architecture, each token requires a forward pass and each pass involves billions of parameters. This means that if you're using extended thinking on the reasoning model, the answer may involve twice as many (probably more) forward passes through the network because of the intermediate steps. This increases token cost dramatically both financially and through latency.

Furthermore, many times the workflow will involve the model calling itself again and again extending the cost and token budget. Consider the following typical workflow.

* A user asks a question
* The model decides it needs to search for information
* The search result comes back and gets fed into the model again
* The model reasons over the result and decides it needs to call another tool
* That result comes back, another pass happens
* Finally the model produces a response

This translates to the coding world. Copilot in vscode gives you a choice of models and each model might have a different multiplier of how much that it counts toward your budget. For example, Claude Opus had their latest model at 15x which would mean that I'd reach my token budget very quickly. So I'd have to consider the tasks that I had.

A simple autocomplete or a boilerplate code suggestion doesn't need a large reasoning model — a smaller, faster model handles it fine and costs very little per call. But I ran into a situation where I discovered a major bug which required a refactor in multiple files. That refactor had to be handled differently based on how much the bug affected the code of that component. This is an example where I wanted to use a larger Opus model and eat the costs. The key takeaway is that this example was very reason heavy. Something that would have taken me my entire day to reason around.

## Roadmap

Most reasoning models are trained on top of an existing LLM rather than trained from scratch. The author will do similar here where we'll first code a conventional LLM, learn to evaluate its current reasoning, and then add reasoning on top of this.
