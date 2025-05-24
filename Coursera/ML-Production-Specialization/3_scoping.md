Scoping is all about deciding what project to work on. When deciding, it's important to consider factors such as what are the metrics that the business is looking for and what are the resources that we have (data, time, and people).

When trying to brainstorm ideas with the business on what to work on. The first thing we want to ask is what are the business problems that the business wishes to solve. Maybe the problem is that they want more visitors to the website to be converted to customers or maybe they want to reduce the amout of inventory that they keep in the warehouse. It's important to focus on asking problems that the business is facing because then we'll determine if ML is even the correct approach.

Once you've brainstormed some ideas that you think ML would be applicable for, it's useful to think about the feasibility of the project. In the screenshot below, this is divided between unstructured data and structured data. with unstructured data such as audio clips and images, it's useful to think about the human level performance. Beecause if a human can't even perform this task, then it's not feasible to develop an ML algo to do this. When looking at structured data like spreadsheet records, we want to identify any features such as spreadsheet columns that may be useful for making possible predictions such as a revenue as time series column.

![image](https://github.com/user-attachments/assets/8bfc6e60-6bba-4e88-a04f-783d30571d18)

Human level performance on unstructured data has a good example in computer vision. In the images below, the first one is easy to see what color the stop light is whereas the second image is ambiguous. Maybe with the second image, it's possible for a human to assess it when they're in their car and close the stop light but a computer vision algo is only going to have access to the images from far away so you'll need to compare HLP at that point.

Andrew gives us an example of how an ML team spent months on a computer vision problem only to figure out that the images were ambiguous and the human couldn't even tell what was happening.

![image](https://github.com/user-attachments/assets/1d50046d-5935-4692-8349-fa923c3d5e69)

When looking at structured data, we really want to look at the mapping from the input x to the output y. In the first example below, if we have the user's past purchase history it's reasonable to say that we have a decently clear mapping to predict future prices. In start contrast, the last example of having a stock's previous price is not a good indication of the future price of that stock because the stock market has so many variables and no human can even predict it.

![image](https://github.com/user-attachments/assets/8485c38e-e7de-449b-8c8a-70e467c009c9)

Finally for feasability assessment, it's also useful to look at the history of the same existing project that we want to work on. In the screenshot below, we've plotted out the error analysis vs time. If we notice that we've been able to reduce errors by 30% each quarter relative to HLP, it's feasible to think that we can reduce that error by the same amount in a similar timeframe.

![image](https://github.com/user-attachments/assets/514293a2-d6a9-4763-a592-88b771d23e65)

One final note is there is often a gap between the metrics that the ML team cares about like accuracy and the metrics that the business cares about such as revenue. When performing feasability, it's often useful to first see if we can bridge the gap between the ML team and the business leaders so that the understanding is well understood and agreed upon. For example, how much is improving word level accuracy going to connect to the revenue stream?

Once we've determined is an ML solution is even applicable to the business problem, then we can begin setting milestones and discussing budget.


![image](https://github.com/user-attachments/assets/02db6126-ba05-4895-9a64-f4d6d62df722)

