# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 


def tax_calculation(tax, state, cost):

    """
    Function calculates full cost of an item based on tax bracket.

    Function asks user for cost of item and state in which transaction is processed.
    It passes the tax, state, and cost as parameters. It evaluates tax based on if user is in CA or not.

    """

    state = raw_input('Are you making a transaction in California? Please enter, "yes" or "no".') #user input for state of CA y/n
    cost = float(raw_input('What is the cost of your item(s) in USD? Please enter in format, "29.99".')) #user input for cost of item(s)
    
    if state == "yes": #if state is noted as California
        tax = float(.07 * cost) #then tax is defined as 7%, bound to variable tax
        return cost + tax #evaluates total cost of item by adding cost & tax

    elif state == "no": #if state is not California
        tax = float(.05 * cost) #then tax is defined as 5%, bound to variable tax
        return cost + tax #evaluates total cost of item by adding cost & tax

    else: #else if any input were not recognized, not sure if this will work since cost is a float
        return "Your answers weren't understood. Please try again." #denotes to user that 1 or more entries were not in correct format
        tax_calculation() #runs function again


#####################################################################


# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def is_berry(fruit_name):

    """
    Function evaluates if a given fruit is a berry based on a list of berries.

    Function asks user for fruit name, then evaluates is entered value exists in berries.

    """

    fruit_name = str(raw_input("What is the fruit name?")) #user input for fruit_name which will be checked against berries list
    berries = ("strawberry", "cherry", "blackberry") #list of possible berries
    print "Is this fruit a berry?" #message leading into answer of t/f for berry

    if fruit_name is str in berries: #if the fruit_name user has input is a string within the berries list
        return True #evaluate that the item is a berry
    else: #otherwise the fruit_name is not in berries
        return False #evaluate that the item is not a berry


def shipping_cost(fruit_name):

    """
    Function calculates shipping cost based on if a fruit is a berry or not.
    """

    is_berry(fruit_name) #calls is_berry() and passes fruit_name as an argument

    if is_berry() == True: #if the fruit_name is in the berries list
        return 0 #fruit will either not be shipped or shipped free
    elif is_berry() == False: #if the fruit_name is not in the berries list
        return 5 #fruit will be shipped with a cost of 5
    else:
        return "Error"


###


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.


def is_hometown():

    """
    Function takes a town name as user input and compares it to my hometown, San Rafael.

    If we share the same hometown, function evaluates to true. Otherwise, it evaluates to false.
    """

    town_name = raw_input("Where is your hometown?") #raw_input for user's entry of hometown
    my_hometown = "San Rafael" #my_hometown is bound to my hometown of San Rafael, a string

    if town_name == my_hometown: #if user's hometown is the same as mine
        return True #evaluate is_hometown to true
    else: #otherwise
        return False #evaluate is_hometown to false


def full_name():

    """
    Asks user for first and last name and stores it for later use.
    """

    first_name = raw_input("What is your first name?") #raw_input for user's entry of their first name
    last_name = raw_input("What is your last name?") #raw_input for user's entry of their last name
    name = str(first_name + last_name) #result of the concatenation of first and last name is bound to a new variable, name
    return name #return full name, or name


def hometown_greeting(town_name, first_name, last_name):

    """
    Function uses is_hometown and full_name output to construct a greeting from me.
    """

    if is_hometown() == True: #if is_hometown evaluates to true
        name = full_name() #name variable is bound to the result of full_name()
        print "Hi,{}, we're from the same place!".format(name) #print this sentence, using the name variable
    else: #if is_homewtown is not true
        name = full_name() #name variable is bound to the result of full_name()
        print "Hi, {}, where are you from?".format(name) #print this sentence, using the name variable


#####################################################################


# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.


def increment(x=1):

    """
    Function takes a value for x and stores it.
    """

    x = int(x) #defines x as an integer
    # x = int(raw_input()) => this is what I previously had here

    def add(x, y):

        """
        Function takes x and a value for y and adds them together.
        """

        y = int(y) #defines y as an integer
        # y = int(raw_input()) => this is what I previously had here
        return x + y #adds x & y

addfive = increment(5) #call increment() and bind result to new variable, addfive
y = 5 #see below, not sure how to call add()
print int(addfive) + y #see below, not sure how to call add()
y = 20 #see below, not sure how to call add()
print int(addfive) + y #see below, not sure how to call add()


# add(addfive, 5) 
#could not figure out how to call add() using the variable addfive as x and 5 as y
#add(addfive, 20) 
#could not figure out how to call add() using the variable addfive as x and 20 as y
 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def numbers(number, number_list):

    """
    Function takes a number and a list of numbers as arguments and returns a new list with the number appended to it.

    """

    number = int(number) #defines number as an integer
    number_list = number_list.append(number) #defines number_list as itself with number added to it
    return number_list #returns new list with appended number


#####################################################################