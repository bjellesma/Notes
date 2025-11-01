# 1 - Orbits

Different Speed with which to launch objects horizontally will launch them into orbits. 

* For a circular orbit, a speed of 7.9 km/s (17,700 mph) is needed. At this speed, the object's centrifugal force exactly balances Earth's gravitational pull.
* For an elliptical orbit, a speed between 17700 mph and 25000 mph is needed. The object's speed varies throughout the orbit - fastest at perigee (closest point), slowest at apogee (farthest point)
* For escape velocity, you must exceed 11.2km/s (25000 mph).

These speeds assume no air resistance

<img width="2409" height="1130" alt="image" src="https://github.com/user-attachments/assets/344de6ea-73b2-4d56-8c61-4fe5cd71dd44" />

Real spacecraft launch vertically first to clear the atmosphere, then pitch over to gain horizontal velocity, making the actual delta-v (change in velocity needed to perform a specific maneuver in space) requirements higher. The gravity losses from fighting Earth's pull during ascent, plus atmospheric drag, mean that the actual delta-v to reach LEO is ~9.4 km/s even though you only need ~7.8 km/s orbital velocity once you reach altitude to maintain a circular orbit. This puts the spacecraft into Low Earth Orbit (LEO).

Low Earth Orbit is 100-2000km above earth. The ISS and starlink sats are in LEO. Earlier internet satalites are in geosynchronous to maintain the same position over earth but this led to higher latency.
Medium Earth Orbit is 2000-35000 km above earth. GPS satalites are in MEO. GPS doesn't need satellites to stay in one place (Geosynchronis) - it needs multiple satellites visible from different angles to triangulate your position. Having them orbit means each satellite covers different areas throughout the day, and the constellation as a whole provides continuous global coverage.
Geosynchronis Orbit is 35786 km above Earth and is where weather satallites are. These stay over the same spot on earth at all times.

Rockets must be launched with some horizontal speed in order to enter orbit. Satellites orbiting Earth are in freefall and must have tremendous horizontal speed so they continuously miss hitting the ground. 

The International Space Station orbits only 400 km (250 miles) above the Earth's surface.   At this distance, the Earth's gravity is only slightly weaker compared to on Earth's surface.   It appears that astronauts on the ISS are weightless because they are in freefall.

The definition of where space starts is 100 km, known as the **Kármán line**, but the atmosphere gets thinner the higher up you go. For example, at 6 km above sea level the air gets so thin that it's hard to breathe. Mount Everest (8.8 km) extends well above this point, so climbers typically spend weeks trying to acclimate to these higher altitudes. There are still tiny traces of atmosphere up to 1000 km above Earth.

<img width="880" height="628" alt="image" src="https://github.com/user-attachments/assets/20588de8-d2db-4974-ac91-28d0959a8a67" />

## Kepler's Three Laws of Planetary Motion

1. Law of Ellipses (Orbit Shape)

All orbits are ellipses with the Sun at one focus
Not perfect circles - though some orbits are nearly circular
The two key points: perihelion (closest approach) and aphelion (farthest point)
Applies to any orbiting body: planets around stars, moons around planets, satellites around Earth

2. Law of Equal Areas (Orbital Speed)

A line from the Sun to a planet sweeps out equal areas in equal times
This means: objects move faster when closer, slower when farther away
Example: Earth moves fastest in January (perihelion), slowest in July (aphelion)
Why: Conservation of angular momentum

3. Law of Periods (Orbital Time)

The square of the orbital period is proportional to the cube of the semi-major axis. The semi-major axis is half the longest diameter of an ellipse - basically the average distance from the center of the orbit to the object being orbited.
T² ∝ a³ (where T = orbital period, a = average distance from Sun) (∝ means is proportional to). This often applied to a planet orbiting the sun where the mass of the sun is M so a³ = T²M. Kepler proposed this equation but didn't understand that this is only a special case with Earth's gravity. Newton expanded on this equation to introduce the gravitational constant and apply this more generally as a³ = T² × (GM/4π²)
Simple version: Farther orbits take longer, but not linearly
Example: Mars is 1.5x farther than Earth, but takes 1.88 years to orbit (not 1.5 years)
- If Mars is 1.5× farther from the Sun than Earth...
- Then (1.5)³ = 3.375 for the distance term...
- So Mars's year² should be 3.375× Earth's year²...
- Therefore Mars's year = √3.375 = 1.84 Earth years (close to actual 1.88!)

Lets us calculate orbital periods if we know distances (or vice versa)
