Training a tokenizer is different from training a model in that the tokenizer is trained by having a statistical analysis run over the corpus of text to build a vocabulary. There are no gradients or loss functions used when training a tokenizer as there is with training a model. 

Because of this difference, Huggingface has a seperate tokenizers library for tokenizers training.

