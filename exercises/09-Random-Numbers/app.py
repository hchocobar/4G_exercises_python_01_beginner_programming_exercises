import random


def get_randomInt():
  	# Change only this line below
	# random_number = random.random()
	random_number = random.randint(1, 10)
	return random_number


print(get_randomInt())
