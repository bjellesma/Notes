* The key to math is to think outside of the box
* The goal is understanding, not doing
    * Learning how to apply a template doesn't always work
* You should have someone else checking your work
* It's common for a mathematician to send something for publication and then get an anonymous person send in an error

## Background reading

Math began about ten thousand years ago to give the world money systems. Greeks made math more into an area of study rather than just a set of tools, this happened when they began to discover irrational numbers. According to legend, when the greeks began to discover lengths to which numbers did not correspond (irrational), they took the guy out to sea and drowned him. Most school math stops its teaching after the invention of calculus and probability theory in the 17th century. The more abstract definitions of what a function means is known as an **epsilon-delta** definition. Mathematics is among the greatest creation of society and education is about passing our knowledge along to the next generation. At the begining of the nineteenth century, the need was still very high for workers that could solve a mathematical problem given the problem but the workforce has shifted to folks that can describe everyday problems in a mathematical manner and use those skills to come up to speed on a tool quickly.

## Set Theory Introduction

A **set** is any well defined collection of objects. For example, the set of all students in a class. If A is a set, then objects in the set of A are called **members**. 

$x \in A$


 
 # Introductory Material

 What is mathematics?

 In the 19th century, the emphasis transition from procedures to analyzing relationships. Some have called it **The science of patterns**. For example, calculus studies the pattern of motion. 

 ## Getting Precise about language

 the primary reason for needing precise language is to develop a proof. Here's an example of well defined language and proof.

 CLAIM: There are infinitely many prime numbers.

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

 An example of a claim that doesn't make sense is

$
\text{For every real number } a \text{the equation } x^2 + a=0 \text{ has a real root.}
$

If we take a=1, we know $x^2 + 1 = 0$ doesn't have a real root because $x^2=-1$ which isn't possible. This shows that the claim is false.

Mathematics uses language is a highly restrictive way. Statements often follow the following forms:

1. Object a has Property P
2. Every object of type T has property P
3. There is an object of type T having property T
4. If statement A, then statement B

## Lecture 1 assignment

1. Find two unambiguous (but natural sounding) sentences equivalent to the sentence The man saw
the woman with a telescope, the first where the man has the telescope, the second where the woman
has the telescope.

There is a man with a telescope that saw a woman.

There is a woman with a telescope that was seen by a man.

2. For each of the three ambiguous newspaper headlines I stated in the lecture, rewrite it in a way
that avoids the amusing second meaning, while retaining the brevity of a typical headline:
(a) Sisters reunited after ten years in checkout line at Safeway.
(b) Large hole appears in High Street. City authorities are looking into it.
(c) Mayor says bus passengers should be belted.

Sisters are reunited after ten years in a checkout line of safeway.

Large hole appears on high street. City authorities are looking into the cause.

Mayor declares that bus passengers should wear their seat belts on the bus.

3. The following notice was posted on the wall of a hospital emergency room:
No head injury is too trivial to ignore.
Reformulate to avoid the unintended second reading. (The context for this sentence is so strong
that many people have difficulty seeing there is an alternative meaning.)

There is no injury of the head that is too trivial to ignore.

4. You often see the following notice posted in elevators:
In case of fire, do not use elevator.
This one always amuses me. Comment on the two meanings and reformulate to avoid the unintended
second reading. (Again, given the context for this notice, the ambiguity is not problematic.)

If a fire happens, don't use the elevator.

The ambiguity is that it can be read to say never use the elevator in case there is a fire.

5. Official documents often contain one or more pages that are empty apart from one sentence at the
bottom:
This page intentionally left blank.
Does the sentence make a true statement? What is the purpose of making such a statement?
What reformulation of the sentence would avoid any logical problems about truth? (Once again,
the context means that in practice everyone understands the intended meaning and there is no
problem. But the formulation of a similar sentence in mathematics at the start of the twentieth
century destroyed one prominent mathematician’s seminal work and led to a major revolution in
an entire branch of mathematics.)

I don't know

6. Find (and provide citations for) three examples of published sentences whose literal meaning is
(clearly) not what the writer intended. [This is much easier than you might think. Ambiguity is
very common.]

Reddit

The lady hit the man with an umbrella.

He gave her cat food.

They are looking for teachers of French, German and Japanese.

7. Comment on the sentence “The temperature is hot today.” You hear people say things like this
all the time, and everyone understands what is meant. But using language in this sloppy way in
mathematics would be disastrous.

The temperature of what is hot today?

8. How would you show that not every number of the form N = (p1 · p2 · p3 · . . . · pn) + 1 is prime,
where p1, p2, p3, . . . , pn, . . . is the list of all prime numbers?

The recommended way to go about doing this is just guess and check. Though this is seems an arbitrary method, it's the best at our disposal. We find that

$ 
2*3*5*7*11*13=30031
$

30031 is equal to 59*509 therefore it's not prime.



JUST FOR FUN
1. Provide a context and a sentence within that context, where the word and occurs five times in
succession, with no other word between those five occurrences. (You are allowed to use punctuation.)
2. Provide a context and a sentence within that context, where the words and, or, and, or, and occur
in that order, with no other word between them. (Again, you can use punctuation.)

# Combinators

The basic combinators are 

1. and

$
(\pi \gt 3) \land (\pi \lt 3.2)
$

This is a **conjuction** and both statements must be true. If one or both are false, the conjuction is false. This is like a boolean and in programming. A useful way to look at this is with a **propositional truth table**.

| $\phi$ | $\psi$ | $\phi \land \psi$ |
| --- | --- | --------- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

2. or

Unlike and, you can have an **exclusive or** where one or the other statement has to be true, but both can't be true, or you can have an **inclusive or** where one or the other or both can true. Because or can be ambiguous, mathematics has more precise notation

Here's an example of an exclusive or: $a\gt0 \text{ or the equation } x^2+a=0 \text{ has a real root} $

| $\phi$ | $\psi$ | $\phi \oplus \psi$ |
| --- | --- | --------- |
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F | 

Here's an example of an inclusive or (or **disjunction**): $ab=0 \text{ if } a=0 \text{ or } b=0$. Generally, this can be expressed as $\phi \lor \psi$

| $\phi$ | $\psi$ | $\phi \lor \psi$ |
| --- | --- | --------- |
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F | 

3. not

not N can be read as $\lnot N$

| $\phi$ | $\lnot\phi$ |
| --- | --------- |
| T | F |
| F | T |

4. implies
5. for all
6. there exists
7. equivalence

The first three are defined in this lecture and will be defined in future lectures.

## Lecture 2 Assignment

1. Simplify the following symbolic statements as much as you can, leaving your answer in the standard
symbolic form. (In case you are not familiar with the notation, I’ll answer the first one for you.)

(a) (π > 0) ∧ (π < 10) [Answer: 0 < π < 10.]

(b) (p ≥ 7) ∧ (p < 12)

$7 \leq p \lt 12$

(c) (x > 5) ∧ (x < 7)

$ 5 \lt x \lt 7$

(d) (x < 4) ∧ (x < 6)

$ x \lt 4 $

(e) (y < 4) ∧ (y^2 < 9)

$-3 \lt y \lt 3$

Since y is less than either 3 or -3 for the second part and y < 4 includes this set, we can keep this one statement

(f) (x ≥ 0) ∧ (x ≤ 0)

$x=0$

Less than or equal to a value and greater than or equal to a value must mean it's equal to that value

2. Express each of your simplified statements from question 1 in natural English.

a. pi is between 0 and 10
b. p is betweeen 7 and 12
c. x is between 5 and 7, exclusive
d. x is less than 4
e. y is less than 3
f. x is 0


3. What strategy would you adopt to show that the conjunction φ1 ∧ φ2 ∧ . . . ∧ φn is true?

All statements must evaluate to true.

4. What strategy would you adopt to show that the conjunction φ1 ∧ φ2 ∧ . . . ∧ φn is false?

At least one statement must evaluate to false

5. Simplify the following symbolic statements as much as you can, leaving your answer in a standard
symbolic form (assuming you are familiar with the notation):

(a) (π > 3) ∨ (π > 10)

$\pi \gt 3$

one set includes the other

(b) (x < 0) ∨ (x > 0)

$x\neq0$

(c) (x = 0) ∨ (x > 0)

$x\geq0$

(d) (x > 0) ∨ (x ≥ 0)

$x\gt0$

(e) (x > 3) ∨ (x^2 > 9)

$x^2\gt9$


6. Express each of your simplified statements from question 5 in natural English.

a. pi is greater than 3

b. x is not equal to zero

c. x is greater than or equal to zero

d. x is greater than or equal to zero

e. x is greater than -3

7. What strategy would you adopt to show that the disjunction φ1 ∨ φ2 ∨ . . . ∨ φn is true?

At least one statement must be true

8. What strategy would you adopt to show that the disjunction φ1 ∨ φ2 ∨ . . . ∨ φn is false?

All statements must be false

9. Simplify the following symbolic statements as much as you can, leaving your answer in a standard
symbolic form (assuming you are familiar with the notation):
(a) ¬(π > 3.2)

$x\leq3.2$

(b) ¬(x < 0)

$x\geq0$

(c) ¬(x^2 > 0)

$x=0$

if $x^2>0$, then $x$ is anything but zero since anything squared is positive. Therefore the negation is that x must be zero.

(d) ¬(x = 1)

$x\neq1$

(e) ¬¬ψ

$\phi$

a double negation is canceled out

10. Express each of your simplified statements from question 9 in natural English.

a. x is less than or equal to 3.2

b. x is greater than or equal to 0

c. x is equal to 0

d. x is not equal to 1

e. $\phi$

11. Let D be the statement “The dollar is strong”, Y the statement “The Yuan is strong” and T
the statement “New US–China trade agreement signed”. Express the main content of each of the
following (fictitious) newspaper headlines in logical notation. (Note that logical notation captures
truth, but not the many nuances and inferences of natural language.) How would you justify and
defend your answers?
(a) Dollar and Yuan both strong

$ D \land Y $

(b) Yuan weak despite new trade agreement, but Dollar remains strong

$ \lnot Y \land D \land T $

(c) Dollar and Yuan can’t both be strong at same time.

$ D \oplus Y $

another way to express this is $\lnot (D \land Y) $

(d) New trade agreement does not prevent fall in Dollar and Yuan

$ T \land (\lnot D \land \lnot Y) $

(e) US–China trade agreement fails but both currencies remain strong

$ \lnot T \land (D \land Y)$ 

TWO TO THINK ABOUT AND DISCUSS WITH OTHER STUDENTS
1. In US law, a trial verdict of “Not guilty” is given when the prosecution fails to prove guilt. This, of
course, does not mean the defendant is, as a matter of actual fact, innocent. Is this state of affairs
captured accurately when we use “not” in the mathematical sense? (i.e., Do “Not guilty” and “¬
guilty” mean the same?) What if we change the question to ask if “Not proven” and “¬ proven”
mean the same?
2. The truth table for ¬¬φ is clearly the same as that for φ itself, so the two expressions make identical
truth assertions. This is not necessarily true for negation in everyday life. For example, you might
find yourself saying “I was not displeased with the movie.” In terms of formal negation, this has
the form ¬(¬ pleased), but your statement clearly does not mean that you were pleased with the
movie. Indeed, it means something considerably less positive. How would you capture this kind of
use of language in the formal framework we have been looking at?

# Quiz

1. Is it possible for one of (ϕ∧ψ)∧θ and ϕ∧(ψ∧θ) to be true and the other false? (If not, then the associative property holds for conjunction.) [Score: 5 points]

| $\phi$ | $\psi$ | $\theta$ | (ϕ∧ψ)∧θ | ϕ∧(ψ∧θ) |
| --- | --- | --- | --- | --- |
| T | T | T | T | T |
| T | T | F | F | F |
| T | F | F | F | F |
| F | T | F | F | F |
| F | F | T | F | F |
| F | T | T | F | F |
| F | F | F | F | F |
| T | F | T | F | F |

No, all of them must be true

2. Is it possible for one of (ϕ∨ψ)∨θ and ϕ∨(ψ∨θ) to be true and the other false? (If not, then the associative property holds for disjunction.) [Score: 5 points]

| $\phi$ | $\psi$ | $\theta$ | (ϕ∨ψ)∨θ | ϕ∨(ψ∨θ)
| --- | --- | --- | --- | --- |
| T | T | T | T | T |
| T | T | F | T | T |
| T | F | F | T | T |
| F | T | F | T | T |
| F | F | T | T | T |
| F | T | T | T | T |
| F | F | F | F | F |
| T | F | T | T | T |

No

3. Is it possible for one of ϕ∧(ψ∨θ) and (ϕ∧ψ)∨(ϕ∧θ) to be true and the other false? (If not, then the distributive property holds for conjunction across disjunction.) [Score: 5 points]

| $\phi$ | $\psi$ | $\theta$ | ϕ∧(ψ∨θ) | (ϕ∧ψ)∨(ϕ∧θ)
| --- | --- | --- | --- | --- |
| T | T | T | T | T |
| T | T | F | T | F |

Yes

4. Is it possible for one of ϕ∨(ψ∧θ) and (ϕ∨ψ)∧(ϕ∨θ) to be true and the other false? (If not, then the distributive property holds for disjunction across conjunction.) [Score: 5 points]

| $\phi$ | $\psi$ | $\theta$ | ϕ∨(ψ∧θ) | (ϕ∨ψ)∧(ϕ∨θ)
| --- | --- | --- | --- | --- |
| T | T | T | T | T |
| T | T | F | T | T |
| T | F | F | T | T |
| F | T | F | F | F |
| F | F | T | F | F |
| F | T | T | T | T |
| F | F | F | F | F |
| T | F | T | T | T |

No


5. Is showing that the ¬ϕ is true equivalent to showing that ϕ is false? [Score: 5 points]

Yes, the negation of a false statement is the only thing that can be true


6. Assuming you know nothing more about Alice, which of (a) - (e)  is most likely? (Or does (f) hold?) [Score: 5 points]



r = rock star

b = bank

q = quiet

h = honest

$
r \land b\newline
q \land b\newline
q \land b\newline
h \land b\newline
b
$




(e) Alice works in a bank. Conjoining any second statement makes it less likely


7. Assuming you know nothing more about Alice, which of (a) - (e) is most likely? (Or does (f) hold?) [Score: 5 points]

r = rock star

b = bank

q = quiet

h = honest

$
r \lor b\newline
q \land b\newline
r\newline
h \land b\newline
b
$

(a) Alice is a rock star or she works in a bank.


