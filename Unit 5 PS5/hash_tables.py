# Hash tables

import urllib
import time


def time_execution(code):
    start = time.clock()
    result = eval(code)  # evaluates string as python expression. So runs string as python.
    run_time = time.clock() - start  # time.clock() here = stop_time
    return result, float(run_time)


# Take a url and return the corresponding web page data.
#
# @param [string] url The URL of a web-page
# @return [string] page The web-page as a string
def getPage(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ""


# This is an example of a bad hash function.
# It won't distribute evenly between buckets.
# If the number of buckets is large, some buckets will be empty.
# It produces an error for the following keyword - ''
def badHashString(keyword, buckets):
    return ord(keyword[0]) % buckets


# Better hash function
# Based on ord of each character, rather than just the first one.
def hashString2(keyword, buckets):
    num = 0
    for ch in keyword:
        num += ord(ch)
    hv = num % buckets
    return hv


# Slightly better hash function
# Does the modulo on each character rather than at the end. Helps if the keyword is very large.
# Could still be a LOT better, this is very slow b/c we loop through each character.
# What if we looped through a max of 3 characters? -> I tried. The bucket range gets WAY larger.
def hashString(keyword, buckets):
    hv = 0
    for ch in keyword:
        hv = (hv + ord(ch)) % buckets
    return hv


def testHashFunction(func, keys, size):
    results = [0] * size  # Start each bucket at 0
    keys_used = []  # List of keys used
    for w in keys:
        if w not in keys_used:  # Don't want to add a word more than once(like crawler)
            hv = func(w, size)  # figure out where the key would hash to (which bucket) - hash value
            results[hv] += 1    # +1 to that bucket
            keys_used.append(w)
    return results


# Get a huge list of words (this is an entire book)
words = getPage('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
# print testHashFunction(badHashString, words, 12)
#=> [730, 1541, 1055, 1752, 1784, 839, 1452, 2074, 1409, 754, 924, 899]
# print testHashFunction(hashString, words, 12)
#=> [1368, 1268, 1273, 1279, 1284, 1245, 1207, 1228, 1281, 1232, 1233, 1315]
ht = testHashFunction(hashString, words, 100)
# print ht
# print min(ht)  # 1000 buckets -> 1; 100 buckets -> 105
# print max(ht)  # 1000 buckets -> 40; 100 buckets -> 192

print time_execution('testHashFunction(hashString, words, 100)')[1]
