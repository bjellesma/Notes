# Divisibility Theorem

What does it mean to say that <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{a}{b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{a}{b}" title="\frac{a}{b}" /></a> is an integer? 

It means that a can be represented as a product of two integers, b and some other integer k so that <a href="https://www.codecogs.com/eqnedit.php?latex=\text{a}&space;=&space;\text{b}&space;*&space;\text{k}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\text{a}&space;=&space;\text{b}&space;*&space;\text{k}" title="\text{a} = \text{b} * \text{k}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{a}{b}&space;=&space;\frac{b&space;*&space;k}{b}&space;=&space;k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{a}{b}&space;=&space;\frac{b&space;*&space;k}{b}&space;=&space;k" title="\frac{a}{b} = \frac{b * k}{b} = k" /></a>

## Examples

15 is divisible by 3 because we can pick k = 5 and 3 * 5 = 15

12 is divisible by -4 because k = -3 where (-4) * (-3) = 12

-24 is divisible by -6 because (-6) * 4 = -24

0 is divisible by 0 because 0 * *any integer* = 0

## Lemma

If c divides a and c divides b, then c divide <a href="https://www.codecogs.com/eqnedit.php?latex=a&space;\pm&space;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a&space;\pm&space;b" title="a \pm b" /></a>

### Examples

c = 2, b = 4, a = 6. 2 divides 4 and 6, 2 divides 10, and 2 divides 2

## Division with remainders

Suppose b is a possitive integer. The result of the devision of a by b with a remainder is a pair of itegers, q called quotient and r called a remainder such that <a href="https://www.codecogs.com/eqnedit.php?latex=a&space;=&space;q&space;*&space;b&space;&plus;&space;r&space;where&space;0&space;\leq&space;r&space;<&space;b" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a&space;=&space;q&space;*&space;b&space;&plus;&space;r&space;where&space;0&space;\leq&space;r&space;<&space;b" title="a = q * b + r where 0 \leq r < b" /></a>

Note that if r is 0, then b divides a

To represent this programmatically, subtract b from a recursively until the result is less than b; the result is remainder r and the number of subtractions is q.

### Example

a = 15, b = 4. Then 15 = 3 * 4 + 3. q = 3 and r = 3

a = -13, b = 3. Then -13 = -5 * 3 + 2. q = -5 and r = 2 

Suppose a is not divisible by 2 (a is odd). What possible remainders can a have when divided by 4?

1

Correct 
This is correct! An example of aa with this remainder is a=1a=1. See the discussion of the problem in the next video.


3

Correct 
This is correct! An example of aa with this remainder is a=3a=3. See the discussion of the problem in the next video.

How many 3-digit non-negative numbers are there that have remainder 7 when divided by 101? Here we assume that 1-digit and 2-digit numbers are also 3-digit, they just start with 0.

The equation we are dealing with is a = 7 + q * 101. Note that if q is negative, then a will be negative, which is a contridiction, therefore q can only be positive. The least integer that q can be is 0 and the final integer that q can be and still yield a 3 digit value is 9, therefore all of the integers between 0 and 9 are valid. The answer is 10 numbers.

Is it true that for any four integers aa, bb, cc, dd there are two of them whose difference is divisible by 3?

There are only 3 possible remainders when dividing by 3: 0, 1, and 2. Therefore, if we divide any two of the above numbers by 3, at least two of the numbers will have the same remainder. Furthermore, If you subtract these two numbers that have the same remainer, the result is divisible by three

### Lemma

Suppose we divide a by 10 with a remainder. Then the remainder is the last digit of a and the quotient is the number formed by all digits of a except the last one.

#### Corollary

An integer a is divisible by 10 iff its last digit is 0

### Question

What is the quotient and remainder of 7347/5?
```
7347 = 7340+7 = 734 * 10 + 7 = (734*2)*5+(5*1)+2 = (1468+1)*5+2 = 1469*5+2
```

therefore, the quotient is 1469 and the remainder is 2
