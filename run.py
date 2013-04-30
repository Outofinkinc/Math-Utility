#imports
import math
import Prompt
import Quadratic
import Addition

#objects
prompt = Prompt.Prompt()
add = Addition.Add()
quad = Quadratic.Quad()

#variables
loop = 1
classlist = [add, quad]

#start
while loop == 1:
    print ""
    choice = prompt.opening()
    print ""
    
    if choice > len(classlist):
        loop = 0
    else:
        classlist[choice - 1].run()
