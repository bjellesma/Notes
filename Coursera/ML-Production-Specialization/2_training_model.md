## Key Challenges

Before tackline key challenges, it's useful to establish the difference between a data-centric and model-centric approach to ML development. **data-centric** indicates that the model architecture remains fixed and we only work on the data whereas a **model-centric** approach indicates that we hold the data fixed and work on the model.

The Key Challenge is that model development is an iterative process whereas you should constantly be performing error analysis

![image](https://github.com/user-attachments/assets/4af02982-d72c-42bf-85c8-a01696936f07)

While auditing performance by utilizing error analysis, it's important to note that the algorithm should perform well first on the training set before even evaluating it on the test set.

Furthermore, it's important to recognizw what's acceptable and what's not acceptable for training an ML in a business. Having a low average error might not be good enough because some metrics are weighted more heavily by the business. Andrew gives the example of a web search. If a user searches directly for something like an apple pie receipe and doesn't get the best one, the user would be more likely to be forgiving. But if a user searches for something like Standford and doesn't get standford.edu, the user will quickly lose trust. For this reason, even though the error rate might be low on average, if the ML algorithm misses an important example, this may not be acceptable.

![image](https://github.com/user-attachments/assets/4ac58dd3-bc7d-410b-90c5-53e16f103e95)

Another key challenge is how well the ML algo performs on key slices of the dataset. As one example, you want to make sure that a loan approval algo doesn't start discriminating and treats everyone fairly.

![image](https://github.com/user-attachments/assets/b8db89dc-ffd2-49e9-83ef-77448ddc048e)

A third key challenge is having rare cases that don't translate well into the real world. For example, Andrew tells us about a time that he was working a medical diagnosis app. There weren't many cases of a Hernia in the training set so that algo misdiagnosed this in a test set. So even though the algo performed well on the vast majority of cases, it failed to recognize the rare case of a hernia. This is something that is easily diagnosed by a human so the algo doesn't quite work.

![image](https://github.com/user-attachments/assets/eb74a9b4-2afc-4b86-872e-e040b4c5aa26)

## Establishing a baseline

When evaluating performance, a useful technique may be to compare the algo's performance against human level performance. The benefit of this is when you look at cases where the algo's performance is low, you may not need to focus your efforts there if the human level performance is also bad. Instead, it may be more worth your efforts to focus on other areas where the algo's performance is significantly lower than human performance.

![image](https://github.com/user-attachments/assets/658091cd-7ecc-4beb-9cbb-80c7a220fcd2)

Usually Human level performance is better with unstructured data such as audio files and image files so it is a good comparison. Structured data such as spreadsheets are usually more difficult for a human to digest and make predictions on so human level performance is typically not a great indicator of a baseline.

