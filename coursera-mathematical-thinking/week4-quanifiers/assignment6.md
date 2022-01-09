1. Show that $\neg [\exists x A(x)] \leftrightarrow \forall x [ \neg A(x)]$. Give an everyday example.

if we assume there is not at least one x that makes A(x) true, then for all x, A(x) must be false.

If it's not true that at least one car is well made, then it is the case that for all cars, they are poorly made.

2. Prove that the following statement is false:
There is an even prime bigger than 2

If we assume $\exists x \gt 2[P(x) \land \neg O(x)]$ then $\neg (\forall x \gt 2)[P(x) \implies O(x)]$ (it's not the case that for all x greater than 2, being prime implies being odd). Th

$\exists x \gt 2 [P(x) \not \implies O(x) \leftrightarrow \neg \forall x \gt 2 [ P(x) \implies O(x)]$

TODO: Stuck

3. Translate the following sentences into symbolic form using quantifiers. In each case the assumed
domain is given in parentheses.
(a) All students like pizza. (All people)

$\forall x(P(x))$

(b) One of my friends does not have a car. (All people)

$\forall x \exists y(y \implies \neg C(x))$

(c) Some elephants do not like muffins. (All animals)

$\forall x \exists y(y \implies\neg M(x))$

(d) Every triangle is isosceles. (All geometric figures)

$\forall x (T(x) and I(x))$

(e) Some of the students in the class are not here today. (All people)

$\forall x \in P \exists y \in S(\neg x)$

(f) Everyone loves somebody. (All people)

$\forall x \in P \exist y \in p(L(x, y))$

(g) Nobody loves everybody. (All people)

$\forall x \in P \neg \exist y \in p  (L(y, x))$

(h) If a man comes, all the women will leave. (All people)

$\exists x \in P \forall y \in p  (L(y))$

(i) All people are tall or short. (All people)

$\forall x \in P (S(x) \lor T(x))$

(j) All people are tall or all people are short. (All people)

$\forall x \in P (T(x)) \lor \forall x \in P(S(x))$

(k) Not all precious stones are beautiful. (All stones)

$\neg \forall x \in S(P(x) \land B(x))$

(l) Nobody loves me. (All people)

$\forall x \in P \exist y \in p  (\neg L(x, y))$

(m) At least one American snake is poisonous. (All snakes)

$\exists x \in S (A(x) \land P(x))$

(n) At least one American snake is poisonous. (All animals)

$\exists x \in A_n (S(x) \land A(x) \land P(x))$

4. Negate each of the symbolic statements you wrote in the last question, putting your answers in
positive form. Then express each negation in natural, idiomatic English.

(a) All students like pizza. (All people)

$\neg \forall x(P(x))$

It's not the case that all students like pizza

(b) One of my friends does not have a car. (All people)

$\forall x \in P(F(x) \land C(x))$

all of my friends have a car

(c) Some elephants do not like muffins. (All animals)

$\forall x \in A \exists y \in A(E(x)M(x))$

Some elephants like muffins

(d) Every triangle is isosceles. (All geometric figures)

$\forall x (T(x) and I(x))$

(e) Some of the students in the class are not here today. (All people)

$\forall x \in P \exists y \in S(\neg x)$

(f) Everyone loves somebody. (All people)

$\forall x \in P \exist y \in p(L(x, y))$

(g) Nobody loves everybody. (All people)

$\forall x \in P \neg \exist y \in p  (L(y, x))$

(h) If a man comes, all the women will leave. (All people)

$\exists x \in P \forall y \in p  (L(y))$

(i) All people are tall or short. (All people)

$\forall x \in P (S(x) \lor T(x))$

(j) All people are tall or all people are short. (All people)

$\forall x \in P (T(x)) \lor \forall x \in P(S(x))$

(k) Not all precious stones are beautiful. (All stones)

$\neg \forall x \in S(P(x) \land B(x))$

(l) Nobody loves me. (All people)

$\forall x \in P \exist y \in p  (\neg L(x, y))$

(m) At least one American snake is poisonous. (All snakes)

$\exists x \in S (A(x) \land P(x))$

(n) At least one American snake is poisonous. (All animals)

$\exists x \in A_n (S(x) \land A(x) \land P(x))$

5. Which of the following are true? The domain for each is given in parentheses.

(a) ∃x(2x + 3 = 5x + 1) (Natural numbers)

False

x would need to be 2/3

(b) ∃x(x^2 = 2) (Rational numbers)

False

Root 2 is irrational
(c) ∀x∃y(y = x^2) (Real numbers)

True

(d) ∀x∃y(y = x^2) (Natural numbers)

False

y would need to be a fraction

(e) ∀x∃y∀z(xy = xz) (Real numbers)

Yes. Y needs to be 1

(f) ∀x∃y∀z(xy = xz) (Prime numbers)

No. Y needs to be 1

(g) ∀x[x < 0 ⇒ ∃y(y^2 = x)] (Real numbers)

True

(h) ∀x[x < 0 ⇒ ∃y(y^2 = x)] (Positive real numbers)

False, x needs to be zero

6. Negate each of the statements in the last question, putting your answers in positive form.

(a) ∃x(2x + 3 = 5x + 1) (Natural numbers)

$\neg \forall x (2x+3=5x+1)$

x would need to be 2/3

(b) ∃x(x^2 = 2) (Rational numbers)

False

Root 2 is irrational
(c) ∀x∃y(y = x^2) (Real numbers)

True

(d) ∀x∃y(y = x^2) (Natural numbers)

False

y would need to be a fraction

(e) ∀x∃y∀z(xy = xz) (Real numbers)

Yes. Y needs to be 1

(f) ∀x∃y∀z(xy = xz) (Prime numbers)

No. Y needs to be 1

(g) ∀x[x < 0 ⇒ ∃y(y^2 = x)] (Real numbers)

True

(h) ∀x[x < 0 ⇒ ∃y(y^2 = x)] (Positive real numbers)

False, x needs to be zero

7. Negate the following statements and put each answer into positive form:

(a) (∀x ∈ N )(∃y ∈ N )(x + y = 1)

$(\exists x \in N)(\forall y \in N)\neg (x+y = 1)$

(b) (∀x>0)(∃y <0)(x + y = 0) (where x, y are real number variables)

$(\exists x>0)(\forall y <0)(x + y \neq 0)$

(c) $∃x(∀ \epsilon > 0)(− \epsilon < x < \epsilon)$ (where x,  are real number variables)

$\forall x(\exists \epsilon \gt 0)(x \leq - \epsilon \lor x \geq \epsilon)$

because the statement before the negation is technically and and, we use an or in the negation

(d) (∀x ∈ N )(∀y ∈ N )(∃z ∈ N )(x + y = z^2)

$(\exists x \in N)(\exists y \in N)(\forall z \in N)\neg(x+y=z^2)$

8. Give a negation (in positive form) of the famous “Abraham Lincoln sentence” which we met in the
previous assignment: “You may fool all the people some of the time, you can even fool some of the
people all of the time, but you cannot fool all of the people all the time.”



9. The standard definition of a real function f being continuous at a point x = a is
(∀ > 0)(∃δ > 0)(∀x)[|x − a| < δ ⇒ |f(x) − f(a)| < ]
Write down a formal definition for f being discontinuous at a. Your definition should be in positive
form.