# Negation of Quantifiers

Let $A(x)$ be some property of x. Show that $\neg[\forall x A(x)]$ is equivalent to $\exists x [ \neg A(x)]$.

Assume $\neg [\forall x A(x)]$. If it is not the case that for all x, $A(x)$, then at least one x must fail to satisy $A(x)$. So for at least one x, $\neg A(x)$ is true.

Likewise: Assume $\exists x [\neg A(x)]$. Then there is an x for which $A(x)$ is false. Then $A(x)$ cannot be true for all x $\forall x A(x)$ must be false. If $A(x)$ is false for some x, it follows that $\neg [\forall x A(x)]$

## Cars example

Let C be the set of all cars, D(x) means x is domestic and M(x) means that x is badly made. We'll use the statement all domestic cars are badly made. $(\forall x \in C)[D(x) \implies M(x)]$. The negation of this statement would be $\exists x \in C[D(x) \not \implies M(x)]$. We know that $[D(x) \not \implies M(x)]$ is equivalent to $D(x) \land \neg M(x)$.

So, $\neg (\forall x \in C)[D(x) \implies M(x)]$ (it's not the case that for all cars, a domestically made car implies that is is badly made) is equivalent to $\exists x \in C [ D(x) \land \neg M(x)]$ (There exists a car that is domestic and not badly made)

## Prime Numbers example

Claim: All prime numbers are odd (we know that this claim is false because 2 is prime and not odd)

Let $P(x)$ mean that x is prime and $O(x)$ mean that x is odd so $\forall x [P(x) \implies O(x)]$.

So for the negation, $\neg \forall x[ P(x) \implies O(x)] \leftrightarrow \exists x [P(x) \not \implies O(x)$. In words, there exists a prime that is not odd.

So in order to prove that the claim is false, we need to find something that proves that "there exists a prime that is not odd"

## Quiz

What is the negation of $(\forall x \gt 2)[P(x) \implies O(x)]$?

$\neg (\forall x \gt 2)[P(x) \implies O(x)] \leftrightarrow \exists x \gt 2[ P(x) \not \implies O(x) \leftrightarrow \exists x \gt 2 [ P(x) \land \neg O(x)]$

Keep in mind that the claim involving a whole number greater than 2 means the negation must involve a whole number greater than 2.

## Mathematical Shorthand

Some mathematicians will write the form $x \geq 0 \implies \sqrt(x) \geq 0$ when it means something like $(\forall x \in \R)[x \geq 0 \implies \sqrt(x) \geq 0]$. This is known as **implicit quantification**. The placement of parentheses/brackets is important too.

## Distributive

$\forall x [ A(x) \lor B(x)]$ is not equivalent to $\forall x A(x) \lor \forall x B(x)$. For example, it's true that for all numbers, they are even or odd. However, it's not true the for all numbers they are even or for all numbers they are odd. See the difference.

$\forall x [ A(x) \land B(x)]$ is equivalent to $\forall x A(x) \land \forall x B(x)$. For example, all athletes are big and strong is equivalent to all athletes are big and all athletes are strong.

$\exists x [ A(x) \land B(x)]$ is not equivalent to $\exists x A(x) \land \exists x B(x)$. For example, it's false that there exists a number that is even and odd but it's true that there exists an even number and there exists an odd number.

$\exists x [ A(x) \lor B(x)]$ is equivalent to $\exists x A(x) \or \exists x B(x)$. For example, it's true that there exists an athlete that is big or strong. It's true that there exists an athlete that is big or there exists an athlete that is strong.