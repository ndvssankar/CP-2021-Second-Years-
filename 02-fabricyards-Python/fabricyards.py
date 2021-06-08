# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricExcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards)
# . Hint: you may want to use fabricYards, which you just wrote!


def fun_fabricyards(inches):
	number_of_fabric_yards = inches // 36
	inches = inches % 36
	if inches == 0:
		return number_of_fabric_yards
	else:
		return number_of_fabric_yards + 1

def fun_fabricexcess(inches):
	number_of_fabric_yards = fun_fabricyards(inches)
	return number_of_fabric_yards * 36 - inches

