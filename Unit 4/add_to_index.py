# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]


index = []


# Associate a url with a keyword in the index.
#
# @param [list] index An list where each element contains two elements -
#   1. the keyword
#   2. A list of urls associated with the keyword
# @param [string] keyword
# @param [string] url
# @return [list] index Updated list (by reference)
def addToIndex(index, keyword, url):
    # If keyword is already in the index, add the url to the list of
    # urls associated with that keyword
    for entry in index:   # Iterate over the index looking for keyword
        if entry[0] == keyword:
            entry[1].append(url)  # If we find the keyword, append the url
            return   # don't keep looking after we find the index

    # If the keyword is not in the index, add the entry to the index:
    # [keyword, [url]]
    index.append([keyword, [url]])


# TESTING
addToIndex(index, 'udacity', 'http://udacity.com')
addToIndex(index, 'computing', 'http://acm.org')
addToIndex(index, 'udacity', 'http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],
#>>> ['computing', ['http://acm.org']]]
