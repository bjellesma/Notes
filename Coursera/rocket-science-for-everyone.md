# 1 - Introduction

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

#2 - Orbits

## Low earth orbit

All astronauts since Apollo ended have only ever been to LEO.

There are tiny amounts of atmosphere still in low earth orbit and so when satalites bump into these little pockets, they lose energy and slowly fall back to Earth. This is known as **atmostpheric drag**. Because of this, the international space station actually needs to account for this every couple of months and needs to be boosted by a rocket to overcome this drag.

Different orbital inclinations would be when one satalite orbits the equator and one orbits the poles for example. Even satalites with a different orbital inclination can still hit each other and for this reason they are often orbiting at different times known as the **orbital phase** (obbital phase refers to where a satellite is along its orbital path at a given time) so that they don't bump into each other <img width="1433" height="890" alt="image" src="https://github.com/user-attachments/assets/d7d3a8c3-8846-46a0-8673-4253aad3dd7c" />

We can calculate the speed of Hubble because we know the orbital period as well as the distance that it covers (the circumference of a circle since it's in a circular orbit). This comes out to about 17,000mph <img width="1719" height="756" alt="image" src="https://github.com/user-attachments/assets/46f23d5b-0c98-4eb2-97d2-ddd7bd841e7d" />

The **Kessler Effect** is a term used to describe the fact that if two objects collide and create debris, that debris will cause other collisions. 

## Medium Earth Orbit

Regions where radiation hits around Earth are known as the **Van Allen Belts**. These are regions where Earth's magnetic field traps charged particles from solar wind. There are two main belts: inner (roughly 1,000-6,000 km) and outer (13,000-60,000 km). <img width="974" height="497" alt="image" src="https://github.com/user-attachments/assets/cd506680-6b22-46c4-8d41-ddbe579a66e1" /> MEO and GPS satellites operate at about 20,200 km altitude, which places them between the two Van Allen Belts, helping avoid the worst radiation.

Most MEO satellites are used for navigation like GPS (though in recent years, there have been satellites launched into MEO with functions beyond navigation) and are at an altitude of about 20,000km. Using Kepler's laws, we get that most of these satallites have an orbital period of 12 hours. This is deliberate because this means that the satellites will orbit the Earth twice. GPS works through **trilateration** - measuring distances from multiple satellites to determine your location. Here's how it builds up:

One satellite: Tells you that you're somewhere on a sphere at a specific distance from that satellite - but that's a huge area.
Two satellites: Where two spheres intersect creates a circle. You're somewhere on that circle.
Three satellites: Three spheres intersect at two points. One is usually in space or underground, so we can often rule it out, but we need more precision.
Four satellites: This fourth satellite is essential for two reasons. First, it resolves any ambiguity about which intersection point is correct. Second, and critically, it provides precise timing synchronization. GPS depends on incredibly accurate time measurements (signals travel at light speed), and the fourth satellite helps correct for clock errors in your receiver. It also accounts for relativistic effects - GPS satellites experience time differently due to both their speed (special relativity) and reduced gravity at their altitude (general relativity). <img width="1739" height="993" alt="image" src="https://github.com/user-attachments/assets/74887046-1d4a-4f3c-8c1d-feb64f8fb4a5" />

Technically a forth satellite is needed to get the exact time and account for relativistic effects. But this means now that GPS requires four satellites to be in view at all times. 

The GPS network overseen by the department of defence runs 32 satellites and ensures that 7-8 are in view at all times ensuring that there is some redundancy built in.

Other countries actually have their own GPS systems. <img width="1919" height="988" alt="image" src="https://github.com/user-attachments/assets/886a9863-c927-41c4-877e-aa4a841b4fc5" />

## Geosynchronous and Geostationary Orbits

Geosynchronous orbital periods are 24 hours so that it's synchronized with the Earth while geostationary orbit is an exact circular orbit above the equator where objects will appear to "hover" in the same spot above the Earth (though it technically is not). 

DirectTV and Dish network work by communicating with Geostationary satellites.

Many NOAA satellites will use Geostationary orbit for weather monitoring <img width="2176" height="1025" alt="image" src="https://github.com/user-attachments/assets/1fe6403d-9fcf-4a6b-a433-797e6c607bd2" />

When Satellites in GEO reach the end of their functional life, they can't ever be deorbited back to Earth (because of no atmospheric drag and the delta v required to get them back would be infeasible) so often they are nudge to a higher "graveyard" orbit which requires them to have fuel left over.

## Orbital Summary

90% of satellites are in LEO, 3% are in MEO, 7% are in GEO. 

60-70% of satellites are for communication, 20% are for Earth observation (weather), and 3% are for navigation. Other satellites are used for things like technology development and taking images away from Earth.

<img width="2370" height="964" alt="image" src="https://github.com/user-attachments/assets/dfe809fa-5002-4571-974a-9be73c3b318c" />

## Special Orbits

### Polar Orbits

Goes over the poles of the Earth, usually 600km from Earth. <img width="1030" height="1015" alt="image" src="https://github.com/user-attachments/assets/3a487e58-0608-4f5d-9fbd-75475dfa87ac" />

These are opposed to **equatorial orbits** which just go around the equator. <img width="1130" height="806" alt="image" src="https://github.com/user-attachments/assets/5ebaa904-a10b-4a58-b96d-ae80f84a892b" /> 

and **inclined orbits** which just have a tilt <img width="1057" height="909" alt="image" src="https://github.com/user-attachments/assets/6fe1325a-56d3-4547-8533-4362acc3d8c6" />

The advantage with a **polar orbit** is that as the Earth rotates, satellites in a polar orbit will be able to see more of the Earth during each orbital period. <img width="1063" height="902" alt="image" src="https://github.com/user-attachments/assets/fa553c25-bd79-4d70-905f-8ffcb9a26271" />

In an inclined orbit, you're never able to see the areas of the Earth around the poles. <img width="1078" height="692" alt="image" src="https://github.com/user-attachments/assets/c5f5ed8e-13f8-4bdf-9961-1843214d3f04" />



### Sun sychronous orbits

Special type of polar orbit.

Though this is still in LEO (600-800km) with a retrograde inclination (97-100%), this is able to pass over the same spot on earth at the same time each day. This is done because the satellites orbital plane rotates at exactly 360 degrees per year (matching earth's orbit around the sun).

### Beyond GEO

The **cislunar orbit** lies between GEO (~36000km) and the moon (400,000km)

## Getting into Orbits

If you launch vertically, you can reach **escape velocity** (25,000mph) which will escape Earth's gravity entirely but this is more than would be needed for orbit. A **suborbital flight** will just launch straight up so that it just barely passes the karmin line but can't make it to orbit because there's not enough horizontal motion to complete an orbit. Furthermore, because it just launches straight up, it will be pulled back down by Earth's gravity (unless it reaches that high speed).  

To achieve orbit, there has to be some degree of horizontal motion. Most orbital rockets will launch vertically to both clear the launch tower and clear the thickest part of the atmosphere. Once a rocket can clear this part of the atmosphere, it becomes easier to accelerate as there is less drag. The point at which the thickest part of the atmosphere is crossed is known as **Max Q (maximum dynamic pressure)**. Once a rocket passes max q (this can be notoriously difficult as you see on webcasts), it can begin to have more of its velocity go toward the horizontal direction. The speed need to achieve orbit is known as **orbital velocity** and is around 17,000mph.

## Keppler's Laws deep dive

### 3rd Law

$$
a^3 = \frac{G}{4\pi^2} P^2 M
$$

where a is the semi major axis, G is the gravitational constant, P is the orbital period, and M is the mass of the object being orbited. 

$$
\begin{align}
\text{How high above Earth's surface did Sputnik orbit?} \nonumber \\
a^3 &= \frac{G}{4\pi^2} P^2 M \\
a^3 &= \frac{G}{4\pi^2} (96.2 \text{ min})^2 (6.0 \times 10^{24} \text{ kg}) \\
\text{Add constants with units:} \nonumber \\
a^3 &= \frac{6.7 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}}{4\pi^2} (96.2 \text{ min})^2 (6.0 \times 10^{24} \text{ kg}) \\
\text{Check units:} \nonumber \\
a^3 &= \frac{6.7 \times 10^{-11} \text{ m}^3 \text{ kg}^{-1} \text{ s}^{-2}}{4\pi^2} \left(96.2 \text{ min} \times \frac{60 \text{ s}}{1 \text{ min}}\right)^2 (6.0 \times 10^{24} \text{ kg}) \\
a^3 &= 3.4 \times 10^{20} \text{ m}^3
\end{align}
$$

The cubed root of this comes out to about 7000km. This is just the semi major axis of the earth so to get the height of sputnick above Earth's surface, we need to subtract the radius of the Earth.

<img width="1088" height="493" alt="image" src="https://github.com/user-attachments/assets/2b8e4635-c73b-420c-9ea3-dc49701c177a" />

# Module 3: Rockets

The speed needed by a rocket are determined by the destination of the rocket as well as the mass of the payload.

The motion of the rocket are governed by Newton's laws of motion.
1. An object at rest stays at rest unless acted on by a force
2. F=Ma. This directly applies to rockets because the more massive the payload, the more force will be needed.
3. Every action has an equal and opposite reaction

Jet Engines work by intaking air, combusting, and outputting hot air to thrust it forward. <img width="1764" height="938" alt="image" src="https://github.com/user-attachments/assets/16ee3a53-425c-44ca-8d63-154e96462f22" />

Because there's no air in space, we can't use a jet engine in space. 

## Chemical Rockets

The rockets used to launch all objects into orbit are **chemical rockets**. Chemical rockets use a **fuel** and and **oxidizer**. Together these are called the **propellant**. 

There are two main types of chemical rockets.

**Liquid Rocket Engines** have fuel and oxidizer stored separately in their liquid forms. These are combined in the combustion chamber just before ignition. <img width="1874" height="963" alt="image" src="https://github.com/user-attachments/assets/cd0711d8-6d5d-4e83-8249-b64182a16462" />

A lot of research has gone into finding the best combination of fuel and oxidizer. <img width="1195" height="537" alt="image" src="https://github.com/user-attachments/assets/725dea5d-edcf-45fa-b16d-0d2ea7d6fa7b" />

The fuel in an airplane is 30% of the total mass. The fuel in a rocket is over 90%.

**Solid Rocket Motors** have fuel and oxidizer mixed into a single solid and stored on the rocket already mixed as inert. Because of this, these are generally considered a lot safer. A basic example of this is a firework. The space shuttle also had this. A big disadvantage of this compared to liquid rocket engines are that once ignition is started, you can't stop it where as in liquid rockets, you have a little more control. <img width="1947" height="1006" alt="image" src="https://github.com/user-attachments/assets/bd1a77bc-8ddf-47e1-bc73-2d64c4d71245" />

Solid boosters also have the disadvantage that they have a lot less force. <img width="1889" height="922" alt="image" src="https://github.com/user-attachments/assets/d741f0ad-fac6-4e17-a5cf-b6de855fced0" />

Given this, the advantages of solid rocket motors is that they're safer on the launch pad and can be stored for decades. 

With all of this information, some rockets like the space shuttle and SLS use a combination of solid and liquid while falcon 9 just uses liquid rockets with RP1 as the propellant. <img width="1970" height="964" alt="image" src="https://github.com/user-attachments/assets/81f954aa-cf8d-4251-906f-5fe042886849" />

## Rocket Equation

The rocket equation came from the idea that as you toss rocks off of a boat, the boat will go faster in that direction. The **Rocket Equation** builds on that idea by saying that as you burn fuel, you'll move faster because you have less mass. This commonly is referred to as **delta v** which is the change in velocity as a result. 

$$
\Delta v = v_e \ln\left(\frac{m_0}{m_f}\right)
$$

For solid rockets, the exhaust velocity is about 2 whereas for liquid rockets it's about 2.5. The initial mass is the mass with the fuel and the final mass is the mass without the fuel.

Here's an example of delta v need to reach LEO

Given:
Required Δv to reach Low Earth Orbit (LEO): 9,400 m/s (includes gravity and drag losses)
Engine exhaust velocity: ve = 3,000 m/s (typical for kerosene/LOX engines)
Payload mass: 1,000 kg
Structural mass (tanks, engines, etc.): 2,000 kg

Find: How much propellant is needed?
Solution:
Final mass after all propellant is burned:
mf = payload + structure = 1,000 + 2,000 = 3,000 kg
Rearranging the rocket equation to find initial mass:
m0 = mf × e^(Δv/ve) = 3,000 × e^(9400/3000) = 3,000 × e^3.133
m0 = 3,000 × 22.88 = 68,640 kg
Therefore, propellant mass:
mpropellant = m0 - mf = 68,640 - 3,000 = 65,640 kg

This means 96% of the rocket's mass must be propellant just to reach orbit! Only 4% can be structure and payload combined.

This extreme mass ratio is why single-stage-to-orbit (SSTO) rockets are so challenging to build, and why most rockets use multiple stages to shed dead weight during ascent.

With a multistage rocket, we can just add the delta v from each stage. <img width="1918" height="977" alt="image" src="https://github.com/user-attachments/assets/fa9ffa93-3c59-4dd2-93eb-70d689d691ca" /> In this screenshot, comparing a SSTO to a two stage equates to us gaining .5 km/s or 1000mph just by using a second stage.

Currently, these are no SSTO rockets in active use today.

## Where are rockets launched

It's faster to launch near the equator because the rotational speed of the Earth is faster. This is because then you're at the equator, you're also perpendicular to the Earth's rotational axis. <img width="1003" height="874" alt="image" src="https://github.com/user-attachments/assets/3609ddd7-fe15-4745-837f-d0971e1bef47" />

The rotation of the Earth is also west to east so we take advantage of Earth's rotation if we launch this way. 

The only caveat to the above two is that if we're going to polar orbit, we don't want this extra rotation interfering so we purposefully launch somewhere farther away from the equator which is why most polar orbit launches are done at Vandenburg rather than at Cape Canaveral. Vandenburg is also able to launch southward. 

## Other types of rockets

Chemical Rockets are the only option when launching from Earth but once a satalite is in orbit, there are there options to be able to provide thrust capability. Some satalites do still use chemical rockets. 

### Electric Proposion (Ion Rockets)

A gas onboard is ionized by electricity and are then accelerated to a high velocity so that the ions can leave the rocket as exhaust to propel the rocket. The reason ion propolsion is not used to launch from Earth is that the mass that's stripped away from ionization is incredibly small and therefore the delta v would be way too small. Those this does mean that an ion drive can last for a long time.

### Nuclear Thermal Rockets

These involve using fissible material such as Uranium to expel energy. The exhaust from this reaction could make a trip to Mars take a couple of weeks instead of 7 months which is why they're being considered. The con is that they are very dangerous.

### Solar Sails

Solar Sails have the same idea as a sailboat where they have a large sail. The momentum of photons are able to propel the satalite forward. This is a big advantage because it means that we don't need any propellant but the downside is that this is a very slow way to travel
