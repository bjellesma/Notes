# Intro

Reasoning models are needed when your task involves complexity like math and involves more compute. Don't confuse this with extended thinking. Most modern models like sonnet 4.5 are reasoning models which you can see by the fact that it uses chain of thought before it comes up with an answer. When you turn on extended thinking, you're just telling the model to use more tokens in chain of thought before it responds. You would want to do this if you have a complex reasoning problem like math. If what you're doing is just retrieving a definition like asking what gradient descent is, you don't need extended thinking.

* This book will help us to understand when we need extended thinking.

## Defining

Reasoning can be visible steps you see in claude or they may be enclosed in `<think>` internally. These are not HTML but special tokens that some models use in their API responses to denote steps. The model knows to use this as a scratchpad and not have it in final output. 

The `<think>` tag is interesting because it can lead to the area of prompt injection. LLMs are usually sophisticated enough to recognize this

Conventional LLMs won't show how they came up with an answer so chain of thought on a reasoning model allows the user to essentially show their work. Think of it like teachers asking us to show our work whenever doing a math problem because they wanted to make sure that the method that we chose to use is correct and will work on other problems.

It's important to keep in mind that this reasoning follows the same principles as the LLM meaning the tokens that it generates is a stochastic process and is subject to the same mistakes. However chain of thought can help to correct this as its own steps can help to course correct the overall thinking. It's also worth noting that it's equally likely that a model can double down on a false assumption. Chain of thought raises the probability of correctness on complex tasks but doesn't eliminate the stochastic risk. It's a better bet, not a guarantee.

In contrast, humans can be trained to apply deterministic mental models like when your math teacher teaches you the rules for taking derivatives or expanding polynomials.

## LLM Training

Convential LLMs work by breaking down text into tokens and then using stochastic processes to predict the next word. 

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

OpenAI builds reasoning capability into the weights during training. At inference (when you build a prompt) time, this capability is activated when you select a reasoning model or enable extended thinking — the model then applies that trained reasoning ability to your specific prompt.

### Reinforcement Learning

This is additional training that happens after post training where you use additional RL to reason more deeply. This is different from RL used during preference tuning in post training.

Post-training RL makes the model behave well. Reasoning RL makes the model think well.

### Distillation

This where we take a freshly trained post trained model and have it trained from a larger model with reasoning capabilities so instead of the model using RL to relearn how to reason (which can be costly with both time and money), the new model learns to just imitate the actions of a larger model that has already done this. It's like just learning to reason from a college professor rather than just reading a bunch of books.
