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
