1. Express the relationship of $b|a$ and $a/b$

$b|a$ is a relationship stating the b divides a and acts over the set of integers, a fact that can't be disputed. $a/b$ is an operation saying aa divided by b and is acting over the set of real numbers. 

2. True of False. Prove your answer.
    1. $0|7$ is false because 0 can't be the divisor.
    2. $9|0$ is true because $\exists q[0=9q]$
    3. $0|0$ is false because 0 can't be the divisor.
    4. $1|1$ is true because $\exists q[1=1q]$
    5. $7|44$ is false because 7 can't go into 44. Even can't go into odd.
    6. $7|-42$ is true because $\exists q[-42=7q]$
    7. $-7|49$ is true because $\exists q[49=-7q]$
    8. $-7|-56$ is true because $\exists q[-56=-7q]$
    9. $\forall n \in \Z[1|n]$ is true because the first property of division says $a|0, a|a$. What was getting me was the order. $1|n$ means that $\exists q[n=-1q]$ which holds because there will be a q for every n to satisy this.
    10. $\forall n \in \N[n|0]$ is true because the first property of division says $a|0, a|a$ and the set of natural numbers doesn't include zero
    11. $\forall n \in \Z[n|0]$ is false because the set of integers includes zero.

3. Prove all parts of the basic properties of division:
    1. $a|0, a|a$

    $\exists q \in \Z[0=qa]$ by definition. Also by definition, $\exists q\in \Z[a=qa]$

    2. $a|1$ iff $a=\pm 1$

    $a=\pm 1 \implies a|1$ because $-1|1$ and $1|1$ both work by the definition of division.

    $a|1 \implies a=\pm 1$ because if q is 1, a can only be 1 and if q is -1, a can only be -1

    3. if $a|b$ and $c|d$, then $ac|bd$ provided $c \ne 0$

    By the definition, there are integer q, r such that b=qa and d=rc. Hence, $bd = (qa)(rc)=(qr)(ac)$. This is the definition of division because it's saying there is some integer qr such that bd=(qr)(ac)

    4. if $a|b$ and $b|c$, then $a|c$ provided $b \ne 0$

    $\exists d,e[b=da \text{ and } c=eb$ (By the definition of division). So, $c=e(da)$ which, by the definition of division, means $a|c$

    5. $a|b$ and $b|a$ if and only if $a=\pm b$
    6. if $a|b$ and $b \ne 0$, the $|a| \le |b|$

    Since $a|b$, $\exists d[b=da]$ (by the definition of division) and $|b|=|d||a|$. Since $b \ne 0$, $|d| \ge 1$ and $|a| \le |b|$

    7. if $a|b$ and $a|c$, then $a|(bx+cy)$ for any integers x, y