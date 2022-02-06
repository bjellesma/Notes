# Analysis of Numbers

Numbers have been used for 100s of years for counting and measurements. **Discrete Counting Numbers** are used for counting and **Continuous Real Numbers** are used for measurement. 

Integers can used to describe rationals which in turn can be used to describe the real numbers. Rational numbers of just ratios. The historic progression of these numbers are the natural numbers to the integers to the rationals and then to the real numbers. The **real numbers** are the set of numbers that are really required to do mathematics because they include the rational as well as irrational numbers.

# Density

If r and s are rationals, with r < s, then there is a rational t such that r < t < s. We say that the rational line is dense if between any two distinct numbers lies a third. Note that this does not mean that there are no gaps in the rational line. An example of a gap would be $\sqrt{2}$ (The quadratic equation $x^2-2=0$ couldn't be solved). This is the idea that led to the **irrational** numbers. The **real numbers** were constructed to fill in the holes

Proof: Let $t = \frac{1}{2}(r+s)$. Clearly $r < t < s$. The question now is is t a rational number.

Let $f=\frac{m}{n}$ and $s=\frac{p}{q}$ where m, n, p, and q are all integers. Then $t=\frac{1}{2}(\frac{m}{n}+\frac{p}{q})=\frac{mq+rp}{2nq}$. Since $mq+rp$ and $2nq$ are all integers, t must be a rational.

# Intervals

Let $a, b \in \R$ where $a < b$. The **Open Interval** (a,b) is the set ${x \in \R | a<x<b}$ that is, x is exclusively greater than a and exclusively less than b. The **Closed Interval** [a,b] is the set ${x \in \R | a \le x \le b}$ that is, x includes a and b. The last thing to note is that you can't have infitity in a closed interval because infinity is not a real number.

# Completeness Property

Given a set of A of real numbers, a number b such that $\forall a \in A[a \le b]$, b is said to be an **upper bound** of A. We say that b is a **least upper bound** of A if, in addition, for any upper bound c of A, we have $b \le c$. The notation for least upper bound of A is $lub(A)$. For example, 7 is the least upper bound of the interval $(-3,7)$ even though 7 is not an element in the interval

The **completeness property** of the the real number system says that every nonempty set of reals that has an upper bound, has a least upper bound.

The completeness property is the most significant property of the real number system that makes it more powerfull than the rational numbers.

# Intro to real analysis

Theorem: The rational line is not complete. 

Proof: Let A be the set $r \in  Q| r \ge 0 \land r^2 < 2$. A is bounded above (an example is that 2 is an upper bound). We'll show that there is no least upper bound.

Let $x \in Q$ be any upper bound of A, and show that there is a smaller number that is still a rational.

L $x=\frac{p}{q}$ where $p,q \in \N$.

Suppose $x^2 < 2$. Then $2q^2 > p^2$. As n gets larger, $\frac{n^2}{2n+1}$ increases without bound, so we can pirck an $n \in \N$ so large that $\frac{n^2}{2n+1} \gt \frac{p^2}{2q^2-p^2}$ which simplifies to $2n^2q^2 \gt (n+1)^2p^2$. Hence $(\frac{n+1}{n})^2(\frac{p^2}{q^2}) \lt 2$. 

Let $y=(\frac{n+1}{n})(\frac{p}{q})$. Thus y is a rational number because it is a quotient of integers and $y^2 \lt 2$. So $y \in A$ but $y \gt x$. This is a contradiction because x is an upper bound of A. So $x^2 \ge 2$ which means that $x^2$ because $\sqrt{2}$ is irrational. Thus $p^2 \gt 2q^2$ (because $x=\frac{p}{q}$) so $(\frac{n+1}{n})^2(\frac{p^2}{q^2}) \gt 2$

Since $(\frac{n+1}{n}) < 1$, $y \lt x$ But, for any $a \in A$, $a^2 \lt 2 \lt y^2$, so $a \lt y$. Hence y is an upper bound of A, smaller than x. Thus A does not have a least upper bount.

This proves the theorem.

# Real Number Sequences

A **sequence** is just a list and is written as $\{a_n\}_{n=1}^{\infty}$. More specifically, the sequence is an **infinite sequence** because it goes to infinity. For example, for the sequence 1, 2, 3, ... we can write this as $\{n\}_{n=1}^{\infty}$. Another example of a constant sequece like 7, 7, 7, ... would be written as $\{7\}_{n=1}^{\infty}$. An **alternating sequence** would be $\{(-1)^{n+1}\}_{n=1}^{\infty}$ because it evaluates to 1, -1, 1, -1,... (the sign changes).

The formal definition of $\{a_n\}_{n=1}^{\infty}$ is $a_n \rightarrow a as n \rightarrow \infty$ iff $(\forall \epsilon \gt 0)(\exists n \in \N)(\forall m \ge n)[|a_m-a| \lt \epsilon)$. This definition means that at some point n onwards, all the numbers are within a distance $\epsilon$ from a.

