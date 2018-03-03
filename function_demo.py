##Functions:  At their simplest, functions provide a way of grouping together and naming a block of code that does something, supplying that code with arguments/parameters, 
##            and then doing something with those arguments/parameters.
            
def subtractor(a, b): #def- defines the function and followed by the name of the function
    """"I subtract b from a and return the result"""  #The triple quoted txt is a docstring
    print("I'm a function. My name is {}".format(subtractor.__name__))  #This line prints out the name of the function by using .format()
    print("I'm about to subtract {} and {}\n\n".format(a,b))  
    return a - b # i output a value by using the return statement
    
if __name__=='__main__':  #is how you define a routine to be executed when (and only when) a Python script is run from the command line.
    subtractor(3,2)