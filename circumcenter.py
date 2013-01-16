import math

def checkundefin(ax, bx):
	if (ax - bx == 0):
		return 1
	else:
		return 0

def slope(ax, ay, bx, by):
	return ((by - ay)/ float(bx - ax))

def check_calc(ax, ay, bx, by):
	if checkundefin(ax, bx) == 0:
		t_slope = slope(ax, ay, bx, by)
	else:
		t_slope = None
	return t_slope

def calc(ax, ay, bx, by, cx, cy):
	slopeab = check_calc(ax, ay, bx, by)
	slopebc = check_calc(bx, by, cx, cy)
	slopeca = check_calc(cx, cy, ax, ay)
	return slopeab, slopebc, slopeca