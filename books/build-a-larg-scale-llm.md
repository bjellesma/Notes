ChatGPT is an NLP built using the transformer architecture. The GPT part stands for generative pretrained transformer

![image](https://github.com/user-attachments/assets/f05f7ff3-faf6-46f7-b4a9-afebb79be548)

ChatGPT is a general purpose LLM and research has shown that LLMs built for a specific purpose like finance or medical perform better in their respective fields.

The first step for building a custom LLM is that the LLM must go through pre training where it is trained on a large and diverse dataset to understand language better. This pretraining is often done on unlabeled data on the internet. It is now capable of simple things like text completion. It can thenn be finetuned on a set of labeled data to then be able to do things like personal assistant and summerization.

![image](https://github.com/user-attachments/assets/62786a0f-7b69-4274-a4ff-2b8c96dad73e)

ChatGPT3 was originally only capable of doing tasks like completing half written sentences.

Once the LLM is trained on a diverse set of unlabeled data, the model can then be finetuned in one of two ways. **Instructional Finetuning** is when the labeled data given to the model is in the form of a query and then the correctly translated answer. **Classification Finetuning** is when the model is used for something like filtering where there were only a few sets of outputs. Classification involves feeding the LLM labeled data such as email and then correctly classifying it.

The advent of deep learning transformers came from a 2017 paper titled "Attention is all you need". The intent was to build a translation model whereas you encode the english text as a set of vectors and then decode those vectors into the German translation.

![image](https://github.com/user-attachments/assets/8146385e-5aa8-418e-b878-f01282be21d2)

The key to the transformer architecture shown above is the **self attention mechanism** which is not depicted. This mechanism places weights  on different words in the sequence that they appear in the text. 

Besides using this transformer architecture to build a GPT, you can also use it to build a **BERT (Bidirection Encoder representations from Transformers)**. These are used more for sentiment analysis. For example, these may be used by social media websites to try to detect harmful content.

Just because ChatGPT is built on the transformer architecture does not mean that all LLMs are. Some LLMs are built on recurrent and convolutional architectures. However, this book uses transformers and LLMs synomously.

**tokens** will refer to a unit of text for LLMs. These are not necessarily complete words as a token can be something like a subword, punctuation, or even special characters like &. 

GPT first came out of a paper by OpenAI in 2018 called *Improving language understanding by generative pretraining*

GPT has 96 transformers and 175 billion parameters so it is significantly larger than the traditional transformer architecture. However, the GPT architecture is the transformer arcitecture without the encoder. It is just several predictors based on top of each other.

![image](https://github.com/user-attachments/assets/a7d11ce0-49f7-43f6-b9c8-f32ccb5d48b0)

The ability of GPT to perform a task that it wasn't explicitly trained to do is referred to as an **emergent behavior**.

This book seeks to use the following architecture for teaching how to build an LLM without the thousand dollar price tag usually associated with pretraining an llm.

![image](https://github.com/user-attachments/assets/258bb856-1048-43e3-98ba-81ec0ecd6a59)

# Chapter 2: text encoding 

embedding is converting one data type to a vector representation. It's important to note that different embedding models will not work for other data types so a video encoder will not work for text.
retreival augmented generation is a technique combining generating text with a retrieval corpus like an external knowledge base.

1. Build a tokenizer that will seperate all words and special characters
2. Match the string tokens into IDs. first we build a vocabulary. Each unique token is put into a mapping and assigned an integer ID. In order to build the vocabulary and enable the model to act on untrained data, we'll want to have a large and diverse corpus of data
3. we often extend the vocab list to include special tokens like unk and eof
4. byte pair encoding is a strategy used to encode new words where the algorithm will attempt to break the unknown word into subwords
5. we want to build a data loader which can use input target pairs to train the data. For this, we'll take an ecoding of the words in order and tell the machine that the predicted word is the next word in the corpus. We do this because the LLM is essentially a large next word prediction model. since the targets are shifted by 1 (or any amount that we specify), we sometimes refer to this as a sliding window approach. the reason that we may increase the slide value is to prevent the model from overfitting.
6. an embedding layer from tensorflow or pytorch is then used to convert the token IDs into seemingly random tensors

