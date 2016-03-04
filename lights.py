def lightswitches(number):
	return [False] * number

def switch(lights, init, fin):
	lights[init:fin + 1] = list(map(lambda x: not x, lights[init:fin + 1]))
	return lights

def parse(filename):
	with open(filename) as f:
		content = [list(map(int, x.strip('\n').split(" "))) for x in f.readlines()]
	return content

if __name__ == '__main__':
	content = parse('lights.txt')
	lights = lightswitches(content[0][0])
	for i in content[1:]:
		lights = switch(lights, min(i), max(i))
	print(sum(lights))
