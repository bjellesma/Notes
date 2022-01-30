While arithmetic is about calculation; number theory examines the abstract properties of number. Number theory is crucial in subjects such as internet security.

# Division Theorem

Let a, b be integers with b>0, the **Division Theorem** states that there are unique integers q, r such that $a=qb+r \text{ and } 0 \le r \lt b$. The proof for this is as follows:

We prove existence first, then uniqueness.

**Existence**: Look at all non-negative integers of the form $a-kb$ where k is an integer, and show that one of them is less than b. Such integers do exist. Take $k=|a|$. Then, since $b \ge 1$, $a-kb=a+|a|b \ge a + |a| \ge 0.$ Let r be the smallest stuch integer. Let q be the value of k for which it occurs (r=a-qb). To complete the proof, we show that $r \lt b$.  Suppose, on the contrary, that $r \ge b$. Then: $a=(q+1)b=a-qb-b=r-b \ge 0$. Thus $a-(q+1)b$ is a non negative inter of the form $a-kb$. But r is the small such, and yet $a-(q+1)b \lt a-qb=r$. This is a contradiction. Hence $r \lt b$. This proves existence.

**Uniqueness**: We show that if there are two representations of a, $a=qb+r=q^1b+r^1$, $0 \le r, r^1 < b$. Rearranging the above equations we have $r^1-r=b(q-q^1)$ and $|r^1-r|=b|q-q^1|$ .

But $-b \lt -r \le 0$ and $0 \le r^1 \lt b$, so $-b \lt r^1-r \lt b$. 

So by $|r^1-r|=b|q-q^1|$, $b|q-q^1| \lt b$ hence $|q-q^1| \lt 1$ so $q=q^1$

And by $r^1-r=b(q-q^1)$, r=r^1

# Infinity

**Infinity**, the idea that something is never ending, is essential to understand in modern science and engineering.

# General Division Theorem

Here, we expand upon the division theorem to include negative number. The theorem is almost the same except instead of having b be strictly positive, we just say that b is nonzero and the final constraint calls for the absolute value of b.

Let a, b be integers with $b \ne 0$, the **General Division Theorem** states that there are unique integers q, r such that $a=qb+r \text{ and } 0 \le r \lt |b|$. The proof for this is as follows:

We have proven the case for $b \gt 0$ above so we'll assume $b \lt 0$. Since $|b| \gt 0$, the previous theorem tells us there are unique integers $q^1$, $r^1$ such that $a=q^1|b|+r^1$ and $0 \le r^1 \lt |b|$

Let $q=-q^1$, $r=r^1$. Then, since $|b|=-b$, we get $a=qb+r$ which proves the theorem.

q is called the **quotient** of a by b, and r is called the **remainder**. We learn these definitions early on but we're now giving them a rigorous proof.

# Divisibility

If division of a by b produces a remainder r=0, we say that a is **divisible** by b. Hence, a is divisible by b if and only if there is an integer q such that a=bq. The notation $b|a$ means that a is divisible by b (describing a relationship) and this is not the same as $b/a$ (describing an operation).

# Prime number

A prime number is an integer p>1 that is divisible only by 1 and p

# Exercises

a. $9|0$ means that $\exists q[0=9q]$ which is true because q can be zero

b. $0|0$ and $0|7$ don't work because of the definition $b|a \text{ iff } \exists q[a=bq]$ where $b \ne 0$

c. $2708|569401$ is false because an even is unable to divide an odd

d. $\forall n \in \Z[1|n]$ is true by the first property of division listed below

e. $\forall n \in \N[n|0]$ is true by the first property of division listed below

f $\forall n \in \N[n|n]$ is true because the set is natural numbers which doesn't include zero

g. $\forall n \in \Z[n|n]$ is false because the set of integers contains zero

# Basic Properties of Divisibility

Theorem: let a, b, c, d be integers with $a \ne 0$ Then the following hold

1. $a|0, a|a$
2. $a|1$ iff $a=\pm 1$
3. if $a|b$ and $c|d$, then $ac|bd$ provided $c \ne 0$
4. if $a|b$ and $b|c$, then $a|c$ provided $b \ne 0$

$\exists d,e[b=da \text{ and } c=eb$ (By the definition of division). So, $c=e(da)$ which, by the definition of division, means $a|c$

5. $a|b$ and $b|a$ if and only if $a=\pm b$
6. if $a|b$ and $b \ne 0$, the $|a| \le |b|$

Since $a|b$, $\exists d[b=da]$ (by the definition of division) and $|b|=|d||a|$. Since $b \ne 0$, $|d| \ge 1$ and $|a| \le |b|$

7. if $a|b$ and $a|c$, then $a|(bx+cy)$ for any integers x, y

For all other statements, we just use the definition of division

# Fundamental Theorem of Arithmetic

Theorem: Every natural number greater than 1 is either prime or can be expressed as a product of primes in a way that is unique except the order in which they're writen.

For example: 2 is prime, 3 is prime, 4 is 2 x 2, 5 is prime, 6 is 3 x 2

The expression of a number as a product of primes is called its **prime decomposition**

The key takeaway is that that a number only has one unique prime decomposition.