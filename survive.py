def bottles(n):
	return n * 16

def gallons(n):
	return n * 128

def time(oz):
	return oz/64

def survivalTime(botN, galN, ozN, peopleN):
	return time(bottles(botN) + gallons(galN) + ozN) / peopleN
