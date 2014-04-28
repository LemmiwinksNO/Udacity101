# Building Web Index
# I think we take a web page, break it up into words with .split(), and add those
# words as keywords to our index.
# Algorithm:
# 1. Clean up content - remove all punctuation
# 2. call split on content to turn the big string into a list of words.
# 3. Loop through each keyword in list
#   a. call addToIndex

import re
import string

# 1 Clean up content - removing punctuation
# Really what we want is to remove prior and trailing punctuation. Could make a better
# regular expression to do this.
#
# OPTIONS
#   1. use regular expressions
#   2. use translate
#   3. use strip(char) where char is anything you want removed.
quote = "In Washington, it's dog eat dog. In academia, it's exactly the opposite."
quote2 = """
    There's no business like show business,
    but there are several businesses like accounting.
        (David Letterman)
        """

# regex .sub -> (pattern, replace, string) -> search for pattern in string and replace
# with what is found with replace.
# print re.sub('[%s]' % re.escape(string.punctuation), '', quote2)

# translate - Delete all characters in string that are in string.punctuation.
# This is fast but not really the purpose of translate, we just have an empty table here.
# print quote.translate(None, string.punctuation)


# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.


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


# Add the content of a web page to our index
#
# @param [list] index An index of keywords and associated URLs
# @param [string] url
# @param [string] content Web page content as a string
def addPageToIndex(index, url, content):
    # Clean up the content by removing prior and trailing punctuation

    # turn content into a list of words
    keywords = content.split()

    # for each keyword, call addToIndex
    for keyword in keywords:
        addToIndex(index, keyword, url)


addPageToIndex(index, 'fake.text', "This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]
