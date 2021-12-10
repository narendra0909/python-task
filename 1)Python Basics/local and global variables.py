def greet():
    name = 'Narendra'      #Here name is Local variable for the greet function and is not accesible outside of it
    print('Hello ', name)

greet()

# Global variablle


# Any variable present outside any function block is called a global variable. Its value is accessible from inside any function. In the following example, the name variable is initialized before the function definition. Hence, it is a global variable.

name='World'  #Now, you can access the global variable name because it has been defined out of a function.
def greeting():
    print ("Hello ", name)
greeting()