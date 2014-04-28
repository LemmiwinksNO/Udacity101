# Define a procedure,

# hashtable_lookup(htable,key)

# that takes two inputs, a hashtable
# and a key (string),
# and returns the value associated
# with that key.


# Find the value associated with a keyword.
#
# @param hash htable Hash table
# @param string key Keyword
# @return int value The value associated with the keyword.
def hashtableLookup(htable, key):
    bucket = hashtableGetBucket(htable, key)
    for entry in bucket:     # search in the relevant bucket
        if entry[0] == key:  # e[0] is the keyword
            return entry[1]  # e[1] is the value associated with the keyword
    return None


# Adds a key and value to the correct bucket in the hash table.
#
# @param hash htable Hash Table
# @param string key Keyword
# @param int value Value associated with keyword
# @return hash htable Updated Hash Table
def hashtableAdd(htable, key, value):
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


table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
        [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

print hashtableLookup(table, 'Francis')
#>>> 13

print hashtableLookup(table, 'Louis')
#>>> 29

print hashtableLookup(table, 'Zoe')
#>>> 14
