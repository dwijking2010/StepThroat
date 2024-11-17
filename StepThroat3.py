import numpy as np

die_sides = int(input("Enter No of sides for dices (6/12): "))
die = ranges(1,die_sides)

num_rolls = int(input("Enter no of times you want to roll the dice: "))

results = np.random.choice(die, size = num_rolls, replace = True)
print(results)