1. Say which of the following are true. (Leave the box empty to indicate that it’s false.)

• A set A of reals can have at most one least upper bound.

True

• If a set A of reals has a lower bound, it has infinitely many lower bounds.

True

• If a set A of reals has both a lower bound and an upper bound, then it is finite.

False

• 0 is the least upper bound of the set of negative integers, considered as a subset of the reals.

True. Negative integers are $(-\infty, 0)$

TODO: this is false

2. Which of the following say that b is the greatest lower bound of a set A of reals? (Leave the box
empty to indicate that it does not say that.)

• b ≤ a for all a ∈ A and if c ≤ a for all a ∈ A, then b ≥ c.

True. If it's for all

• b ≤ a for all a ∈ A and if c ≤ a for all a ∈ A, then b > c.

TODO: This is false

True. If it's for all. Closed or open set shouldn't matter

• b < a for all a ∈ A and if c < a for all a ∈ A, then b ≥ c.

False. b must be in A.

• b < a for all a ∈ A and if c ≤ a for all a ∈ A, then b ≥ c.

False. b must be in A.

• b ≤ a for all a ∈ A and if $\epsilon$ > 0 there is an a ∈ A such that a < b + $\epsilon$.

True.

3. The Sandwich Theorem (also sometimes called the Squeeze Theorem) says that if {an}∞
n=1, {bn}∞
n=1,
{cn}∞
n=1 are sequences such that, from some point n0 onwards,
an ≤ bn ≤ cn,
and if
limn→∞
an = L , limn→∞
cn = L,
then {bn}∞
n=1 is convergent and
limn→∞
bn = L.
Taking the Sandwich Theorem to be correct (which it is), grade the following proof using the course
rubric.
Theorem limn→∞
sin2 n
3
n
= 0
Proof: For any n,
0 ≤
sin2 n
3
n
≤
1
3
n
Clearly, limn→∞
1
3
n
= 0. Hence, by the Sandwich Theorem,
limn→∞
sin2 n
3
n
= 0
as required.

This theorem doesn't prove anything. It just uses the squeeze theorem and applies it.

TODO: This proof was given a full 24 points

4. Is the following proof of the Sandwich Theorem correct? Grade it according to the course rubric.
Theorem (Sandwich Theorem) Suppose {an}∞
n=1, {bn}∞
n=1, {cn}∞
n=1 are sequences such that, from
some point n0 onwards,
an ≤ bn ≤ cn.
Suppose further that
limn→∞
an = L , limn→∞
cn = L.
Then {bn}∞
n=1 is convergent and
limn→∞
bn = L.
Proof: Since limn→∞
an = L, we can find an integer n1 such that
n ≥ n1 ⇒ |an − L| < 
Since limn→∞
cn = L, we can find an integer n2 such that
n ≥ n2 ⇒ |cn − L| < 
Let M = max{n0, n1, n2}. Then
n ≥ M ⇒ (− < an−L < ) ∧ (− < cn−L < )
⇒ − < an−L ≤ bn−L ≤ cn−L <  (using an ≤ bn ≤ cn)
⇒ − < bn−L < 
⇒ |bn − L| < 
By the definition of a limit, this proves that {bn}∞
n=1 is convergent and limn→∞
bn = L, as required.

20 points. This has very sound logic. I'm just a little confused how the proof got to introducing one step

TODO: This grade is good. The student is just missing the initial assumption.

5. Evaluate this purported proof, and grade it according to the course rubric.
Theorem limn→∞
n + 1
2n + 1
=
1
2
.
Proof: Let  > 0 be given. Choose N large enough so that N ≥
1
2
.
Then, for n ≥ N,




n + 1
2n + 1
−
1
2



 =




2(n + 1) − (2n + 1)
2(2n + 1)




=




1
2(2n + 1)




=
1
2(2n + 1)
<
1
2n + 1
<
1
2n
≤
1
2N
≤ 
By the definition of a limit, this proves the theorem.

10 points. This is a serious logic hole because why did the equal change to less than

TODO: The proof was givin full marks
