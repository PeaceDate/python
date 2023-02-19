if __name__ == '__main__':
    #** boolean - True or False

    one_and_half = 1.5
    two = 2
    name = "Andrii"
    localized_name = "Андрій"

    # comparison operators - check the equality of the variables
        # == - equal
        # != - not equal
        # > - greater than
        # < - less than
        # >= - greater than or equal
        # <= - less than or equal  

    print(one_and_half == two) # False
    print(one_and_half != two) # True
    print(one_and_half > two) # False
    print(one_and_half < two) # True
    print(one_and_half >= two) # False
    print(one_and_half <= two) # True

    print(name == localized_name) # False
    print(name != localized_name) # True

    #type method - check the type of the variable

    print(type(one_and_half)) # <class 'float'>
    print(type(two)) # <class 'int'>
    print(type(name)) # <class 'str'>
    print(type(localized_name)) # <class 'str'>

    # not operator - reverse the boolean value

    print(not True) # False
    print(not False) # True

    # and operator - check if both values are True

    print(True and True) # True
    print(True and False) # False
    print(False and True) # False
    print(False and False) # False

    # or operator - check if at least one value is True

    print(True or True) # True
    print(True or False) # True
    print(False or True) # True
    print(False or False) # False
    
