def understanding_dictionary():
    """
    # The TREE IS SO:
    # DICTIONARY
    # ARRAYS
    # LISTS
    # STRINGS/ INTEGERS

    # ARRAYS
    # all arrays start with the square bracket.

    Sentence = ["My", "Name", "is", "Kinjal"]  # This is an array
    print(Sentence)
    print(Sentence[3])  # Kinjal is the third item in the array under variable Sentence
    # all arrays are indexed starting from 0 and towards the end from -1

    -----------------------------------------------------------------------------

    # DICTIONARY
    # All dictionaries start with a curly bracket

    Dictionary = {1: "Kinjal", "Age": "32", "interests": "learning", "courses": ["Python", "Languages"]}
    Dictionary1 = {"Name": "Kinjal", "Age": "32", "interests": "learning"}["interests"]
    #Name is a key
    #when you call the key, the binding related to the key is displayed

    print(Dictionary)
    print(Dictionary[1])
    print(Dictionary["courses"])
    print(Dictionary1)

    -----------------------------------------------------------------------------------

    checking if a key exists in the dictionary:
        using get method
        print(Dictionary.get('phone', 'Not Found'))
        result is None if no second argument is passed since phone does not exist in the dictionary
        result here is Not Found since that is the result we want to print: second argument

    add a Key in the Dictionary
        Dictionary['phone'] = '555-555-555'

    replace/update values:
        Dictionary[1] = 'Jane'
        print(Dictionary)

    also using update:
        Dictionary.update({1: "Kinjal", "Age": "35", 'phone': '555-555-555'})

    del Dictionary["phone"]
        print(Dictionary)
        popped = Dictionary.pop("Age")
        print(popped)

    see all the keys in the dictionary:
        print(Dictionary.keys())

    see all the values:
        print(Dictionary.values())

    see keys and values:
        print(Dictionary.items())

    to view keys and values and print them from the dictionary:
    for key, value in Dictionary.items():
        print(key, value)

    """
    pass
Dictionary = {1: "Kinjal", "Age": "32", "interests": "learning", "courses": ["Python", "Languages"]}
Dictionary1 = {"Name": "Kinjal", "Age": "32", "interests": "learning"}["interests"]

#Name is a key
#when you call the key, the binding related to the key is displayed

print(Dictionary)
print(Dictionary[1])
print(Dictionary["courses"])
print(Dictionary1)
print(Dictionary.get('phone', 'Not Found'))
Dictionary['phone'] = '555-555-555'
print(Dictionary.get('phone'))
Dictionary[1] = 'Jane'
print(Dictionary)
Dictionary.update({1: "Kinjal", "Age": "35", 'phone': '555-555-555'})
print(Dictionary)
del Dictionary["phone"]
print(Dictionary)
popped = Dictionary.pop("Age")
print(popped)
print(Dictionary.keys())
print(Dictionary.values())
print(Dictionary.items())

for key, value in Dictionary.items():
    print(key, value)

help(understanding_dictionary)
