import Addition
import Quadratic

class Prompt:
    
    #prompt titles
    titles = [Addition.prompt, ]
    
    def opening(self):
        print "Choose an option:"
        print ""
        print "1: Addition"
        print "2: Quadratic"
        print "3: Exit"
        print ""
        choice = int(raw_input("> "))
        return choice
