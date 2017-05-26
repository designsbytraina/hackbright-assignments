"""List Assessment 

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    return [odds for odds in numbers if odds % 2 > 0] #used list comprehension to return items in numbers where the remainder of an integer divided by 2 is anything but zero


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """

    for i, item in enumerate(items): #attempted to do this with length and range method, but read through notes and saw further study on enumerate method. still could not make this work with list comprehension, though.
        print i, item


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """
    
    for foods in foods1, foods2:
        foods1 = set(foods1) #rebound foods1 (list) to a set with the same elements
        foods2 = set(foods2) #rebound foods2 (list) to a set with the same elements
        foods = list(foods1 & foods2) #took the intersection of sets food1 & food2 and bound to new variable foods
        print foods #printed new variable foods, which should be the intersection of foods1 & foods2 alpha-sorted
        #ISSUE: console is printing two intersection sets, is it due to two arguments being passed into function?

    #for foods in foods1, foods2: ------ UNSUCCESSFUL -------
        #foods1 = set(foods1)
        #foods2 = set(foods2)
        #foods = foods1 & foods2
        #list(foods)
        #print foods


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """
    
    return items[::2] #indexes all items in items and returns every other number by stepping 2


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """


    for item in items: #begins loop
        n = items[-1] #assumes n is the last number of the list, binds to variable n
        given_list = items[:-1] #assumes list is a slice of all numbers before n, binds to new variable given_list

        for item in given_list: #begins loop evaluating new list slice, given_list
            #item = given_list[n] #item is bound to index n of given_list
            if item is None or n > item:
                return n #this should return empty list, but is returning 5
            elif item > n:
                return item #this is working, but not returning the count separately or in brackets
            elif item == n:
                return item, n #if item is equal to n, return both values separated by a comma
            else:
                return "ValueError"

    ### ISSUE: Not able to get more than one number to appear, I would like to talk through this during advising.
        # Left some commented out code below:

        ###

          #  if item is None or n > item:
           #     item = given_list[n]
            #return n, "This is if statement" #this should return empty list, but is returning 5
         #   elif item > n:
          #      return item, "This is elif #1" #this is working, but not returning the count separately or in brackets
           # elif item == n:
            #    return item, n, "This is final statement" #if item is equal to n, return both values separated by a comma
         #   else:
         #       return "ValueError"

        ###

        #item = items[:] #binds given_item variable to index of all items
        #if item is None or n > item : #if given_item is None or less than n
         #   item = n # then given_item is rebound to n
        #return item #returns given_item

        ###

        #given_item = items[::1] #binds given_item variable to index 1 of items
        #for given_item in items: # begins loop for n/item in a list of items
          #  if given_item > n: # if n is greater than the previous value for given_item
           #     given_item = n # binds n to given_item variable
            #    return given_item

        ###

        #given_item = None
        #for n in items:
         #   if given_item is None or n > given_item :
          #      given_item = n
           # return given_item

        ###

        #for n in items:
         #   return items[::1]
            #if item > n:
             #   return n


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
