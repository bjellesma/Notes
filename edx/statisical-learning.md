# Intro

**Supervised Learning** can be thought of a teacher showing pictures of houses and bikes to a kindagardener and the kid starts to learning that the houses have sharper edges whereas bikes are more rounded edges. In this example, we're using **labeled** data. **Unsupervised Learning** can be thought as just seeing these things through daily experience and recognizing patterns. One of the challenges of unsupervised learning techniques such as **clustering** is that you don't really have a very good indication of how well you're doing. This means that unsupervised learning can be a good preprocesser for supervised learning because it's a lot more common to have unlabeled data if you think about going on the internet.

**Machine Learning** can be thought of as a subfield of Artificial intellegence and has a greater emphasis on prediction accuracy. **Statistical Learning** can be thought of as a subfield of statistics and emphasizes models and their interpretability.

# Regression models

Rgression Function will have both a **reducible** part which is the function of x and the **irreducible** part which is the error in preduction. To deal with the irreducible part of the function, we will have take an average which is known as the neighborhood of values

![image](https://github.com/user-attachments/assets/fa2d5c99-b180-4b43-8630-c8d07689e5e3)

If you draw a line through the data, the distance between the line and each data point is known as a **residual** . The idea with using the linear regression method known as **least squares** is that you for each rotation of the line, you'll sum up the square of each residual point. From here, you want to take the least of these sums. The rotation of the line that yielded that sum will be used to fit the data. 

![image](https://github.com/user-attachments/assets/f8582c74-4d0d-485e-8596-463c622238f4)

![image](https://github.com/user-attachments/assets/da443dc7-3eab-484e-b7b4-31592e538c15)
