The Key Challenge is that model development is an iterative process whereas you should constantly be performing error analysis

![image](https://github.com/user-attachments/assets/4af02982-d72c-42bf-85c8-a01696936f07)

While auditing performance by utilizing error analysis, it's important to note that the algorithm should perform well first on the training set before even evaluating it on the test set.

Furthermore, it's important to recognizw what's acceptable and what's not acceptable for training an ML in a business. Having a low average error might not be good enough because some metrics are weighted more heavily by the business. Andrew gives the example of a web search. If a user searches directly for something like an apple pie receipe and doesn't get the best one, the user would be more likely to be forgiving. But if a user searches for something like Standford and doesn't get standford.edu, the user will quickly lose trust. For this reason, even though the error rate might be low on average, if the ML algorithm misses an important example, this may not be acceptable.

![image](https://github.com/user-attachments/assets/4ac58dd3-bc7d-410b-90c5-53e16f103e95)
