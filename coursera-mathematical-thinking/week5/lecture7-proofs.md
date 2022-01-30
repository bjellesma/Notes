# What is a proof

# Why are proofs used?

You may an intuition about a solution such as **Fermat's Last Theorem** but you can't be sure about it unless we can construct a **proof**, a logically sound argument. This was a conjecture until a proof was constructed in 1994 so this is now a theorem. The main purpose of a proof is both to establish the truth of a statement and explain why the statement is true.

In Contrast, there is a conjecture called **Goldbach Conjecture** that says that every even number greater than 2 can be expressed as a sum of two prime numbers. To date, this has been verified for every even number up to the quintillions but a proof has yet to be written, thus it's still a conjecture. If you found one number that can disprove this conjecture, the conjecture is disproven.

"A mathematical proof is a thought sculpture built from the poetry of patterns" - Gioia De Cari

The most important feature of a proof is its logical structure. The proof should also be sufficiently easy to follow for another person at your level but it is not a requirement.

# Euclid's infinitely many primes theorem

 PROOF (as made by Euclid): 
 $
\text{We show that if we list the primes} \ p_1, p_2, p_3,...,p_n\newline
\text{Can we find another prime to continue the list}\newline
\text{Set} N = (p_1*p_2*p_3*...*p_n)+1\newline
\text{If N is prime, we have found a prime bigger than} p_n \text{and we can continue the list}
\text{If N is not prime, it is divisible by a prime, say p}\newline
\text{p cannot be any of} p_1, p_2,...,p_n \text{because dividing N by any of those would leave a remainder of 1 (N//2=1 and N//5=1) but it must be divisible by a number bigger than } p_n \newline
\text{So }p>p_n\text{ So again we have found a prime bigger than } p_n \text{. If N is not prime, there is a bigger prime meaning that the list can be continued}
 $

  The above proof is saying that in both cases, there are infinitely many primes. If N is prime, this is already proven. If N is not prime, then there must be a bigger prime that it is divisible by. In both cases, the list continues. The key definition is $\text{Set} N = (p_1*p_2*p_3*...*p_n)+1\newline$

# Lemma

A **lemma** is a result from a theorem that is worth pointing out.


# Root 2 is irrational

Theorem: $\sqrt{2}# is irrational

Proof: Assume, on the contrary, $\sqrt{2}$ is rational. Then there are natural numbers p, q with no common factors (p and q having no common factors just means that $\frac{p}{q}$ is in its simplist form), such that $\sqrt{2}=\frac{p}{q}$. 

Squaring: $2=\frac{p^2}{q^2}$

Rearranging: $2q^2 = p^2$

So, $p^2$ must be even because it is equal to double some other natural number. This means $p$ must be even (squaring an even gives an even, squaring an odd gives an odd). So $p=2r$ for some r.

Substituting: $2q^2 = (2r)^2 = 4r^2$

Canceling: $q^2 = 2r^2$

So $q^2$ is even and $q$ is even for the same logic as above.

This means that p and q are both even which means they have common factors. Since we said at the begining that p and q have no common factors, this is disproven. If $\sqrt{2}$ is not rational, it must be irrational.

# Proof by contriction

The proof that root 2 is irrational is an example of a proof by contridiction. 

1. You want to prove some statement $\phi$
2. Start by assuming $\neg \phi$
3. You reason until you reach a conclusion that is false.
    * Often by deducing bot $\phi$ and $\neg \phi$
    * For example, we deduced that p,q had no common factor and that p,q are both even
4. A true assumption cannot lead to a false conclusion
5. Hence the assumption $\neg \phi$ must be false
6. In other words $\phi$ must be true, in contrast to the assumption

Because you can deduce any contradiction which creates such a wide target area, this is often the easiest for people to do. It provides a clear starting path and many paths to a logical conclusion.

# Ending

It's a habit of Mathematicians to enter "QED" (latin) at the end of the proof.

# Prove that root 3 is irrational

1. Assume $\sqrt{3}$ is rational. Then there are natural numbers p, q with no common factors, such that $\sqrt{3}=\frac{p}{q}$. 

Squaring: $3=\frac{p^2}{q^2}$

Rearranging: $3q^2 = p^2$ or $p=\sqrt{3}q$ and $q=\frac{p}{\sqrt{3}}$

# Contrapositive

Conditionals involving quantifiers are usually best handled by proving the **contrapositive**, that is, to prove $\phi \implies \psi$, prove $\neg \psi \implies \neg \phi$ (notice that the direction of implication is switched).

Claim: $(sin(\theta)\ne0) \implies \forall n \in \N (\theta \ne n\pi)$

This is equivalent to the contrapositive $\neg (\forall n \in \N) (\theta \ne n\pi) \implies \neg (sin(\theta)\ne 0)$

Converting this to positive form: $(\exist n \in \N)(\theta=n\pi) \implies (sin(\theta) = 0)$. Notice that the negation has change the $\ne$ to = and the $\forall$ to $\exists$

We know that whenever you have a whole number multiple of $\pi$, its sine is always 0 so the contrapositive is true thus the claim is true.

# Rationals and Irrationals

Let r and s be irrational numbers, which of the following are necessarily irrational.

1. $r+3$

Assume $r+3=rational$. $r=rational-3$ and 3 is rational so a rational-rational must be rational which is a contridiction.

True

2. $5r$

Assume the product is rational then r=rational/5. The quotient of a rational and a rational must be rational which is a contridiction.

True

3. $r+s$

Assume the sum is rational so that $r+s=rational$. Then r = rational-s. We can't conclude the sum or difference.

Finding an example, set $r=\sqrt{2}$ and $s=10-\sqrt{2}$. The the sum would be 10 which is rational

False

4. $r*s$

if we assume this to be rational, $r*s=\frac{p}{q}*\frac{m}{n}=\frac{pn+mq}{qn}$. We can't conclude the values of the products.

Finding an example, set $r=\sqrt{2}$ and $s=\sqrt{2}$. The the product would be 2 which is rational

False

5. $\sqrt{r}$

If we assume $\sqrt{r}$ to be rational then $\sqrt{r}=\frac{p}{q}$ so $r=\frac{p^2}{q^2}$ so $p^2$ and $q^2$ are both rational. But r is irrational so this is a contridiction

True