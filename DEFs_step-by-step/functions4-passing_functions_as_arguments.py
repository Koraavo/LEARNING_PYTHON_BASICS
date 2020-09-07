# Python program to illustrate functions
# can be passed as arguments to other functions
def understanding_arguments():
    """
    def shout(text):
        return text.upper()

    def whisper(text):
        return text.lower()

    def greet(func):
        # storing the function in a variable
        greeting = func("Hi, I am created by a function passed as an argument.")
        print(greeting)

    greet(shout)
    greet(whisper)

    Let us understand this step-by-step now
    - def shout(text): gets read into the global func scope
    - def whisper(text): gets read into the global func scope
    - def greet(func): gets read into the global func scope
    - greet(shout) is first called
    - def greet(func) starts to get executed
    - greeting = func("Hi, I am created by a function passed as an argument.")
        greet(func) == greet(shout)
        shout == func
        replacing func with shout we get:
        greeting = shout("Hi, I am created by a function passed as an argument.")
        this is equivalent to def shout(text):
            so text = "Hi, I am created by a function passed as an argument."
    - def shout(text): gets executed and return = capitalised text
    - computer goes to execute the next line which is print(greeting)
    - capitalised greeting is print
    - greet(shout) is over
    - greet(whisper) is called
    - steps repeated like greet(shout)
    - small letters greeting is print


"""
    pass

help(understanding_arguments)
