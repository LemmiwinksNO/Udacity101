# Define a procedure,
#
#    hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in
# the correct bucket), with the correct
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)


# Adds a key and value to the correct bucket in the hash table.
#
# @param hash htable Hash Table
# @param string key Keyword
# @param int value Value associated with keyword
# @return hash htable Updated Hash Table
def hashtable_add(htable, key, value):
    bucket = hashtableGetBucket(htable, key)
    bucket.append([key, value])
    return htable


# Returns the bucket(element) of the hash tbale that would
# contain the keyword.
#
# @param hash htable Hash table
# @param string keyword Keyword we are searching for
# @return list htable The bucket the keyword would be in
def hashtableGetBucket(htable, keyword):
    buckets = len(htable)  # number of buckets
    hv = hashString(keyword, buckets)  # index of bucket
    return htable[hv]  # return the bucket


# Find the relevant hash value for a keyword.
# Maps a keyword to a bucket.
#
# @param string keyword
# @param int buckets Number of buckets
# @return int hv Hash value or number index of bucket
def hashString(keyword, buckets):
    hv = 0
    for ch in keyword:
        hv = (hv + ord(ch)) % buckets
    return hv


# Creates empty table with nbuckets
def makeHashTable(nbuckets):
    table = []
    for i in range(0, nbuckets):
        table.append([])
    return table


table = makeHashTable(5)
hashtable_add(table, 'Bill', 17)
hashtable_add(table, 'Coach', 4)
hashtable_add(table, 'Ellis', 11)
hashtable_add(table, 'Francis', 13)
hashtable_add(table, 'Louis', 29)
hashtable_add(table, 'Nick', 2)
hashtable_add(table, 'Rochelle', 4)
hashtable_add(table, 'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]
