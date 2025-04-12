A second type of unsupervised learning is anomaly detection where we find data points that are outside of the data that we've found earlier.

![alt text](image-113.png)

In the above screenshot, our datapoint $x\sub{test} looks like it has a high specific heat and low vibration intensity. Given that the plotted datapoint looks very different than many other datapoints, this would lead us to conclude that we would want to have further testing before installing that engine in an aircraft.

One algorithm for detecting anomalous behavior is called **Density Estimation** where we assign a probability to all points in a dataset of being anomalous. All of the points are plotted on a scatter plot and then further datapoints can be assigned a probability of where they would appear on that scatter plot. If the datapoint would land more toward the center of the scatter plot, it would be assigned a high probability and therefore has a higher chance of being ok. In contrast, a datapoint plot further outside would be assigned a low probability and is therefore more likely to be an anomaly. We make the classification by using a number, $\epsilon$, to represent the threshold of what determines ok vs anomaly.

![image](https://github.com/user-attachments/assets/1d4e98ba-4297-4cea-a20d-63321a648e34)

A common use case for density estimation specifically is in fraud detection. You may have features like how often the user logs in or how many transactions the user makes and model that on a scatter plot to assign a probability. This probability can then be used with a threshold that you assign to determine is the activity should be flagged as anomalous or not. If something is flagged as anomalous, it can be an indicator that maybe the security team should take a further look at this account to determine if the behavior is fradulant or just a false alarm.

![image](https://github.com/user-attachments/assets/227b8e9d-2b2c-46b0-a219-04843bf63911)
