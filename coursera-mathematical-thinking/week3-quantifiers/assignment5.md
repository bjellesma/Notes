1. Express the following as existence assertions. (Feel free to use a mix of symbols and words.)
(a) The equation x^3 = 27 has a natural number solution.

$\exists x \in \N[x^3=27]$

(b) 1,000,000 is not the largest natural number.

$\exists x[x \gt 1000000]$

(c) The natural number n > 1 is not a prime.

$(\exists n \gt 1)[\exists q \in \N][q \text{ divides } n]$

2. Express the following as ‘for all’ assertions (using symbols and words):
(a) The equation x^3 = 28 does not have a natural number solution.

$(\forall x \in \N)[x^3 \ne 28]$

(b) 0 is less than every natural number.

$\forall n \in N[n \gt 0]$

(c) The natural number n > 1 is a prime.

$(\forall p \gt 1 \land p \in \N)(\forall q \in \N)[n = pq \implies p = 1 \lor q = 1]$

3. Express the following in symbolic form, using quantifiers for people:
(a) Everybody loves somebody.

$(\forall p \in P)(\exists p_2 \in P[L(p, p_2) \text{ denotes "p loves } p_2 \text{"}]$

(b) Everyone is tall or short.

$\forall p \in P[p=\text{tall } \lor \text{short}]$

(c) Everyone is tall or everyone is short.

$\forall p \in P[p=\text{tall}]\lor \forall p \in P[p=\text{short}]$

(d) Nobody is at home.

$\forall p \in P[p \ne \text{home}(p)]$

(e) If John comes, all the women will leave.

$\text{John comes} \implies \forall w \in W[w \implies \text{leaves}(w)]$

(f) If a man comes, all the women will leave.

$\exists m \in M[Man(m)=\text{comes}]] \implies \forall w \in W[Woman(w) = \text{leaves}]$

4. Express the following using quantifiers that refer (only) to the sets R (real numbers) and N (natural numbers):
(a) The equation x^2 + a = 0 has a real root for any real number a.

$(\forall a \in \R)(\forall x \in \R)[x^2+a=0]$

(b) The equation x
2 + a = 0 has a real root for any negative real number a.

$(\forall a \in \R)[a \lt 0) \implies \exists x[x^2+a=0]]$

(c) Every real number is rational.

$\forall r \in \R(r = \frac{p}{q} \in \Z \land q \ne 0)$

(d) There is an irrational number.

$\exists n[\frac{p}{q} \notin \Z]$

(e) There is no largest irrational number. (This one looks quite complicated.)

$(\forall n \in \N)(\exists m)(\nexists p \gt m[m \gt n]$

5. Let C be the set of all cars, let D(x) mean that x is domestic, and let M(x) mean that x is badly
made. Express the following in symbolic form using these symbols:
(a) All domestic cars are badly made.

$\forall x \in C[D(x)=M(x)]$

(b) All foreign cars are badly made.

$(\forall x \in C)[D(x) \ne M(x)]$

(c) All badly made cars are domestic.

$\forall x \in C[M(x) \implies D(x)]$

(d) There is a domestic car that is not badly made.

$(\forall x \in C)(\exists x \in D(x)[x \ne M(x)]$

(e) There is a foreign car that is badly made.

$(\forall x \in C)(\exists x \notin D(x)[x \ne M(x)]$

6. Express the following sentence symbolically, using only quantifiers for real numbers, logical connectives, the order relation < , and the symbol Q(x) having the meaning ‘x is rational’:
You can find a rational number between any two unequal real numbers.

$(\exists n \in \N()[n = \frac{p}{q} \land p \lt n \lt q]$

7. Express the following famous statement (popularly, but falsely, believed to be due to Abraham
Lincoln) using quantifiers for people and times: “You may fool all the people some of the time, you
can even fool some of the people all of the time, but you cannot fool all of the people all the time.”




8. A US newspaper headline read, “A driver is involved in an accident every six seconds.” Let x be
a variable to denote a driver, t a variable for a six second interval, and let A(x, t) be the property
that x is in an accident during interval t. Express the headline (as written) in logical notation.
9. Rewrite the headline so that its literal meaning is what the headline writer was trying to convey,
and express your revised version in logical notation.