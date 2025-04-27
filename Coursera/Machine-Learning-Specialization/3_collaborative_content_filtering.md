![image](https://github.com/user-attachments/assets/c9045154-d8f7-4edd-82ee-d65fe6302ec0)

r(i,j) is either 1 or 0. It is 1 is the movie has a rating and 0 if it does not.

Let's use the notation $n_u$ to be the number of users, $n_m$ to be the number of movies, and the $n$ to be the number of features that we have available. In the below table, we can see that we have 

| Movie | Alice(1) | Bob(2) | Carol(3) | Dave(4) | X₁ (romance) | X₂ (action) |
|-------|----------|--------|----------|---------|--------------|-------------|
| Love at last | 5 | 5 | 0 | 0 | 0.9 | 0 |
| Romance forever | 5 | ? | ? | 0 | 1.0 | 0.01 |
| Cute puppies of love | ? | 4 | 0 | ? | 0.99 | 0 |
| Nonstop car chases | 0 | 0 | 5 | 4 | 0.1 | 1.0 |
| Swords vs. karate | 0 | 0 | 5 | ? | 0 | 0.9 |

$$
n_u=4
n_m=5
n=2
$$

Let's also use $x^(i)$ to be the feature matrix of the features that we have. For example, 

$$
x^(3)=
\begin{bmatrix}
   0.99 \\
   0 \\
\end{bmatrix}
$$

because it is a .99 in romance and a 0 in action. Now let's say that we have the following weights (w) and bias (b). We'll use the notation of having superscripts to denote that these are for user 1 (Alice in this case)

$$
w^(1)=
\begin{bmatrix}
   5 \\
   0 \\
\end{bmatrix}
$$

$b^(1)=0$

We would use linear regression

$$ w^{(1)} \cdot x^{(3)} + b 
= \begin{bmatrix} 5 \\ 
0 \\ \end{bmatrix} \cdot \begin{bmatrix} 0.99 \\
0 \\ \end{bmatrix} + 0 
= 5 \times 0.99 + 0 \times 0 + 0 = 4.95 $$

So based on these example weights, we would say that Cute puppies of love is predicted to have a 4.95 rating for Alice.

![image](https://github.com/user-attachments/assets/3f8a4b66-7180-45bc-85a6-92f3826eccd3)

So you can see this is similar to **linear regression** but where each user has their own weights and biases.

The more general form of the recommender system for predicting user j's rating for movie i using linear regression will be $w^(j) \dot x^(i) + b^(j)$

## Cost function

Let's start with some notation

$r(i,j) = 1$ if user $j$ has rated movie $i$ ($0$ otherwise)  
$y^{(i,j)} =$ rating given by user $j$ on movie $i$ (if defined)  
$w^{(j)}, b^{(j)} =$ parameters for user $j$  
$x^{(i)} =$ feature vector for movie $i$  

For user $j$ and movie $i$, predict rating: $w^{(j)} \cdot x^{(i)} + b^{(j)}$  
$m^{(j)} =$ no. of movies rated by user $j$  
To learn $w^{(j)}, b^{(j)}$

Now, the cost function using **mean squared error** for a single user will be

## $\min_{w^{(j)}b^{(j)}} J(w^{(j)}, b^{(j)}) = \frac{1}{2m^{(j)}} \sum_{i:r(i,j)=1} (w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)})^2$

We can also enhance this by adding the regularization param

## $\min_{w^{(j)}b^{(j)}} J(w^{(j)}, b^{(j)}) = \frac{1}{2m^{(j)}} \sum_{i:r(i,j)=1} (w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)})^2 + \frac{\lambda}{2m^{(j)}} \sum_{k=1}^{n} (w_k^{(j)})^2$

where n is the number of features

### For all users

Now, we can also enhance this function by generalizing it as the sum for all users

$$
J\left(\begin{array}{c}
w^{(1)}, \ldots, w^{(n_u)} \\
b^{(1)}, \ldots, b^{(n_u)}
\end{array}\right) = \frac{1}{2}\sum_{j=1}^{n_u} \sum_{i:r(i,j)=1} (w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)})^2 + \frac{\lambda}{2}\sum_{j=1}^{n_u}\sum_{k=1}^{n} (w_k^{(j)})^2
$$

where $n_u$ is the number of users. Notice that we've also removed the $m^(j)$ term from the equation. This is because this is a constant factor for the given user and removing it does not incluence the value of the cost function.

## What if you don't know x1 and x2

So far we've assumed that we have data for $x_1$ and x_2$ but how did we generate those? Let's first make the assumption that we know $w^{(1)}, b^{(1)}, w^{(2)}, b^{(2)}, \ldots, w^{(n_u)}, b^{(n_u)}$ (We'll dive more into this later. To get one feature we use 

## $J(x^{(i)}) = \frac{1}{2} \sum_{j:r(i,j)=1} (w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)})^2 + \frac{\lambda}{2} \sum_{k=1}^{n} (x_k^{(i)})^2$

Going further, we can generalize this to be for all the features that we're looking for.

## $J(x^{(1)}, x^{(2)}, ..., x^{(n_m)}) = \frac{1}{2}\sum_{i=1}^{n_m}\sum_{j:r(i,j)=1}(w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)})^2 + \frac{\lambda}{2}\sum_{i=1}^{n_m}\sum_{k=1}^{n}(x_k^{(i)})^2$

## How do we get the weights and biases

Now what we want to do is to take the cost function to get the weights and biases along with the cost function to get the input to get $J(w,b,x$

## $J(w, b, x) = \frac{1}{2} \sum_{(i,j):r(i,j)=1} (w^{(j)} \cdot x^{(i)} + b^{(j)} - y^{(i,j)})^2 + \frac{\lambda}{2} \sum_{j=1}^{n_u} \sum_{k=1}^{n} (w_k^{(j)})^2 + \frac{\lambda}{2} \sum_{i=1}^{n_m} \sum_{k=1}^{n} (x_k^{(i)})^2$

As with linear regression from before, we want to find the minimum values for these using gradiant descent.

## $w_i^{(j)} = w_i^{(j)} - \alpha \frac{\partial}{\partial w_i^{(j)}} J(w, b, x)$

## $b^{(j)} = b^{(j)} - \alpha \frac{\partial}{\partial b^{(j)}} J(w, b, x)$

## $x_k^{(i)} = x_k^{(i)} - \alpha \frac{\partial}{\partial x_k^{(i)}} J(w, b, x)$

## Recommender Systems

Building on our knowlege of collaborative filtering, the question that arises is: What if a brand new user shows up? We don't want to assume that that user is just going to give everying a zero and not like anything. We'd like to assume that they're going to like some stuff so that we can still make recommendations. What we want to employ is **mean normalization**.
So if we have a matrix as below where question marks are placeholders meaning that the user has no rating for the movie, we notice that we have an entire column of ?s representing the new user.

$$
\begin{bmatrix}
5 & 5 & 0 & 0 & ? \\
5 & ? & ? & 0 & ? \\
? & 4 & 0 & ? & ? \\
0 & 0 & 5 & 4 & ? \\
0 & 0 & 5 & 0 & ?
\end{bmatrix}
$$

What we want to do is generate a vector that'll be the mean taken for each row for only the users that have provided a rating for the movie. We end up with:

$$
\mu = 
\begin{bmatrix}
2.5 \\
2.5 \\
2 \\
2.25 \\
1.25
\end{bmatrix}
$$

So by putting in mean normalization, we will subtract $\mu$ from the user matrix

$$
y^(i,j)=
\begin{bmatrix}
2.5 & 2.5 & -2.5 & -2.5 & ? \\
2.5 & ? & ? & -2.5 & ? \\
? & 2 & -2 & ? & ? \\
-2.25 & -2.25 & 2.75 & 1.75 & ? \\
-1.25 & -1.25 & 3.75 & -1.25 & ?
\end{bmatrix}
$$

and use this to derive $w^j \dot x^i + b^j$. Because we did a subtraction for mean normalization, we will do an addition so that our value once again fall within the range properly. $w^j \dot x^i + b^j + \mu$. We can use this to get how our new user would rate this movie they haven't seen. Because it's a new user, we can assume that the weights and bias are just 0.

## $w^{(5)} \cdot x^{(1)} + b^{(5)} + \mu_1 = 2.5$
## 0 + 2.5 = 2.5

So the new user is more likely to give the mean rating which is 2.5

Mean normalization will help show reasonable recommendations to new users but this is still generally referred to as a **cold start problem**. Sometimes side information is used for this. So for example, the location (gotten by the IP address), or the age of the user may influence recommendations given a cold start problem.

Below is an implementation of a recommender system.

```py
import numpy as np
import tensorflow as tf
from tensorflow import keras
from recsys_utils import *

# utils
def normalizeRatings(Y, R):
    """
    Preprocess data by subtracting mean rating for every movie (every row).
    Only include real ratings R(i,j)=1.
    [Ynorm, Ymean] = normalizeRatings(Y, R) normalized Y so that each movie
    has a rating of 0 on average. Unrated moves then have a mean rating (0)
    Returns the mean rating in Ymean.
    """
    Ymean = (np.sum(Y*R,axis=1)/(np.sum(R, axis=1)+1e-12)).reshape(-1,1)
    Ynorm = Y - np.multiply(Ymean, R) 
    return(Ynorm, Ymean)

def load_precalc_params_small():

    file = open('./data/small_movies_X.csv', 'rb')
    X = loadtxt(file, delimiter = ",")

    file = open('./data/small_movies_W.csv', 'rb')
    W = loadtxt(file,delimiter = ",")

    file = open('./data/small_movies_b.csv', 'rb')
    b = loadtxt(file,delimiter = ",")
    b = b.reshape(1,-1)
    num_movies, num_features = X.shape
    num_users,_ = W.shape
    return(X, W, b, num_movies, num_features, num_users)
    
def load_ratings_small():
    file = open('./data/small_movies_Y.csv', 'rb')
    Y = loadtxt(file,delimiter = ",")

    file = open('./data/small_movies_R.csv', 'rb')
    R = loadtxt(file,delimiter = ",")
    return(Y,R)

def load_Movie_List_pd():
    """ returns df with and index of movies in the order they are in in the Y matrix """
    df = pd.read_csv('./data/small_movie_list.csv', header=0, index_col=0,  delimiter=',', quotechar='"')
    mlist = df["title"].to_list()
    return(mlist, df)

# end util

def cofi_cost_func(X, W, b, Y, R, lambda_):
    """
    Returns the cost for the content-based filtering
    Args:
      X (ndarray (num_movies,num_features)): matrix of item features
      W (ndarray (num_users,num_features)) : matrix of user parameters
      b (ndarray (1, num_users)            : vector of user parameters
      Y (ndarray (num_movies,num_users)    : matrix of user ratings of movies
      R (ndarray (num_movies,num_users)    : matrix, where R(i, j) = 1 if the i-th movies was rated by the j-th user
      lambda_ (float): regularization parameter
    Returns:
      J (float) : Cost
    """
    nm, nu = Y.shape
    J = 0
    ### START CODE HERE ###  
    _,n = X.shape
#     cost without reg
    for j in range(0, nu):
        
        for i in range(0, nm):
            J += R[i,j] * np.square((np.dot(W[j,:], X[i,:]) + b[0,j] - Y[i,j]))
    
    J = J/2
    
# reg params
    reg_weights, reg_x = 0, 0
    for j in range(nu):
        for k in range(n):
            reg_weights+=np.square(W[j,k])
    reg_weights = (lambda_/2) * reg_weights
    
    for i in range(nm):
        for k in range(n):
            reg_x+=np.square(X[i,k])
    reg_x = (lambda_/2) * reg_x
    
    J += reg_weights + reg_x
    

    ### END CODE HERE ### 

    return J

X, W, b, num_movies, num_features, num_users = load_precalc_params_small()
Y, R = load_ratings_small()

# Reduce the data set size so that this runs faster
num_users_r = 4
num_movies_r = 5 
num_features_r = 3

X_r = X[:num_movies_r, :num_features_r]
W_r = W[:num_users_r,  :num_features_r]
b_r = b[0, :num_users_r].reshape(1,-1)
Y_r = Y[:num_movies_r, :num_users_r]
R_r = R[:num_movies_r, :num_users_r]

# Evaluate cost function with regularization 
J = cofi_cost_func(X_r, W_r, b_r, Y_r, R_r, 1.5);

# load ratings
my_ratings = np.zeros(num_movies)
Y, R = load_ratings_small()

# use column stacking and add it as the first axis is the existing matrix y
Y = np.c_[my_ratings, Y]

# Add new user indicator matrix to R
R = np.c_[(my_ratings != 0).astype(int), R]

# Normalize the Dataset
Ynorm, Ymean = normalizeRatings(Y, R)

### Use tensorflow to train the model
num_movies, num_users = Y.shape
num_features = 100

# Set Initial Parameters (W, X), use tf.Variable to track these variables
tf.random.set_seed(1234) # for consistent results
W = tf.Variable(tf.random.normal((num_users,  num_features),dtype=tf.float64),  name='W')
X = tf.Variable(tf.random.normal((num_movies, num_features),dtype=tf.float64),  name='X')
b = tf.Variable(tf.random.normal((1,          num_users),   dtype=tf.float64),  name='b')

# Instantiate an optimizer.
optimizer = keras.optimizers.Adam(learning_rate=1e-1)

### GradientTape is how tensorflow is recording the results and "learning" the next values that it should do


iterations = 200
lambda_ = 1
for iter in range(iterations):
    # Use TensorFlow’s GradientTape
    # to record the operations used to compute the cost 
    with tf.GradientTape() as tape:

        # Compute the cost (forward pass included in cost)
        cost_value = cofi_cost_func_v(X, W, b, Ynorm, R, lambda_)

    # Use the gradient tape to automatically retrieve
    # the gradients of the trainable variables with respect to the loss
    grads = tape.gradient( cost_value, [X,W,b] )

    # this is the code that will actually update the weights and biases at each iteration
    # grads the amounts to change at each iteration while zip will pair each gradient with the corresponding tf variables that we've set earlier
    optimizer.apply_gradients( zip(grads, [X,W,b]) )

    # Notice that the loss goes down with each iteration
    if iter % 20 == 0:
        print(f"Training loss at iteration {iter}: {cost_value:0.1f}")

### Make predictions!
# We can now use the trained weights and biases that we've generated to make new recommendations

# Make a prediction using trained weights and biases
p = np.matmul(X.numpy(), np.transpose(W.numpy())) + b.numpy()

#restore the mean
pm = p + Ymean

my_predictions = pm[:,0]

# sort predictions
ix = tf.argsort(my_predictions, direction='DESCENDING')

for i in range(17):
    j = ix[i]
    if j not in my_rated:
        print(f'Predicting rating {my_predictions[j]:0.2f} for movie {movieList[j]}')

print('\n\nOriginal vs Predicted ratings:\n')
for i in range(len(my_ratings)):
    if my_ratings[i] > 0:
        print(f'Original {my_ratings[i]}, Predicted {my_predictions[i]:0.2f} for {movieList[i]}')
```

![image](https://github.com/user-attachments/assets/af20b40c-115e-4394-99f2-bbd8318a3d6b)


Note that we can also use tensorflow to make the generation of the linear algebra used for the cost function easier.

```py
def cofi_cost_func_v(X, W, b, Y, R, lambda_):
    """
    Returns the cost for the content-based filtering
    Vectorized for speed. Uses tensorflow operations to be compatible with custom training loop.
    Args:
      X (ndarray (num_movies,num_features)): matrix of item features
      W (ndarray (num_users,num_features)) : matrix of user parameters
      b (ndarray (1, num_users)            : vector of user parameters
      Y (ndarray (num_movies,num_users)    : matrix of user ratings of movies
      R (ndarray (num_movies,num_users)    : matrix, where R(i, j) = 1 if the i-th movies was rated by the j-th user
      lambda_ (float): regularization parameter
    Returns:
      J (float) : Cost
    """


    j = (tf.linalg.matmul(X, tf.transpose(W)) + b - Y)*R
    J = 0.5 * tf.reduce_sum(j**2) + (lambda_/2) * (tf.reduce_sum(X**2) + tf.reduce_sum(W**2))
    return J
```

# Content Based Filtering

Collaborative filtering will reccend items to you based on ratings of users who gave similar ratings as you. By contrast, content-based filtering will recommend items to you based on features of user and the items they match to find a good match. The main way to think of content based filtering is that we're also taking user features into account. 

![image](https://github.com/user-attachments/assets/3700391d-52e8-439b-8533-4fe8ebd4e5f9)

So we're going to introduce two new notations for our movie system $\mathbf{x}_u^{(j)} \text{ for user } j$ and $\mathbf{x}_m^{(i)} \text{ for movie } i$ In addition, we'll also introduce $V_u^{(i)$ and $V_m^{(i)$ that will be derived from user vector $X_u^{(i)$ and movie vector $X_m^{(i)$ respectively. This is handy because $X_u^{(i)$ and $X_m^{(i)$ can be different sizes because of different features while $V_u^{(i)$ and $V_m^{(i)$ will be made to stay the same size which is needed for the dot product.

## Dimensionality reduction

This brings up the question of how do we reduce the potentially thousands of input difference to two vectors/matrices with the same dimensions? The way that this architecture will work is that we'll have a neural network for the user network and one for the movie network. Notice that we'll need the output layer of both of these to be the same.

![image](https://github.com/user-attachments/assets/f1d82580-058a-4c74-8ffc-6185ce8ee846)

Cost function: J = \sum_{(i,j):r(i,j)=1} (v_u^{(j)} \cdot v_m^{(i)} - y^{(i,j)})^2 + \text{NN regularization term}

the output of the item/movie neural network,v is not dependent on the user network.x. when making predictions. This allows you to precompute the results, which speeds up the prediction process.

One caveat of this algorithm is that it may be computationally very expensive bepending of your catalogue size as you're invoking neural networks. Because of this computational expense, we move to our next topic to make this more efficient. For example, we might have a database of 1000+ movies like Netflix.

<img width="1867" alt="image" src="https://github.com/user-attachments/assets/5435a96b-5a2b-4cda-94fd-a50f3d43849e" />

We handle this by taking a subset first of the most plausible item candidates through a two step process called retrieval and ranking. An example of the retrieval step might be only generate a list of 10 most similar movies based on the last 10 movies watched rather than use the entire user history.

<img width="1858" alt="image" src="https://github.com/user-attachments/assets/2d14c139-211e-4022-b425-d503f7091342" />

From this retrieval step to generate the subset of movies, you'll now use the trained model to create a ranking

![image](https://github.com/user-attachments/assets/5dffb29a-79d1-4a0f-b22f-20303e4df7c9)

If we choose to modify the algorithm to add more items to the retrieval step, this might take longer to process but should improve recommendations.

## Ethical uses of recommender systems

Recommend:

→ • Movies most likely to be rated 5 stars by user
→ • Products most likely to be purchased  

The following can be a little more dubious and can be used for harm or for good.

→ • Ads most likely to be clicked on +high bid
→ • Products generating the largest profit
→ • Video leading to maximum watch time

For example, the following are ways that ads can be used unethically

Targeting Vulnerable Groups: Some ads may target low-income individuals with high-interest loans or payday loans, which can lead to financial exploitation. These ads often promote products that are not in the best interest of the consumer, leading to a cycle of debt.

Misinformation and Manipulation: Ads can spread misinformation, such as promoting false health claims or conspiracy theories. This can mislead consumers and contribute to harmful behaviors or beliefs, especially if the content is designed to provoke strong emotional reactions.

![image](https://github.com/user-attachments/assets/6f710ab1-bf7e-4069-8460-d16ba3e89039)

Conclusively, recommender systems are extremely powerful systems so ethics really does come into play.

