import quadratic
import circumcenter

loop = 1

while loop == 1:
	print ""
	print "1. Calculate Quadratic"
	print "2. Circumcenter"
	print "3. Exit"
	print ""
	choice = int(raw_input("> "))
	print ""
	
	#quadratic
	if choice == 1:
		#gather A, B, C
		quadA = int(raw_input("A = "))
		quadB = int(raw_input("B = "))
		quadC = int(raw_input("C = "))
		print ""
		
		#check if solvable and solve if solvable
		if quadratic.check_solvable(quadA, quadB, quadC) == 0:
			print "Not Solvable"
			loop = 1
		else:
			print "x =", quadratic.calc(quadA, quadB, quadC)
			loop = 1
	
	#circumcenter
	if choice == 2:
		#gather ax, ay, bx, by, cx, cy
		ax = int(raw_input("Ax = "))
		ay = int(raw_input("Ay = "))
		bx = int(raw_input("Bx = "))
		by = int(raw_input("By = "))
		cx = int(raw_input("Cx = "))
		cy = int(raw_input("Cy = "))
		print ""
		
		#calculate, getting the numerators and denominators of each slope.
		slopeabn, slopeabd, slopebcn, slopebcd, slopecan, slopecad = circumcenter.calc(ax, ay, bx, by, cx, cy)
		
		#print slope, for developement purposes
		#if slope is undefined, print "N/A"
		if slopeabd is None:
			print "m(AB) = N/A"
		#if not, print value as fraction and decimal
		else:
			print "m(AB) = %r/%r (%r)" % (slopeabn, slopeabd, (slopeabn / float(slopeabd)))
		if slopebcd is None:
			print "m(BC) = N/A"
		else:
			print "m(BC) = %r/%r (%r)" % (slopebcn, slopebcd, (slopebcn / float(slopebcd)))
		if slopecad is None:
			print "m(AC) = N/A"
		else:
			print "m(AC) = %r/%r (%r)" % (slopecan, slopecad, (slopecan / float(slopecad)))
	
	#exit
	if choice == 3:
		loop = 0