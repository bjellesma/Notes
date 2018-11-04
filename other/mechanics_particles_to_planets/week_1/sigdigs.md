To figure out the number of seconds in 1 year we use:

<img src="https://latex.codecogs.com/gif.latex?1&space;yr&space;=&space;365.24&space;day&space;*&space;\frac{24&space;hours}{1&space;day}&space;*&space;\frac{3600&space;seconds}{1&space;hour}&space;=&space;31556736&space;seconds" title="1 yr = 365.24 day * \frac{24 hours}{1 day} * \frac{3600 seconds}{1 hour} = 31556736 seconds" />

Then, we want to convert this to the number of seconds in 14 billion years

<img src="https://latex.codecogs.com/gif.latex?14&space;x&space;10^9&space;yr&space;=&space;14*10^9&space;yr&space;*&space;\frac{31556736&space;sec}{1&space;yr}&space;=&space;4.4*10^{17}&space;sec" title="14 x 10^9 yr = 14*10^9 yr * \frac{31556736 sec}{1 yr} = 4.4*10^{17} sec" />

Notice that we use `4.4 * 10^17` because we started with `14 * 10^9` so both 4.4 and 14 have two significant digits*

The sketch is a cross section through the earth, showing two points that have a difference in latitude of angle <img src="https://latex.codecogs.com/gif.latex?\theta" title="\theta" />. The mean radius RR of the earth is `6.371 * \ 10^6`
 meters. A nautical mile is defined as 1852 meters exactly. Using these data, calculate how many nautical miles there are between two points on the earth's surface that have the same longitude but have latitudes that differ by 1.000 degree. (Just in case: the definition of angle, in radians, is the arc of a circle it subtends divided by the radius of the circle. A circle is 2π radians or 360∘.)

Because we want to find the distance between two points on a circle, we want to use the arc length formula

<img src="https://latex.codecogs.com/gif.latex?s&space;=&space;r\Theta" title="s = r\Theta" />

We know that radius is <img src="https://latex.codecogs.com/gif.latex?6.371&space;*&space;10^{6}" title="6.371 * 10^{6}" />

and theta is

<img src="https://latex.codecogs.com/gif.latex?2\pi&space;=&space;360\degree&space;\therefore&space;\frac{2\pi}{360\degree}&space;=&space;\frac{360\degree}{360\degree}&space;=&space;1\degree" title="2\pi = 360\degree \therefore \frac{2\pi}{360\degree} = \frac{360\degree}{360\degree} = 1\degree" />

Finally, we want a conversion to nautical miles

<img src="https://latex.codecogs.com/gif.latex?\frac{1&space;nautical&space;mile}{1852&space;meters}" title="\frac{1 nautical mile}{1852 meters}" />

So, our final equation is

<img src="https://latex.codecogs.com/gif.latex?s&space;=&space;r\theta&space;=&space;(6.371&space;*&space;10^{6}&space;meters)(\frac{2\pi}{360\degree})(\frac{1&space;nautical&space;mile}{1852&space;meters})&space;=&space;(6.371&space;*&space;10^{6}&space;meters)(1.74532&space;*&space;10^{-2})(\frac{1&space;nautical&space;mile}{1852&space;meters})&space;=&space;(11.1194&space;*&space;10^{4}&space;meters)(\frac{1&space;nautical&space;miles}{1852&space;meters})&space;\simeq&space;60.04&space;nautical&space;miles" title="s = r\theta = (6.371 * 10^{6} meters)(\frac{2\pi}{360\degree})(\frac{1 nautical mile}{1852 meters}) = (6.371 * 10^{6} meters)(1.74532 * 10^{-2})(\frac{1 nautical mile}{1852 meters}) = (11.1194 * 10^{4} meters)(\frac{1 nautical miles}{1852 meters}) \simeq 60.04 nautical miles" />
