# Supervised Learning

Examples of supervised machine learning would be taking an input such as email and expecting an output such as whether it's spam. This is an application called **spam filtering**. Other examples are found below.

| input | Output | Application |
| ----- | ------ | ------------|
| audio | transcripts | speech recognition |
| english | spanish | machine translation |
| ad | will the user click based on profile | online advertising |
| image, radar | position of other cars | self driving |
| image of item | detection of defect (0/1) | visual inspection |

One more concretely visual example would be predicting the cost of a house based on the square footage. You can use a straight line to try to fit in the data or use a slightly complex more curved line. An ML algorithm may tell you the best method to use. This is supervised ML because we gave the algorithm the correct price or labels for the data.

![image](https://github.com/user-attachments/assets/97af4301-604e-4c03-96d4-bb4d23703e86)

Contrary to what you may think, classification algorithms can actually have more than two possible categories though two is more common. What makes this very different from regression models where you're attempting to fit a line on a graph where a line can have an infinite number of values is that classification algorithms have a very small number of possible output. So in the case of a cancer diagnosis, a tumor can be benign, malignant type 1, or malignant type 2 

![image](https://github.com/user-attachments/assets/d19f487d-f698-485e-a7c4-47c1a39618df)

In Summary, the two main types of **supervised learning** are regression and classification. The difference between these two is mainly the number of outputs. Regression is predicting a large number of outputs because this is often drawing a line to a graph and a line is continuous so it can have an infinite number of outputs whereas classification is predicting categories which are generally only a small number of possible classifications. The main differentiation of supervised vs unsupervised learning is that supervised learning is fascilitated by giving the algorithm the right answer so that it can learn to identify on its own based on the inputs given. An example of supervised would be spam filtering because we give the algorithm correctly marked spam in order so that it can classify it.

During training of spam filtering, we give the algorithm a dataset of **labeled** (already correctly classified) data and from that it can learn to recognize certain **features** like specific words or the length of the email address used in order to act on new unseen data.

![image](https://github.com/user-attachments/assets/10c1eb00-4c60-466a-9bd6-469ad11dac1c)

# Unsupervised Learning

The main difference with **Unsupervised Learning** is that we're not giving the algorithm any labeled data to train it and insteading we're leaving it up to the algorithm to be able to find patterns in the data itself. 

<img width="1888" alt="image" src="https://github.com/user-attachments/assets/57e22fae-1773-4d17-8b40-5c46bdab58db">

**Clustering** is a particular type of algorithm in unsupervised learning where the algorithm is actually clustering data together based on some patterns or similar features that it finds.

![image](https://github.com/user-attachments/assets/89dfe4bd-0a84-4733-92be-0199b798fc65)

Google news is an example of a clustering algorthm because it will group together stories with similar features. In the case of Google news, it is grouping together stories based on the feature of the headline. In the below particular example, it is grouping based on the word panda being in the headline. The words twin and zoo also appear in the headlines

![image](https://github.com/user-attachments/assets/412ab767-1a6f-46aa-afe6-8e606fb5569e)

Another example of unsupervised learning is looking at a dna array. This heatmap shows the genetic predisposition for each gene  by person where the genes are the rows and the individuals are the columns. This is a good example because we can't really tell the algorithm anything about the data in advance and we're just giving the algorithm a set of data and asking it to find patterns on its own. In this exmple, the algorithm begins finding similar features and grouping them by type. I think an analogous example would be if your boss just gives you a big set of books and asks you to find any patterns and group them by any pattern that you wish. In that analogous example, we're clustering the data together based on the features that we find on our own.

Two other types of algorithms used widely in unsupervised learning are **anomaly detection** where the goal is to find unusual data points based on other features (this is used widely in the financial industry for fraud detection) and **Dimensionality Reduction** where the goal is to compress the data down to fewer data points. Dimensionality reduction is really more of a preprocessing step to reduce features and therefore make the next algorithm used not be as computationally expensive. For example, image recognition often has a large set of features (in the 1000s) due to the number of pixels. The goal of dimensionality reduction would be to find the most relevant set of features so that the number of features might be reduced to something like 50. 

![image](https://github.com/user-attachments/assets/9c11df5e-154a-4220-9f87-242c91d3dafb)


Think of dimensionality reduction to something like studying for an exam. You might have textbooks, lecture notes, recordings, etc. You employ dimensionality reduction when you attempt to distill only the most relavent details from the text rather than memorize every single detail which is overwhelming.

## Linear Regression

![image](https://github.com/user-attachments/assets/fc24b4f5-07ac-4ab2-9caa-25d9c42fe919)


![image](https://github.com/user-attachments/assets/e0e695d9-b574-44c9-98b9-ca7e2ef7c1ac)


Unsupervised learning with one variable is often call **Univariate Linear Regression**. Think of plotting two points and finding the slot intercept equation of the line.

You can think of linear regression as finding the slope intercept form whereas you can use $y_2 - y_1 = m(x_2 - x_1)$. In the context of machine learning, the slope intercept formula applied to linear regression is typically looked as $f_{w,b}(x) = wx+b$ where w and b are both referred to as the **weights** that you can adjust in order to better fit the model. $f_{w,b}(x)$ can sometimes be referred to as $\hat{y}$. And just a reminder that we'll often use the superscipt i to refer to the index (the specific value being plotted) so $\hat{y}^{(i)} = wx^{(i)} + b$

# Cost Function

![image](https://github.com/user-attachments/assets/d928b397-59ce-43a7-9860-d0596955ee39)


