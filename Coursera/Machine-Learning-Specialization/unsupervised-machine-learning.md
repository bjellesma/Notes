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

The challenge comes into play with finding a w and b parameter that'll fit for all indices of $\hat{y}^{(i)} = wx^{(i)} + b$ . This is where we want to use a **cost function** where we can measure the distance between $\hat{y} and y$. One example of that would be to take the sum of all of the square of all of these distances, $J(w,b) = \frac{\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})^{2}}{2m}$ where m is the number of training examples, $\hat{y}^(i)$ or $f_{w,b}(x^{(i)}$ is the value of the line that we're proposing, and $y^{(i)}$ is the actual value. This function specifically is referred to as the **squared error cost function**

![image](https://github.com/user-attachments/assets/a9776602-91ee-406a-a5a6-9c9e8cfb3b18)

Our goal is that we want $J(w,b)$ to be as small as possible so we want to find the best possible values of w and b to accomplish this. Mathematically, we write this as $\min_{w,b} J(w,b)$. A strategy for this is that we can look at only one of these parameters at a time. So if look at only w, our cost function will become $J(w) = \frac{\sum_{i=1}^{m} (f_{w}(x^{(i)}) - y^{(i)})^{2}}{2m}$ where $f_w(x) = wx$ which means that the line is just now passing through the origin since there is no y intercept.

![image](https://github.com/user-attachments/assets/a358768c-8a13-45c8-be39-30a659a65098)

Intutively, the idea is that the cost function will be the distance between the estimated w value and the actual y value. So a line y=x where it goes through every data point perectly will have a cost function of 0. So, let's use w=1 in the following table.

| $f_w(x)^{(i)}$ | $y^{(i)} |
|----------|----------|
| 1 | 1
| 2 | 2
| 3 | 3

$J(w) = \frac{\sum_{i=1}^{m} (f_{w}(x^{(i)}) - y^{(i)})^{2}}{2m}$ = $J(w) = \frac{(1-1)^2 + (2-2)^2 + (3-3)^2}{2m}$ = $0$

![image](https://github.com/user-attachments/assets/9d8c26d2-ece0-469f-87b6-8505019321de)

Now, let's look at that same example but use w=0.5

| $f_w(x)^{(i)}$ | $y^{(i)} |
|----------|----------|
| 0.5 | 1
| 1 | 2
| 1.5 | 3

$J(w) = \frac{\sum_{i=1}^{m} (f_{w}(x^{(i)}) - y^{(i)})^{2}}{2m} = \frac{(.5-1)^2 + (1-2)^2 + (1.5-3)^2}{2m} = \frac{.25 + 1 + 2.25}{2m} = \frac{3.5}{2 * 3} = \frac{3.5}{6} \approx{.58}$ 

![image](https://github.com/user-attachments/assets/fd651fa6-e84a-42a2-ad0e-6a24fc99ca94)

Now, let's look at that same example but use w=0

| $f_w(x)^{(i)}$ | $y^{(i)} |
|----------|----------|
| 0 | 1
| 0 | 2
| 0 | 3

$J(w) = \frac{\sum_{i=1}^{m} (f_{w}(x^{(i)}) - y^{(i)})^{2}}{2m} = \frac{(0-1)^2 + (0-2)^2 + (0-3)^2}{2m} = \frac{1 + 4 + 9}{2m} = \frac{14}{2 * 3} = \frac{14}{6} \approx{2.3}$ 

![image](https://github.com/user-attachments/assets/eb710950-e080-42c1-96de-30ded01dbe41)

So if we plot each cost function at a different value of w, we see that w=0, we get the the smallest cost function. Notice that the cost function is usually parabolic

![image](https://github.com/user-attachments/assets/c92bafb9-4f43-4e7c-9289-7c9d331e0012)

In order to introduce back the y intercept, b, back into this equation, what we want to is to make a **countor plot**, a graph to view three dimensional data only using three axes. To make this plot, what we'll do is to first make a 3d plot by introducing the z axis and then we'll take slices of that to be the different countours. The idea is that each value for b and w on the countour plot will be the same value for J. You want to choose the inmost countour to have the minimum value. To think of this conceptually, what we can do is think of the different countours of a mountain. The inmost countour is going to be the highest point on the mountain.

![image](https://github.com/user-attachments/assets/1cc2e0fb-e63e-4b8a-8073-f7830cf615ea)

To give an example, here is how we can visualize choosing the minimum by doing a countour plot. By looking for the minimum countour, we can see that the point corresponds to w=0.13 and b corresponds to b=71. This will give us the function $f(x) = 0.13x+71$. If we plot that line now on our actual chart of price vs size of house, the line is actually a decent fit for the data with the errors between the predicted and actual values not being that bad.

![image](https://github.com/user-attachments/assets/501a1ff5-b929-41fa-a6e0-1e550b979600)

Keep in find that once you find the values on the countour plot that you want to use, you can still plot these values on the price vs size chanrt to check that you are getting the expected values.

![image](https://github.com/user-attachments/assets/19d5ef55-8710-4207-8b2c-dcf252d6700c)

# Gradient Decent

**Gradient Descent** is used in much of machine learning but it is common in linear regression to find the local minima and has mathematical roots in vector calculus for finding minima in optimization problems. Coceptually think of this as standing on a curvey golf course and we want to find the quickest path to get to the lowest valleys. Gradient descent will find the best vector at that point to get to the next countour to eventually get to the local minima. This becomes very useful in linear regression models as the objective is to minimize the cost function, which is essentailly an optimization problem. 

![image](https://github.com/user-attachments/assets/a6882bcf-088b-441a-805a-7e1c4d8ecf27)

Gradient Descent can be used in linear regression to find the best possible w by $w = \alpha (\frac{d}{dw}J(w,b))$ where $\alpha$ is the learning rate. We can think of the derivative term as give us the direction of the vector while the learning rate gives us the magnitude of the vector. What we want to do with gradient descent is that we want the values of w and b to converge so we take a loop of four steps:

1. $tmp_b = \alpha (\frac{\partial}{\partial b}J(w,b))$
2. $tmp_w = \alpha (\frac{\partial}{\partial w}J(w,b))$
3. $ w = tmp_w$
4. $b = tmp_b$

Notice above that we're calculating the above two partial derivates first and then setting the temp values as the new variables. A common mistake is to perform one derivative and then immediately update the variable which ends up failing when we're calculating the next derivate.

<img width="1737" alt="image" src="https://github.com/user-attachments/assets/883479d5-b3bd-4df1-a055-db017d87b2fc">

In gradient descent assuming that $\alpha$ is a positive number, if we have a negative slope every update step will increase the value of w and if slope is positive, every step will decrease slope. This is because if the deveritive is negative, the subtraction sign in the equation will turn positive and if the deveritivat is positive, we will be still subtracting.

![image](https://github.com/user-attachments/assets/86dd25e9-4f0b-48e6-bc47-484865e29b79)

## Chosing a learning rate

As describe in the previous section, the learning rate is the value that you multiply the derivate by. This value is an important consideration because if the value you choose is too small, the steps of the algo will be too slow and may never reach the minum or, at best, be too computationally expensive. If the value that you choose is too large, then it may overstep the local minimum and fail to every converge.

![image](https://github.com/user-attachments/assets/1fde218a-7e62-41b6-b633-896204010e6a)

When we say that it converges to 0, we mean that the slope of the tangent line at that point is 0 which makes the derivate 0 which means $w=w$

![image](https://github.com/user-attachments/assets/3452ba0c-41d7-4774-9b98-036e54a01716)

For a fixed learning rate, the derivative will automatically get smaller and smaller at each step because the slope is getting smaller and smaller each time.

![image](https://github.com/user-attachments/assets/5f3e937c-c39e-4cc5-aa21-21244e60b6b4)

A version of the Squared Error Cost Function equation can actlly be derived from the devative gradient descent. For this reason, we can actually remove the derivates in the gradient descent and use

$w = w - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})(x^{(i)})$

$b = b - \alpha \frac{1}{m}\sum_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})$

Notice that the equation for w is multiplied by the x term because in the original univariate linear regression, w is multipled by x. Notice also that the squared term is gone in both equations because of using the exponent rule in calculus and dividing the denominator by 2 cancels the 2 in the denominator of the coefficient.

![image](https://github.com/user-attachments/assets/0d99be4c-0b6d-40d0-b434-9a1ad0633f57)

The last part of gradient descent to cover is that depending on the starting values that you choose, you might hit a local minimum rather than the global minimum.

In code, keep in mind that we need to use initial values for w and b. These are typically chosen a (0,0).

```python
def gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function): 
    """
    Performs gradient descent to fit w,b. Updates w,b by taking 
    num_iters gradient steps with learning rate alpha
    
    Args:
      x (ndarray (m,))  : Data, m examples 
      y (ndarray (m,))  : target values
      w_in,b_in (scalar): initial values of model parameters  
      alpha (float):     Learning rate
      num_iters (int):   number of iterations to run gradient descent
      cost_function:     function to call to produce cost
      gradient_function: function to call to produce gradient
      
    Returns:
      w (scalar): Updated value of parameter after running gradient descent
      b (scalar): Updated value of parameter after running gradient descent
      J_history (List): History of cost values
      p_history (list): History of parameters [w,b] 
      """
    
    # An array to store cost J and w's at each iteration primarily for graphing later
    J_history = []
    p_history = []
    b = b_in
    w = w_in
    
    for i in range(num_iters):
        # Calculate the gradient and update the parameters using gradient_function
        dj_dw, dj_db = gradient_function(x, y, w , b)     

        # Update Parameters using equation (3) above
        b = b - alpha * dj_db                            
        w = w - alpha * dj_dw                            

        # Save cost J at each iteration
        if i<100000:      # prevent resource exhaustion 
            J_history.append( cost_function(x, y, w , b))
            p_history.append([w,b])
        # Print cost every at intervals 10 times or as many iterations if < 10
        if i% math.ceil(num_iters/10) == 0:
            print(f"Iteration {i:4}: Cost {J_history[-1]:0.2e} ",
                  f"dj_dw: {dj_dw: 0.3e}, dj_db: {dj_db: 0.3e}  ",
                  f"w: {w: 0.3e}, b:{b: 0.5e}")
 
    return w, b, J_history, p_history #return w and J,w history for graphing
```

```python
# initialize parameters
w_init = 0
b_init = 0
# some gradient descent settings
iterations = 10000
tmp_alpha = 1.0e-2
# run gradient descent
w_final, b_final, J_hist, p_hist = gradient_descent(x_train ,y_train, w_init, b_init, tmp_alpha, 
                                                    iterations, compute_cost, compute_gradient)
print(f"(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})")
```

```
Iteration    0: Cost 7.93e+04  dj_dw: -6.500e+02, dj_db: -4.000e+02   w:  6.500e+00, b: 4.00000e+00
Iteration 1000: Cost 3.41e+00  dj_dw: -3.712e-01, dj_db:  6.007e-01   w:  1.949e+02, b: 1.08228e+02
Iteration 2000: Cost 7.93e-01  dj_dw: -1.789e-01, dj_db:  2.895e-01   w:  1.975e+02, b: 1.03966e+02
Iteration 3000: Cost 1.84e-01  dj_dw: -8.625e-02, dj_db:  1.396e-01   w:  1.988e+02, b: 1.01912e+02
Iteration 4000: Cost 4.28e-02  dj_dw: -4.158e-02, dj_db:  6.727e-02   w:  1.994e+02, b: 1.00922e+02
Iteration 5000: Cost 9.95e-03  dj_dw: -2.004e-02, dj_db:  3.243e-02   w:  1.997e+02, b: 1.00444e+02
Iteration 6000: Cost 2.31e-03  dj_dw: -9.660e-03, dj_db:  1.563e-02   w:  1.999e+02, b: 1.00214e+02
Iteration 7000: Cost 5.37e-04  dj_dw: -4.657e-03, dj_db:  7.535e-03   w:  1.999e+02, b: 1.00103e+02
Iteration 8000: Cost 1.25e-04  dj_dw: -2.245e-03, dj_db:  3.632e-03   w:  2.000e+02, b: 1.00050e+02
Iteration 9000: Cost 2.90e-05  dj_dw: -1.082e-03, dj_db:  1.751e-03   w:  2.000e+02, b: 1.00024e+02
(w,b) found by gradient descent: (199.9929,100.0116)
```

Notice in each of the above iterations that the derivatives also get smaller. If we also plot the cost function vs the number of iterations, we also notice it decreasing.

<img width="771" alt="image" src="https://github.com/user-attachments/assets/d148375f-6077-46e9-8f6d-07103a50d32b">

Before we discussed that if $\alpha$ is too large, then it will continuously overshoot the local minimum. Here's an example in code.

```python
# initialize parameters
w_init = 0
b_init = 0
# set alpha to a large value
iterations = 10
tmp_alpha = 8.0e-1
# run gradient descent
w_final, b_final, J_hist, p_hist = gradient_descent(x_train ,y_train, w_init, b_init, tmp_alpha, 
                                                    iterations, compute_cost, compute_gradient)
```

```
Iteration    0: Cost 2.58e+05  dj_dw: -6.500e+02, dj_db: -4.000e+02   w:  5.200e+02, b: 3.20000e+02
Iteration    1: Cost 7.82e+05  dj_dw:  1.130e+03, dj_db:  7.000e+02   w: -3.840e+02, b:-2.40000e+02
Iteration    2: Cost 2.37e+06  dj_dw: -1.970e+03, dj_db: -1.216e+03   w:  1.192e+03, b: 7.32800e+02
Iteration    3: Cost 7.19e+06  dj_dw:  3.429e+03, dj_db:  2.121e+03   w: -1.551e+03, b:-9.63840e+02
Iteration    4: Cost 2.18e+07  dj_dw: -5.974e+03, dj_db: -3.691e+03   w:  3.228e+03, b: 1.98886e+03
Iteration    5: Cost 6.62e+07  dj_dw:  1.040e+04, dj_db:  6.431e+03   w: -5.095e+03, b:-3.15579e+03
Iteration    6: Cost 2.01e+08  dj_dw: -1.812e+04, dj_db: -1.120e+04   w:  9.402e+03, b: 5.80237e+03
Iteration    7: Cost 6.09e+08  dj_dw:  3.156e+04, dj_db:  1.950e+04   w: -1.584e+04, b:-9.80139e+03
Iteration    8: Cost 1.85e+09  dj_dw: -5.496e+04, dj_db: -3.397e+04   w:  2.813e+04, b: 1.73730e+04
Iteration    9: Cost 5.60e+09  dj_dw:  9.572e+04, dj_db:  5.916e+04   w: -4.845e+04, b:-2.99567e+04
```

<img width="874" alt="image" src="https://github.com/user-attachments/assets/d8e462c1-46d7-4e32-aa4a-8d5b6ca28fef">
