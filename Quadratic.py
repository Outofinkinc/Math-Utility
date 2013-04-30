import math

prompt = 'Quadratic'

class Quad:
    
    def run(self):
        #gather a, b, c
        a = int(raw_input("A = "))
        b = int(raw_input("B = "))
        c = int(raw_input("C = "))
        print ""
        
        if (((b**2)-(4*a*c)) < 0):
            print "Not solvable"
        else:
            x1 = (((-1*b)+(math.sqrt((b*b)-(4*a*c))))/(2*a))
            x2 = (((-1*b)-(math.sqrt((b*b)-(4*a*c))))/(2*a))
            print "x = { %r ; %r }" % (x1, x2)
        
        print ""
        raw_input("Press ENTER to continue ...")
