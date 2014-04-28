# Define a procedure,

# hashtable_update(htable,key,value)

# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

# Hint: Use hashtable_lookup as a starting point.
# Make sure that you return the new htable


def findBucket(bucket, key):
    for entry in bucket:
        if entry[0] == key:
            return entry
    return None


# Update value associated with a key. If key is already in table, update the value.
# Otherwise, add a new entry for the key and value.
#
# @param hash htable Hash Table
# @param string key Keyword
# @param int value Value associated with keyword
def hashtableUpdate(htable, key, value):
    bucket = hashtableGetBucket(htable, key)
    entry = findBucket(bucket, key)
    if entry:
        entry[1] = value
    else:
        bucket.append([key, value])  # more efficient to add this way than hashtableAdd


# Find the value associated with a keyword.
#
# @param hash htable Hash table
# @param string key Keyword
# @return int value The value associated with the keyword.
def hashtableLookup(htable, key):
    bucket = hashtableGetBucket(htable, key)
    entry = findBucket(bucket, key)
    if entry:
        return entry[1]
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

hashtableUpdate(table, 'Bill', 42)
hashtableUpdate(table, 'Rochelle', 94)
hashtableUpdate(table, 'Zed', 68)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42],
#>>> ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2],
#>>> ['Rochelle', 94]]]
