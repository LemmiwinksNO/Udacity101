# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

import re


def split_string3(source, splitlist):
    pattern = "[" + splitlist + "]"
    keywords = re.split(pattern, source)  # split list based on splitlist
    while keywords.count('') != 0:  # check for '' list items and remove them
        keywords.remove('')

    return keywords


# Class version (doesn't work)
def split_string2(source, splitlist):
    output = []
    atsplit = True  # At a split point
    for ch in source:  # iterate through string by each letter
        if ch in splitlist:
            atsplit = True
        else:
            if atsplit:
                # create a new word
                output.append(ch)
                atsplit = False
            else:
                # add character to last word
                output[-1] = output[-1] + ch
        return output


# My new improved version
def split_string(content, splitlist):
    pattern = "[" + splitlist + "]"
    # Clean up the source string by removing substrings that start with
    # 'http' or '<'
    # regex -> starts with < or http, followed by any number of non-white
    # space characters, optionally followed by a blank space.
    content2 = re.sub("(<|http)\S* ?", '', content)
    keywords = re.split(pattern, content2)  # split list based on splitlist
    while keywords.count('') != 0:  # check for '' list items and remove
        keywords.remove('')

    return keywords


out = split_string("This is a test-of the,string separation-code!", " ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code", ",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
