import unittest

def FunnyPlant (people, fruit):
	i = 1
	fruittrees = [0] * fruit
	while True:
		fruittrees = list(map(lambda x: x + 1, fruittrees))
		i +=1
		if sum(fruittrees) >= people:
			return i
		else:
			fruittrees += [0] * sum(fruittrees)

print(FunnyPlant(15, 1))
print(FunnyPlant(200, 15))
print(FunnyPlant(50000, 1))
print(FunnyPlant(150000, 250))