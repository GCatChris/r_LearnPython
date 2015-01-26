from math import ceil

coin_types = [
["pennies", 2.5, 0.01, 50],
["nickels", 5.0, 0.05, 40],
["dimes", 2.268, 0.1, 50],
["quarters", 5.67, 0.25, 40]]

for coin, weight, value, roll in coin_types:
	coin_weight = float(raw_input("Enter weight of %s: " % coin))
	total_coins = ceil(coin_weight / weight)
	total_rolls = ceil(total_coins / roll)
	total_value = total_coins * value
	print "You have %d %s totaling $%.2f. You will need %d rolls." % (total_coins, 
									coin, total_value, total_rolls)
	