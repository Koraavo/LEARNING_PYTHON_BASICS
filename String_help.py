def understanding_strings():
    """
    Strings can be written either with single/double or triple quotes
    All string methods returns new values. They do not change the original string.
    
    my_string = "Hello, welcome to
               the world of Python"
    print(my_string)

    str = 'Hello World'
        print('str = ', str)
    # Indexing starts at 0

    # slicing 2nd to 5th character: "ello"
        print('str[1:5] = ', str[1:5])

    # slicing 6th to 2nd last character: "Worl
        print('str[5:-2] = ', str[5:-2])

    # Concatenation
    str1 = 'Hello'
    str2 = 'World!'

    # using +
        print('str1 + str2 = ', str1 + str2)

    # using *
        print('str1 * 3 =', str1 * 3)

    # BUILT-IN METHODS
    text = "python is AWesome."

    Method	Description
    All methods work with the following syntax:
    text.method()

    zfill()	            Fills the string with a specified number of 0 values at the beginning

    len()               Returns the total length of the string starting from 1
    syntax: len(text)

    count(word, word_to_search)	    Returns the number of times a specified value occurs in a string
    one argument is necessary

    center()	        Returns a centered string
    Example:
        text.center(30) # takes one positional argument
    ljust()	            Returns a left justified version of the string
    rjust()	            Returns a right justified version of the string


    split(separator)	            Splits the string at the specified separator, and returns a list
    rsplit()	        Splits the string at the specified separator, and returns a list
    splitlines()	    Splits the string at line breaks and returns a list

    strip()	            Returns a trimmed version of the string
    rstrip()	        Returns a right trim version of the string
    lstrip()	        Returns a left trim version of the string


    # no positional arguments necessary
    title()	            Converts the first character of each word to upper case
    istitle()	        Returns True if the string follows the rules of a title
    capitalize()	    Converts the first character to upper case
    swapcase()	        Swaps cases, lower case becomes upper case and vice versa
    upper()	            Converts a string into upper case
    isupper()	        Returns True if all characters in the string are upper case
    lower()	            Converts a string into lower case
    casefold()	        Converts string into lower case # more aggressive than lower()
    islower()	        Returns True if all characters in the string are lower case


    startswith()	    Returns true if the string starts with the specified value
    endswith()	        Returns true if the string ends with the specified value
    both take one positional argument
    syntax: text.endswith('d') for Hello World = True else false

    index()	            Searches the string for a specified value and returns the position of where it was found
    text.index('e') # one argument to search for the letter
    rindex()	        Searches the string for a specified value and returns the last position of where it was found

    enumerate()
    Example:
        L = ['apples', 'bananas', 'oranges']
        for idx, val in enumerate(L, start=1(optional argument):
            print(f"index is {idx} and value is {val}")
    Example2:
        list(enumerate(['a', 'b', 'c']))
        for idx, val in enumerate(['a', 'b']):
            print(idx, val)

    isidentifier()	    Returns True if the string is an identifier
    isalnum()	        Returns True if all characters in the string are alphanumeric
    isalpha()	        Returns True if all characters in the string are in the alphabet
    isdecimal()	        Returns True if all characters in the string are decimals
    isdigit()	        Returns True if all characters in the string are digits
    isnumeric()	        Returns True if all characters in the string are numeric
    isspace()	        Returns True if all characters in the string are whitespaces
    isinstance(word, identifier(str, int, float, etc)) Returns true for the word

    isprintable()	    Returns True if all characters in the string are printable
    This function is used to check if the argument contains any printable characters such as :
    Digits ( 0123456789 )
    Uppercase letters ( ABCDEFGHIJKLMNOPQRSTUVWXYZ )
    Lowercase letters ( abcdefghijklmnopqrstuvwxyz )
    Punctuation characters ( !”#$%&'()*+, -./:;?@[\]^_`{ | }~ )
    and Space ( )


    text.find()	        Searches the string for a specified value and returns the position of where it was found
    Example:
        print(text.find('o')) for "Hello World" returns 4 (first index position for the letter
    rfind()	            Searches the string for a specified value and returns the last position of where it was found

    format()	        Formats specified values in a string
    Example:
        a = 'Hello'
        b = 'World'
        print("{}, {}".format(a, b))

    format_map()	    Formats specified values in a string
    Example:
        point = {'x':4,'y':-5}
        print('{x} {y}'.format_map(point))

        point = {'x':4,'y':-5, 'z': 0}
        print('{x} {y} {z}'.format_map(point)) returns the respective values as output


    join()	            Joins the elements of an iterable to the end of the string
    Example:
        list1 = ['1','2','3','4']
        s = "-"

        # joins elements of list1 by '-'
        # and stores in sting s
        s = s.join(list1)
        Returns 1-2-3-4

        list1 = ['g','e','e','k', 's']
        print("".join(list1)) # prints geeks

    # It always returns a three tuple string
    partition()	        Returns a tuple where the string is parted into three parts
    rpartition()	    Returns a tuple where the string is parted into three parts
    Example:
        txt = "I could eat bananas all day"
        x = txt.partition("mangoes")
        ('I could eat bananas all day', '', '')
        y = txt.rpartition("mangoes")
        ('', '', 'I could eat bananas all day')

    replace()	        Returns a string where a specified value is replaced with a specified value
        syntax: text.replace(old, new)



    maketrans()	        Returns a translation table to be used in translations
    translate()	        Returns a translated string
    Example:
        # Python3 code to demostrate
        # translations using
        # maketrans() and translate()


        # target string
        trg = "weeksyourweeks"

        # specify to translate chars
        str1 = "wy"

        # specify to replace with
        str2 = "gf"

        # delete chars
        str3 = "u"


        # using maketrans() to
        # construct translate
        # table
        table = trg.maketrans(str1, str2, str3)

        # Printing original string
        print("The string before translating is : ", end="")
        print(trg)

        # using translate() to make translations.
        print("The string after translating is : ", end="")
        print(trg.translate(table))

    encode()	        Returns an encoded version of the string
    takes one or two arguments
    Example:
        # unicode string
        string = 'pythön!'
        print('The string is:', string)

        # ignore error
        print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))

        # replace error
        print('The encoded version (with replace) is:', string.encode("ascii", "replace"))


    expandtabs()	    Sets the tab size of the string
    syntax: text.expandtabs()
    Example:
        str = 'xyz\t12345\tabc'
        # if no argument is passed, default tabsize is 8
        result = str.expandtabs(15) # xyz            12345          abc


    """
    pass

understanding_strings()
help(understanding_strings)