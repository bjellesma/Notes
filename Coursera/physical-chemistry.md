## Intro to thermodynamics

### SI Units

1 Liter is equal to 1 cubic decimeter

The seven base **SI** units

| Measurement | Unit | Abbreviation |
|---|---|---|
| Distance | metre (meter) | m |
| Mass | kilogram | kg |
| Time | second | s |
| Temperature | kelvin | K |
| Current | amphere | A |
| Quantity | mole | mol |
| Luminous Intensity | candela | cd |

Many other units you hear about such as the newton (N) and the joule (J) are derived from these base units. Units are never pluralized to avoid ambiguity. Foe example, 30 min is correct while 30 mins is incorrect. Units are also always written with a space between the value and the unit and between each part of a compound unit. For instance, meter per second is written as $m{ }s^{-1}$ where as millisecond is written as $ms$

More information on how units are used can be found on https://d396qusza40orc.cloudfront.net/physicalchemistry/docs/Exercise%20on%20units.pdf

### Thermodynamic definitions

A **thermodynamic system** is defined as any part of the universe under consideration. For instance, a beaker of water can be a thermodynamic system as well as an oil refinery.

Once the thermodynamic system is defined, everything surrounding the system is known as the **thermodynamic surrounding**.

The **thermodynamic boundary** controls transfer of work, heat, and matter from the system to its thermodynamic surroundings.

![image](https://user-images.githubusercontent.com/7660667/201575626-a7bb0462-ad2c-4994-acf3-08c37acc7d71.png)

An **open system** may exchange both energy and matter with its surroundings. An example is a beaker of water

![image](https://user-images.githubusercontent.com/7660667/201575822-d2e6208e-662b-47bc-b607-7e54db1b0d70.png)

A **closed system** may exchange energy but not matter. An example is putting a lid on that beaker of water.

![image](https://user-images.githubusercontent.com/7660667/201576001-f9b1b905-b836-44fb-af89-4c7414750555.png)

An **isolated system** may exchange neither energy nor matter with its surroundings. Now we're surrounding the beaker with walls. Another example would be hot coffee is a thermos flask

![image](https://user-images.githubusercontent.com/7660667/201576221-3857b835-954e-4494-860f-c3d50e99cd5f.png)

A **diathermic system** allows heat energy flow into or out of the system.

An **adiabatic system** prevents heat energy flow into or out of the system.

![image](https://user-images.githubusercontent.com/7660667/201576474-5731f0a6-e0fa-4944-b5f1-882779fbc8d7.png)

### State change

A **state function** describes the state of a system. The following are examples of functions
* Pressure
* Volume
* Temperature
* Mass
* Quantity
* Internal Energy, U
* Enthalpy, H
* Entropy, S
* Gibbs Energy, G

**Isothermal** implies a state of constant temperature, T

**Isobaric** implied a state of constant pressure, p

**Isochric** implies a state of constant volume, V

Functions governing transition between states are called **path functions**. There are only two path functions
* Heat, q - Random molecular motion
* Work, w - uniform molecular motion

They can often be defined as the heat supplied to a system $q_{in}$ and mechanical work done on the system, $w_{on}$

![image](https://user-images.githubusercontent.com/7660667/201577673-73153507-9ac6-48e3-a89a-b74a56e29a77.png)

Path functions are **positive** when energy enters a system and **negative** when energy leaves a system.

## The zeroeth law of themodynamics

* Ironically, this was the last law to be discovered

The second law of thermodynamics isn't the focus of this lecture but is necessary to define this law. The law describes the direction in which all processes spontateously occur. For example, this is the direction of heat so a hot object always loses heat to its surrounding. This discovery lead to the definition of a new state function, **entropy**, which measures the order of an object moving to disorder on a molecular level.

The 3rd law of thermodynamics was discovered in 1912 and leads to the definition of **absolute zero** which is zero on the entropy scale and complete deteration of molecular motion. It is impossible to reach absolute zero.

These discoveries lead to the **Zeroth Law of Themodynamcis**. When two objects are separately in thermodynamic equilibrium with a third object, they are in thermodynamic equilibrium with each other. When objects come together and given enough time, they will become the same temperature. When this happens, we say that they are in thermodynamic equilibrium.

## The first law of thermodynamics and enthalpy

The first law was stated by Rdolph Clausius in 1850 and says that every system possesses and internal energy which is affected by energy being added or removed from the system and is given by the equation, $\Delta U = q_{in} + w_{on}$

The work done by an expanding gas is given by the equation, $w_{on} = Fd$ where F is the force exerted on the piston shown in the image below and d is the distance the piston moves. The pressure on the piston is given by the force exerterted divided by the cross sectional area of the piston, $p = F / A$. Through these, we find that $F = pA$, the force exerted on the piston is given by the pressure exerted multiplied by the cross sectional area. Also, $w = pAd$. We notice then that the cross sectional area multiplied by the distance through which the piston moves is the change in volume so $w=p \delta V$ which means that work done on the system is negative and given by $w_{on} = - p \Delta V$

![Word done by an expanding Gas](https://user-images.githubusercontent.com/7660667/202970299-d44cf17e-c542-4a1b-abab-6b01ad8d62ec.png)

Putting the above equations together, we come up with the **First Law of Thermodynamics** given by $\Delta U = q_{in} - p \Delta V$

There is a special case called **free expansion** where p = 0. An example is that in space, p = 0 meaning that $p \Delta V$ is also zero, therefore $\Delta U = q_{in}$ or just the heat transferred into the system. 

Another special case is **Reactions at Constant Volume** or isochoric conditions where $\Delta V = 0** and thus $\Delta U = q_v$ where heat generated occurs under constant volume or isochoric conditions. These require massive pressure changes and are usually left to the heavy chemical industry.

Another special case is **Reactions at Constant Pressure** or isobaric conditions. These reactions are most often what is performed by chemists in glassware like beakers. This is where we define a new state function called **enthalpy** given by $H = U + pV$. Thus, $\Delta H = \Delta U + \Delta (pv)$. We can simplify $\Delta (pv)$ by differentiating with the product rule to get $\Delta H = \Delta U + p \Delta V + V \Delta p$. But, under icobaric conditions, $\Delta p = 0$ canceling the second term so $\Delta H = \Delta U + p \Delta V$. Because we've defined that $\Delta U = q_{in} - p \Delta V$, we can see that $\Delta H = q_p$ where $q_p$ is heat generated under isobaric conditions.

## Reversible Expansion

The **Ideal Gas Equation** is given by $pV = nRT$ where p is pressure, V is volume, n is quantity, R is the ideal gas constant, and T is absolute temperature. We can rearrange this to be $p = \frac{nRT}{V}$. Example: Consider 1 mol of an ideal gas at 298K

p = (1 mol * 8.314 JK^{-1}mol^{-1} * 298K) / V
p = (2477.572 J) / V

Consider for volumes of 1, 3, 5, 7, 9, and 11 m^3. 

p = (2477.572 J) / 1 m^3 = 2477.572 J / m^3
p = (2477.572 J) / 3 m^3 = 825.8573 J / m^3
p = (2477.572 J) / 5 m^3 = 495.5144 J / m^3
p = (2477.572 J) / 7 m^3 = 353.9388 J / m^3
p = (2477.572 J) / 9 m^3 = 275.2857 J / m^3
p = (2477.572 J) / 11 m^3 = 225.2338 J / m^3

1 joule is equal to 1 Pascal time meters cubed therefor 1 J / m^3 = 1 Pa so the above units can also be given in terms of pascals.

These above equations give the following graph. Notice that the work is done over 2 m^3 therefor $\Delta V = 2 m^3$ so the work done is exactly double the number of pascal units. The expansion is Isothermic at 298K. You can total the work done and then negate it to get the work done over the 11 m^4 of volume.

![Isothermic Expansion](https://user-images.githubusercontent.com/7660667/202976264-4e21d69c-a060-46e8-9f52-47d09b105ab1.png)

![Isothermic Expansion](https://user-images.githubusercontent.com/7660667/202976678-ec917666-1994-4a3a-9334-a26fa0b52955.png)

Now, we'll change the 2 m^3 intervals to be .5 m^3, this gets us to a better approximation

![Isothermic Expansion](https://user-images.githubusercontent.com/7660667/202977033-8c79e184-fb1f-4b5e-bfc6-ab07577933df.png)

If we allow the intervals to become something infintesimally small, we get what's called **Reversible Isothermal Expansion**. Because this is infintesimally small, this only a theorical construct.

![Reversible Isothermal Expansion](https://user-images.githubusercontent.com/7660667/202977299-f137d1f1-761b-4c9f-967b-ded153b49bcc.png)

Because $w_{on} = - pdV$ and $p = nRT / V$, we get $w_{on} = - (nRT / V)dV$. If we now consider an expansion from $V_i$ to $V_f$, we can use an integral to get $w_{on} = - nRT \int_{V_i}^{V_f} \frac{dV}{V}$ which we can simplify to $w_{on} = - nRT \ln \frac{V_f}{V_i}$. If we go back to the example of 1 mol, we get $w_{on} = - (1 mol)(8.314JK^{-1}mol^{-1}(298K) \ln \frac{11}{1} = -5941J$ which is the value we obtained in the screenshots above.

## Heat Capacity

When an object is heated, it is expanded, the rate that this happens is dictated by the object's **heat capacity** defined as C, the heat energy rquired to raise the temperature of an object by 1K. If it heats slowly, it has a high heat capacity. If it heats quickly, it has a low heat capacity. $C=q / \Delta T$

![Heating Objects](https://user-images.githubusercontent.com/7660667/202980455-84e96c59-2f9d-4539-85ca-d99bdf75297c.png)

There are definitions built off of this which refer to the amount of heat energy required to raise the temperature of a certain volume (**Specific Heat Capacity**) or certain quantity (**molar heat capacity**) ![image](https://user-images.githubusercontent.com/7660667/202981375-e5c2e7b6-a4be-4e11-bcb9-7bd7beaafb78.png)

Metalic substances tend to have a lower heat capacity while substances like wood and rubber tend to have higher heat capacities ![Heat Capacities](https://user-images.githubusercontent.com/7660667/202981648-8d15c341-c41c-4e87-8bd4-f1810505c9df.png)

**Isochoric heat capacity** is defined as: $C_v = q_v / \Delta T = \Delta U / \Delta T$

**Isobaric heat capacity** is defined as: $C_p = q_p / \Delta T = \Delta H / \Delta T$

 $C_{p,m} = C_{V,m} + R$ Specific and molar heat capacity for an ideal gas
