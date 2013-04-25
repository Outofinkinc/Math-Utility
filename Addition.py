class Add:
    prompt = "Addition"
    
    def run(self):
        print "Enter two numbers to add."
        a = int(raw_input("Num 1 > "))
        b = int(raw_input("Num 2 > "))
        result = a + b
        print ""
        print "%r + %r = %r" % (a, b, result)
