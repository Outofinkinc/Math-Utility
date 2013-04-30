import Addition
import Quadratic

#prompt titles
prompts = [Addition.prompt, Quadratic.prompt]

class Prompt:
    
    #prompt titles
    #prompts = [Addition.prompt, Quadratic.prompt]
    
    def opening(self):
        print "Choose an option:"
        print ""
        i = 0
        while i < len(prompts):
            print "%r: %s" % (i + 1, prompts[i])
            i = i + 1
        print "%r: Exit" % (i + 1)
        print ""
        choice = int(raw_input("> "))
        return choice
