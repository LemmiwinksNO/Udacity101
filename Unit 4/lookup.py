# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


# Check index for keyword and return a list of associated URLs if keyword is found
# otherwise return an empty list
#
# @param [list] index An index of keywords and associated URLs
# @param [string] keyword
# @return [list] urls A list of urls associated with the keyword
def lookup(index, keyword):
    # Search for keyword in index
    for entry in index:
        if entry[0] == keyword:
            return entry[1]  # list of urls
    return []   # if we don't find the keyword, return empty list


print lookup(index, 'udacity')
#>>> ['http://udacity.com','http://npr.org']
