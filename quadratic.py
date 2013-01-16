import math

def check_solvable(a, b, c):
	if ((b**2)-(4*a*c)) < 0:
		return 0
	else:
		return 1

def calc(a, b, c):
	x1 = (((-1*b)+(math.sqrt((b*b)-(4*a*c))))/(2*a))
	x2 = (((-1*b)-(math.sqrt((b*b)-(4*a*c))))/(2*a))
	return x1, x2