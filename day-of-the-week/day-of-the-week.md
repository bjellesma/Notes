The General formula to figure out the day of week for any given date is the following:

$$
\text{Day Code} = \text{Date Code} + \text{Month Code} + \text{Year Code}
$$

# Date Code

The date is simply the day number of the month. So in January 27, 2003, the date code is simply 27.

# Month Code

**Note** On leap years, January reduces to 5 and February reduces to 1. Both reduce by 1

| Month | Number | Mnemonic |
|---|---|---|
| January | 6 | WINTER has 6 letters |
| February | 2 | February is 2nd month |
| March | 2 | March 2 the beat. 
| April | 5 | APRIL has 5 letters (& FOOLS!) |
|  May | 0 | MAY-0 | 
| June | 3 | June BUG (BUG has 3 letters) |
| July | 5 | FIVERworks |
| August | 1 | A-1 Steak Sauce at picnic |
| September | 4 | FALL has 4 letters |
| October | 6 | SIX or treat! |
| November | 2 | 2 legs on 2rkey |
| December | 4 | LAST (or XMAS) has 4 letters |

# Year Code

## For years 2000 to 2003:

| Year | Number |
|---|---|
| 2000 | 0 |
| 2001 | 1 |
| 2002 | 2 |
| 2003 | 3 |

**Note** remember that 2000 is a leap year so we'll have to reduce January and February by 1 in the month codes.

## Leap Years

For every 12 years between 2000 and 2096, the last two digits of the year will be divided by 12 to give the year code:

| Year | Formula | Number |
|---|---|---|
| 2000 | 0/12 | 0 |
| 2012 | 12/12 | 1 |
| 2024 | 24/12 | 2 |
| 2036 | 36/12 | 3 |
| 2048 | 48/12 | 4 |
| 2060 | 60/12 | 5 |
| 2072 | 72/12 | 6 |
| 2084 | 84/12 | 7 |
| 2096 | 96/12 | 8 |

For years between, they also rely on a pattern as well

$$
\text{Year Code} = \text{Last 12 yr code} + 4 + \text{Number of leap years in 12 year cycle}
$$

For example, 2004 is the first year in the twelve year cycle and the previous 12 year code is zero so...

$$
\text{Year Code} = (\text{Last 12 yr code} + \text{Number of years in 12 year cycle} + \text{Number of leap years in 12 year cycle}) % 7
                
                 = (0 + 4 + 1) % 7
                 
                 = 5 % 7

                 = 5
$$

For 2032

$$
\text{Year Code} = (\text{Last 12 yr code} + \text{Number of years in 12 year cycle} + \text{Number of leap years in 12 year cycle}) % 7
                
                 = (2 + 8 + 2) % 7
                 
                 = (12) % 7

                 = 5
$$

For 2064

$$
\text{Year Code} = (\text{Last 12 yr code} + \text{Number of years in 12 year cycle} + \text{Number of leap years in 12 year cycle}) % 7
                
                 = (5 + 4 + 1) % 7
                 
                 = (10) % 7

                 = 3
$$

| Year | Formula | Number |
|---|---|---|
| 2000 | 0/12 | 0 |
| 2004 | (0+4+1)%7 | 5 |
| 2008 | (0+8+2) | 3 |
| 2012 | 12/12 | 1 |

## Years between leap years

Getting the year code for years in between these years is a simple matter of adding the number of years since the last leap year. Therefore, this will always be 1, 2, or 3. To find the year code for 2065, this is a two step approach:

1. Find the year code for the last leap year, 2065

$$
\text{Year Code} = (\text{Last 12 yr code} + \text{Number of years in 12 year cycle} + \text{Number of leap years in 12 year cycle}) % 7
                
                 = (5 + 4 + 1) % 7
                 
                 = (10) % 7

                 = 3
$$

2. Add 1 because 2065 is 1 year from the last leap year

$$
= 3 + 1
= 4
$$

## Other Centuries

Find the year code for dates in other centuries follows a simple pattern as well. This pattern follows that the dates repeat every 400 years. The pattern is as follows:

| Years since last 400 | Number |
|---|---|---|
| 0-99 | 0 |
| 100-199 | 5 |
| 200-299 | 3 |
| 300-399 | 1 |

These numbers are add to the year code determined

# Calculation

Adding these three numbers can yield a very large number which a day code won't initially solve. For any result greater than 6, we will take the modulo 7 (the remainder after dividing by 7). Since any modulo 7 number is going to be between 0 and 6, this means that we will always have a day.

# Day code

Now that we've defined the date, month, and year codes, getting the day is simply a matter of translating the day code.

| Day | Number |
|---|---|
| Sunday | 0 |
| Monday | 1 |
| Tuesday | 2 |
| Wednesday | 3 |
| Thursday | 4 |
| Friday | 5 |
| Saturday | 6 |