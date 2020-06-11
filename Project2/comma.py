
# Developer: Ignacio Aular
# ignacio345@gmail.com
# Wed Jun 3, 5:11 PM

# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your func-
# tion should be able to work with any list value passed to it.

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(L):
    # if length of L is equal to 0 return the empty list.
    if len(L) == 0:
        return L
    
    # if length of L is equal to 1 return the item at the first position.
    if len(L) == 1:
        return L[0]

    # if length of L is greater than 1 convert each item to string
    L = list(map(str, L))

    # insert the word "and" before the last item
    L.insert(-1, 'and')

    # return the list as a string in comma separated form
    return ', '.join(L)

print(comma(spam))

