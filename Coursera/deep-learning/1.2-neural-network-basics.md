As a recap, the sigmoid function will be the following where we can ensure that if z is a large positive number, the sigmoid will be close to 1 and if z is a large negative number, the sigmoid will be close to zero.
<img width="3700" height="1029" alt="image" src="https://github.com/user-attachments/assets/ae9d6b88-fab6-4afd-a786-adb8db66d1f7" />

Remember that W is an $n_x$ dimensional vector and b is a real number

## Cost function

In machine learning, you often use the natural log. This is what numpy uses.

A **Loss function** applies to one training example whereas a **cost function** is more generalized and will apply to the entire set.

<img width="3748" height="964" alt="image" src="https://github.com/user-attachments/assets/630dfbd1-f724-469e-9ac2-bc77a1fbfc62" />

A rudimentary approach to the loss function is to use room mean squared error but this is difficult because the resulting graph will have multiple local maxima (non convex) but gradient descent will not be able to find a global maxima.

<img width="3616" height="338" alt="image" src="https://github.com/user-attachments/assets/91e1ab75-8d80-4adc-bb86-7ef756bcdbf5" />

Using the earlier approach will logarithms will result in a convex function where gradient descent can find the global minima (the value to minimize the cost) more easily.

<img width="1828" height="931" alt="image" src="https://github.com/user-attachments/assets/d84a8ca1-2f52-4fe3-8af2-9784d347a52a" />

## Gradient Descent

**Gradient Descent** works by taking a step in the steepest downhill direction.

<img width="2015" height="932" alt="image" src="https://github.com/user-attachments/assets/10ddd264-edca-49b8-8252-ccc4316b8bb1" />

Gradient Descent is implemented by repeatedly taking the partial derivative of the cost function to update the values for w and b. Keep in mind that $\alpha$ is the learning rate and is a parameter that we can tune.

<img width="3676" height="1930" alt="image" src="https://github.com/user-attachments/assets/e82edb2f-1bf7-4e81-be36-ccbf75499401" />

## Forward and Back Propogation

Computations of a neural network are organized in terms of a **forward propogation** where we compute the output of a neural network and a **back propogation** in which we compute the gradients. 

One step of backward propogation on a computation graph yields derivative of final output variable.

A **computation graph** is a visual map that shows how math operations connect together, like a recipe with steps.<img width="1590" height="359" alt="image" src="https://github.com/user-attachments/assets/dfccc372-1418-47cf-b90a-e315576bb730" />

Think of it like tuning a sound mixer:

Inputs: The musicians (you can't change their instruments)
Weights: The volume knobs and EQ settings
Output: The final mixed song (currently sounds bad)
Backpropagation: Tells you exactly which knobs to turn and by how much to make the song sound better

So backpropagation is really about learning the right parameters, not about measuring input importance. Though once trained, you could analyze the learned weights to understand feature importance - but that's a different analysis!

Take the following example:

<img width="1720" height="672" alt="image" src="https://github.com/user-attachments/assets/109b2101-f7aa-4d08-bfe1-bc10ffac534b" />


The value of J can be factored like so. Notice we're factoring out (b+c)

```
J = a(b + c) - (b + c)
J = (a - 1)(b + c)
```

## Vectorization

**Vectorization**  is eliminating explicit Python for-loops by expressing operations as array/matrix operations that NumPy (or similar libraries) can execute using optimized, parallelized C/Fortran code under the hood. <img width="2073" height="954" alt="image" src="https://github.com/user-attachments/assets/70844dff-fd61-4b20-b21c-30ace9669ba4" />

```python
import numpy as np

# Non-vectorized (slow)
f = 0
for j in range(n):
    f += w[j] * x[j]

# Vectorized (fast)
f = np.dot(w, x)
```

Both compute the same result, but the vectorized version:

* Avoids Python's interpreter overhead for each iteration
* Leverages CPU-level parallelism
* Uses highly optimized compiled code

In testing, vectorization can speed up code by about 300x. Vectorization can be done with or without a GPU.

Basic rule of thumb is that whenever you're tempted to write a for loop, check if there's a vectorized version that you can do with numpy.

Let's say that we have m training examples and we want to compute the forward propogation step, we can simply use vectorization with numpy to compute all of these at once. This works because we can put w and x into matrices. <img width="1902" height="886" alt="image" src="https://github.com/user-attachments/assets/c4a5e755-4736-4523-bdc0-c04df297f77a" />

Notice here how you can implement both the forward and back propogation steps using vectoriztion. Notice that even with vectorization, you still need a for loop to go over the total number of iterations. <img width="2212" height="989" alt="image" src="https://github.com/user-attachments/assets/89a3b1e3-ee2f-4191-a655-d330d11fc84d" />

## Broadcasting in python

**Broadcasting** is when you're performing matrix math and the other factor(s) is/are made to match the dimensions of the larger factor <img width="2231" height="1070" alt="image" src="https://github.com/user-attachments/assets/f6980a34-7b5d-4089-93f8-9ac376c31ef0" />

More generally, Broadcasting is when NumPy automatically expands the smaller array to match the larger one so element-wise operations work. Keep in mind that broadcasting is a numpy concept and is not in linear algebra. Linear algebra is more strict.

* Matrix addition: both must be same shape
* Matrix multiplication: inner dimensions must match

## Programming Assignment

One technique often used in gradient descent is normalization. **normalization** of a vector is dividing it by its norm so that you're converting it to a unit vector — a vector that points in the same direction but has length 1. This preserves the direction (the relative relationships between features) while standardizing the magnitude. 

Without normalization, features can have wildly different scales. If one feature ranges from 0-1 and another from 0-10,000, the loss landscape becomes elongated and steep in some directions. Gradient descent ends up taking inefficient zigzag paths toward the minimum. After normalization, the landscape is more spherical, so gradient descent can take a more direct path.

```python
import numpy as np

x = np.array([3, 4])

# The L2 norm (Euclidean length)
norm = np.linalg.norm(x)  # sqrt(3² + 4²) = 5

# Normalized vector
x_normalized = x / norm  # [0.6, 0.8]

# Verify it's now a unit vector
np.linalg.norm(x_normalized)  # 1.0
```

```python
x = np.array([
    [0, 3, 4],
    [2, 6, 4]
])
norm = np.linalg.norm(x, axis=1, keepdims=True)
```



This computes the L2 norm (Euclidean length) for each row. Note that we normalize row wise. This comes from the definition in linear algebra and is useful for machine learning because we normally use rows to denote samples.

Also note: axis tells NumPy which dimension to collapse when computing the norm — it's an index into the shape tuple, not a size.
For a matrix with shape (2, 3):

axis=0 means "collapse along rows" → compute norm down each column → result shape (3,)
axis=1 means "collapse along columns" → compute norm across each row → result shape (2,)

- **Row 0:** √(0² + 3² + 4²) = √(0 + 9 + 16) = √25 = **5**
- **Row 1:** √(2² + 6² + 4²) = √(4 + 36 + 16) = √56

so norm is a column vector

```python
[[5],
 [√56]]
```
x_normalized = x / norm
```python
Row 0: [0/5,   3/5,   4/5  ] = [0,    0.6,  0.8 ]
Row 1: [2/√56, 6/√56, 4/√56] ≈ [0.27, 0.80, 0.53]
```

$$
\text{softmax}(x) = \begin{bmatrix}
    \frac{e^{x_{11}}}{\sum_j e^{x_{1j}}} & \frac{e^{x_{12}}}{\sum_j e^{x_{1j}}} & \frac{e^{x_{13}}}{\sum_j e^{x_{1j}}} & \cdots & \frac{e^{x_{1n}}}{\sum_j e^{x_{1j}}} \\\\
    \frac{e^{x_{21}}}{\sum_j e^{x_{2j}}} & \frac{e^{x_{22}}}{\sum_j e^{x_{2j}}} & \frac{e^{x_{23}}}{\sum_j e^{x_{2j}}} & \cdots & \frac{e^{x_{2n}}}{\sum_j e^{x_{2j}}} \\\\
    \vdots & \vdots & \vdots & \ddots & \vdots \\\\
    \frac{e^{x_{m1}}}{\sum_j e^{x_{mj}}} & \frac{e^{x_{m2}}}{\sum_j e^{x_{mj}}} & \frac{e^{x_{m3}}}{\sum_j e^{x_{mj}}} & \cdots & \frac{e^{x_{mn}}}{\sum_j e^{x_{mj}}}
\end{bmatrix}
$$

This can be implemented as follows

```python
def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (m,n).

    Argument:
    x -- A numpy matrix of shape (m,n)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (m,n)
    """
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=1,keepdims=True)
    s = x_exp / x_sum
    return s
```

### Flattening Images

A common trick for flattening images is to use 

X_flatten = X.reshape(X.shape[0], -1).T      # X.T is the transpose of X

If X has dimensions (209, 64, 64, 3) representing 209 images of 64x64x3 (3 being the color channels), then X[0].shape is (64,64,3) and X.shape[0] is 209 so X.reshape(X.shape[0], -1) (-1) is a convenience to multiply 64x64x3) will be (209, 12288). Finally, we'll get the Transpose of this which'll flip the dimensions to be (12288, 209). This means that we have 209 rows of 12288 numbers now.

One last note is that the .T is specific to Andrew Ng's course notation where he wants samples as columns. Most ML libraries (sklearn, PyTorch, TensorFlow) expect the opposite — samples as rows, shape (n_samples, n_features).

## Programming Assignment: Image Recognition

```python
def initialize_with_zeros(dim):
    """
    This function creates a vector of zeros of shape (dim, 1) for w and initializes b to 0.
    
    Argument:
    dim -- size of the w vector we want (or number of parameters in this case)
    
    Returns:
    w -- initialized vector of shape (dim, 1)
    b -- initialized scalar (corresponds to the bias) of type float
    """
    w=np.zeros((dim,1))
    b=0.
    return w, b
def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    z -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(z)
    """
    s=1/(1+np.exp(-z))
    return s
def propagate(w, b, X, Y):
    """
    Implement the cost function and its gradient for the propagation explained above

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat) of size (1, number of examples)

    Return:
    grads -- dictionary containing the gradients of the weights and bias
            (dw -- gradient of the loss with respect to w, thus same shape as w)
            (db -- gradient of the loss with respect to b, thus same shape as b)
    cost -- negative log-likelihood cost for logistic regression
    """
    
    m = X.shape[1]
    # forward prop
    A=sigmoid(np.dot(w.T,X)+b)
    cost=-(1/m)*np.sum(Y*np.log(A)+(1-Y)*np.log(1-A))
    
    # back prop
    dw = (1/m)*np.dot(X,(A-Y).T)
    db = (1/m)*np.sum(A-Y)
    
    # YOUR CODE ENDS HERE
    cost = np.squeeze(np.array(cost))

    
    grads = {"dw": dw,
             "db": db}
    
    return grads, cost

dim = 2
w, b = initialize_with_zeros(dim)
grads, cost = propagate(w, b, X, Y)

##### Now we can start using gradient descent by optimizing
def optimize(w, b, X, Y, num_iterations=100, learning_rate=0.009, print_cost=False):
    """
    This function optimizes w and b by running a gradient descent algorithm
    
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of shape (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat), of shape (1, number of examples)
    num_iterations -- number of iterations of the optimization loop
    learning_rate -- learning rate of the gradient descent update rule
    print_cost -- True to print the loss every 100 steps
    
    Returns:
    params -- dictionary containing the weights w and bias b
    grads -- dictionary containing the gradients of the weights and bias with respect to the cost function
    costs -- list of all the costs computed during the optimization, this will be used to plot the learning curve.
    """
    
    w = copy.deepcopy(w)
    b = copy.deepcopy(b)
    
    costs = []
    
    for i in range(num_iterations):
        grads, cost = propagate(w, b, X, Y)
        dw = grads["dw"]
        db = grads["db"]
        
        # update rules
        w = w - learning_rate*dw
        b = b - learning_rate*db
        # Record the costs
        if i % 100 == 0:
            costs.append(cost)
        
            # Print the cost every 100 training iterations
            if print_cost:
                print ("Cost after iteration %i: %f" %(i, cost))
    
    params = {"w": w,
              "b": b}
    
    grads = {"dw": dw,
             "db": db}
    
    return params, grads, costs

params, grads, costs = optimize(w, b, X, Y, num_iterations=100, learning_rate=0.009, print_cost=False)

#### Finally, we can make predictions

def predict(w, b, X):
    '''
    Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b)
    
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    
    Returns:
    Y_prediction -- a numpy array (vector) containing all predictions (0/1) for the examples in X
    '''
    
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    
    A = sigmoid(np.dot(w.T,X)+b)
    
    # YOUR CODE ENDS HERE
    
    for i in range(A.shape[1]):
        if A[0, i] > .5 :
            Y_prediction[0,i] = 1
        else:
            Y_prediction[0,i] = 0
        
        # YOUR CODE ENDS HERE
    
    return Y_prediction

w = np.array([[0.1124579], [0.23106775]])
b = -0.3
X = np.array([[1., -1.1, -3.2],[1.2, 2., 0.1]])
print ("predictions = " + str(predict(w, b, X)))
```

predictions = [[1. 1. 0.]]

Now we can put this together to create and train our model

```python
def model(X_train, Y_train, X_test, Y_test, num_iterations=2000, learning_rate=0.5, print_cost=False):
    """
    Builds the logistic regression model by calling the function you've implemented previously
    
    Arguments:
    X_train -- training set represented by a numpy array of shape (num_px * num_px * 3, m_train)
    Y_train -- training labels represented by a numpy array (vector) of shape (1, m_train)
    X_test -- test set represented by a numpy array of shape (num_px * num_px * 3, m_test)
    Y_test -- test labels represented by a numpy array (vector) of shape (1, m_test)
    num_iterations -- hyperparameter representing the number of iterations to optimize the parameters
    learning_rate -- hyperparameter representing the learning rate used in the update rule of optimize()
    print_cost -- Set to True to print the cost every 100 iterations
    
    Returns:
    d -- dictionary containing information about the model.
    """

    w,b = initialize_with_zeros(X_train.shape[0])
    
    params, grads, costs = optimize(w, b, X_train, Y_train, num_iterations=num_iterations, learning_rate=learning_rate, print_cost=False)
    
    w,b = params["w"], params["b"]
    Y_prediction_test = predict(w=w, b=b, X=X_test)
    Y_prediction_train = predict(w=w, b=b, X=X_train)

    # Print train/test Errors
    if print_cost:
        print("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
        print("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test, 
         "Y_prediction_train" : Y_prediction_train, 
         "w" : w, 
         "b" : b,
         "learning_rate" : learning_rate,
         "num_iterations": num_iterations}
    
    return d

logistic_regression_model = model(train_set_x, train_set_y, test_set_x, test_set_y, num_iterations=2000, learning_rate=0.005, print_cost=True)
```

The call to model takes awhile to run. Here are the acccuracy results

train accuracy: 99.04306220095694 %
test accuracy: 70.0 %

Here you can also plot the cost function to see that the cost is rapidly going down with each iteration.

```python
# Plot learning curve (with costs)
costs = np.squeeze(logistic_regression_model['costs'])
plt.plot(costs)
plt.ylabel('cost')
plt.xlabel('iterations (per hundreds)')
plt.title("Learning rate =" + str(logistic_regression_model["learning_rate"]))
plt.show()
```

<img width="694" height="453" alt="image" src="https://github.com/user-attachments/assets/8fbb43fc-6c7a-400c-87aa-3233100fb0fc" />

In the below screenshot, we will also try using a few different learning rates. The learning rate  𝛼
  determines how rapidly we update the parameters. If the learning rate is too large we may "overshoot" the optimal value. Similarly, if it is too small we will need too many iterations to converge to the best values. That's why it is crucial to use a well-tuned learning rate.

<img width="784" height="442" alt="image" src="https://github.com/user-attachments/assets/4f116e17-f83d-490a-ae96-bcdf2ba3bc98" />

Notice that the learning rate 0.01 tends to ocillate but does eventually converge. Conversely, the learning rate of .0001 is too small so not enough progress is made.
