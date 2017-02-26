"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.



###############################################################################


def is_hometown(town_name):
    """determins if the town_name is hometown "Citi1"

    >>> is_hometown("City1")
    True
    
    >>> is_hometown(3)
    False
    
    >>> is_hometown([])
    False
    """

    home_town = "City1"
    return town_name == home_town

    # Question:
    # Python does not allow to check if parameter is there or not
    # inside the function (eg. if(!town_name): return False)
    # Is there a way to catch the error without calling it from
    # other error-catcher function?


def make_full_name(first_name, last_name):
    """Concatinate first and last names to make a full name
    
    >>> make_full_name("Cathy", "Thomas")
    'Cathy Thomas'

    # # For type edge case
    # >>> make_full_name(0, "Thomas")
    # 'Please input strings for the first & last names.'
    
    # Solution 2 assertion
    # >>> make_full_name("Tom","jones")
    # 'Tom Jones'

    # >>> make_full_name("TOM","JONES")
    # 'Tom Jones'

    """

    # # Type edge case (uses type built-in function)
    # if type(first_name) != str or type(last_name) != str:
    #     return 'Please input strings for the first & last names.'

    return first_name+' '+last_name

    ## Solution 2: if the first letter needs to be capitalized
    # return first_name[0].upper()+first_name[1:].lower()\
    # +' '+last_name[0].upper()+last_name[1:].lower()


def print_greetings(home_town, first_name, last_name):
    """ Let the user know if from same hometown & otherwise asks where"""

    full_name = make_full_name(first_name, last_name)

    if is_hometown(town_name):
        print "Hi, %s, we're from the same place!" %full_name
    else:
        print "Hi %s, where are you from?"%full_name


# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    fruits = {"strawberry", "cherry", "blackberry"}

    # # Type edge case (uses type built-in function)
    # if type(fruit) != str:
    #     return 'Please input the fruit name in string.'
    
    return fruit in fruits
    

# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    # # Type edge case (uses type built-in function)
    # if type(fruit) != str:
    #     return 'Please input the fruit name in string.'

    if is_berry(fruit):
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    # # Type edge case (uses type built-in function)
    # if type(num) != int:
    #     return 'Please input an integer.'

    return lst + [num]



# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(item_cost, state, tax_rate = .05):
    """Calculates total price by adding tax-by-state to base price

    len is a built-in func &  since there is no edge cases above
    dealing with more/less that two letter state, the error proof skipped
    for other study's sake. also, negative values of inputs and other
    edge cases are ignored for the sake of homework.
    
    Fun I love, but too much fun is of all things the most loathsome. 
    Mirth is better than fun, and happiness is better than mirth.
    - William Blake

    """
    state = state.upper()

    # calculate after tax amount
    after_tax_cost = item_cost * (1+tax_rate)

    # calculate total by adding fees
    if state == 'CA':
        total = after_tax_cost * (1.03) # 3% recycling fee
    elif state == 'PA':
        total = after_tax_cost + 2 # Highway fee
    elif state == 'MA':
        if after_tax_cost < 100: # commonwealth fund fee
            total = after_tax_cost + 1
        else:
            total = after_tax_cost + 3
    else:
        total = after_tax_cost

    return total


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
