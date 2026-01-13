As a recap, the sigmoid function will be the following where we can ensure that if z is a large positive number, the sigmoid will be close to 1 and if z is a large negative number, the sigmoid will be close to zero.
<img width="3700" height="1029" alt="image" src="https://github.com/user-attachments/assets/ae9d6b88-fab6-4afd-a786-adb8db66d1f7" />

Remember that W is an $n_x$ dimensional vector and b is a real number

## Cost function

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
