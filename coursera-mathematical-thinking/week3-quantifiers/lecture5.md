There are two main quantifiers, there exists and for all, because most other mathematical statements can be defined in terms of these two.

# There Exists

There exists a real number x such that $x^2+2x+1=0$ can be written as $\exists x[x^2+2x+1=0]$. $\exists$ is called the **existential quantifier**.

The easiest way to prove an existence statement is to solve it. However, sometimes you can prove the existance quantifier without solving the equation. This is referred to as an **indirect proof**. For example, if we look at $\exists x[x^3+3x+1=0]$, we know that this is a continuous function because it is a cubic function with no jumps in the graph. We know that for x=-1, y=-3 and for x=1, y=5. We can conclude that the x-axis will be crossed somewhere between these two values therefore we know that there is a solution.

Let's look at another proof. Claim $\sqrt2$ is rational. This is obviously false, but we'll prove this.

There exists a rational number such that $\sqrt2 = p/q$

$\exists p \exists q [\sqrt2=p/q]$

We can make this more explicit and say that p and q are natural numbers.

$(\exists p \in \N )(\exists q \in \N) [\sqrt2=p/q]$

you may also see a more abreviated form as

$(\exists p,q \in \N ) [\sqrt2=p/q]$

# For All

$\forall$ is called the **universal quantifier** and means for all in the set.

The square of any real number is greater than or equal to zero can be written as:

$\forall z(z^2 \geq 0)$

# Combinations of Quantifiers

For all natural numbers m, there exists a natural number N such n is greater than m. This can be written as: 

$(\forall m \in \N)(\exists n \in N)(n \gt m))$

The order of the quantifiers here is different because 

$(\exists n \in N)(\forall m \in \N)(n \gt m))$

says that there is a natural number n bigger than the set of all natural numbers.

