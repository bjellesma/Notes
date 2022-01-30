# Induction Proofs

To prove mathematical statements with quantifiers, we often use a proof by induction. 

## Example: Prove Existence Statement ($\exists x A(x)$)

Theorem: There are irrationals r,s such that $r^s$ is rational.

Case 1: If $\sqrt(2)^{\sqrt(2)}$ is rational, take $r=s=\sqrt(2)$

Case 2: If $\sqrt(2)^{\sqrt(2)}$ is irrational, take $r=\sqrt(2)^{\sqrt(2)} \text{ and } s=\sqrt(2) $
    then $r^s=(\sqrt(2)^{\sqrt(2)})^{\sqrt(2)} = \sqrt(2)^2=2 which is rational$

These two cases prove the theorem since this is an existence theorem.

This is an **indirect proof** because we don't know if $\sqrt(2)^{\sqrt(2)}$ is rational or irrational but these two cases prove the theorem. This specific proof with examples is know as a **method of proof by cases** which is used a lot in upper level mathematics.

## Example: Prove Universal Statement ($\forall x A(x)$)

In the below, we'll take an arbitrary x and show that it satisfies A(x).

Statement: $\forall n \exists m (m \gt n^2)$

Let n be an arbitrary natural number. Set $m=n^2+1$. Then $m \gt n^2$. This proves $\exists m (m \gt n^2)$. It follows that $\forall n \exists m (m \gt n^2)$ thus proving the statement.

The key in the above statement is that we're removing the forall quantifier and replacing it by saying let n be an arbitrary natural number. 

## Method of Contridiction

To prove $\forall x A(x)$, we can assume $\neg \forall x A(x)$. This is equivalent to $\exists x \neg A(x)$

# Induction

**Induction Proofs** are often done by finding a pattern in the first few cases. To prove $\forall n A(n)$, we estabilish two statements.

1. Initial Step: Prove A(1)
2. Induction Step: Prove $\forall n (A(n) \implies A(n+1))$

For example, we want the induction step to prove $A(1) \implies A(2)$ to conclude A(2) and that $A(2) \implies A(3)$, etc.

## Example:

Theorem: For any n, $1+2+3+...+n = \frac{1}{2} n(n+1)$

Proof: By mathematical induction.

For n=1, the identity reduces to $1 = \frac{1}{2}(1)(1+1)=1$. This proves the initial case.

Assume the identity holds for n, $1+2+3+...+n = \frac{1}{2} n(n+1)$ which means we want to deduce the n+1 case $1+2+3+...+n+1 = \frac{1}{2} (n+1)((n+1)+1)$. So, we'll add n+1 to both sides of $1+2+3+...+n = \frac{1}{2} n(n+1)$.

$1+2+3+...+n+1 = \frac{1}{2} n(n+1)+(n+1)$

distribute on the left: $= \frac{1}{2} [n(n+1)+2(n+1)]$

Simplify the left side: $= \frac{1}{2} [n^2+n+2n+2]$

Simplify the left side: $= \frac{1}{2} [n^2+3n+2]$

Simplify the left side: $= \frac{1}{2} [(n+1)(n+2)]$

Make the left side match the deduced case: $= \frac{1}{2} [(n+1)((n+1)+1)]$

This proves the induction step and thus proves that the theorem holds.

Mathematical Induction is a very deep topic because it proves statements that are true for all natural numbers, and the are infinitely many of them.

## Mathematical Induction Variant

There are some proofs which, by their statements, cannot be started at 1 and need to be started at the first available number. The following theorem will be proved by mathematical induction but will start at n=2.

Theorem: Every Natural number greater than 1 is either prime or a product of primes.

Proof: By induction, our induction statement A(n) is $\forall m[2\le m \le n \implies m \text{ is either a prime or a product of primes}]$

TODO: I'm having trouble understanding this part in particular.