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



