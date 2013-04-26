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

#start
while loop == 1:
    print ""
    choice = prompt.opening()
    
    #determine
    #if 1 (Addition)
    if choice == 1:
        print ""
        add.run()
    
    #if 2 (Quadratic)
    if choice == 2:
        print ""
        quad.run()
    
    #if 3 (Exit)
    if choice == 3:
        loop = 0
