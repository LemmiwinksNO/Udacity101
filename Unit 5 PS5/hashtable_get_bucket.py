# Define a procedure, hashtableGetBucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.


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


table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
        ['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtableGetBucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

print hashtableGetBucket(table, "Brick")
#>>> []

print hashtableGetBucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]
