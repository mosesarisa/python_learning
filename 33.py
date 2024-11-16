pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
result = "pluto weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    pluto_mass, (pluto_mass / earth_mass) * 100, population,
)
print(result)
