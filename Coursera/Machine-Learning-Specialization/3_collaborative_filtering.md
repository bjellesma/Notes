![image](https://github.com/user-attachments/assets/c9045154-d8f7-4edd-82ee-d65fe6302ec0)

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
