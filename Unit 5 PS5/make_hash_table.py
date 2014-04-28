# Creating an empty Hash Table
# Need to start with all the buckets


# Mine
def makeHashTable(nbuckets):
    table = []
    for i in range(0, nbuckets):
        table.append([])
    return table


def makeHashTable2(nbuckets):
    i = 0
    table = []
    while i < nbuckets:
        table.append([])
        i += 1
    return table

print makeHashTable(50)


