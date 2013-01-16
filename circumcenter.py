import math

#check if slope is undefined
def checkundefin(ax, bx):
	if (ax - bx == 0):
		return 1
	else:
		return 0

#calculate slope
def slope(ax, ay, bx, by):
	return (by - ay), (bx - ax)

#combines checkundefin() and slope()
def check_calc(ax, ay, bx, by):
	if checkundefin(ax, bx) == 0:
		return slope(ax, ay, bx, by)
	else:
		return None, None


def calc(ax, ay, bx, by, cx, cy):
	slopeabn, slopeabd = check_calc(ax, ay, bx, by)
	slopebcn, slopebcd = check_calc(bx, by, cx, cy)
	slopecan, slopecad = check_calc(cx, cy, ax, ay)
	return slopeabn, slopeabd, slopebcn, slopebcd, slopecan, slopecad