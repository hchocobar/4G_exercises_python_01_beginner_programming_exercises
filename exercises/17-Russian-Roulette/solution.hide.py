import random

bullet_position = 3


def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position


# Don´t change the code above 
def fire_gun():
	# Your code here
	if spin_chamber() == bullet_position:
		return "You're dead!"
	else:
		return "Keep playing!"


print(fire_gun())