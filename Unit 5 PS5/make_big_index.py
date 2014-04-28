

import time


def time_execution(code):
    start = time.clock()
    result = eval(code)  # evaluates string as python expression. So runs string as python.
    run_time = time.clock() - start  # time.clock() here = stop_time
    return result, float(run_time)


def make_string(p):
    s = ""
    for e in p:
        s = s + e
    return s


def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None


def addToIndex(index, keyword, url):
    # for entry in index:  # Iterate over the index looking for keyword
    #     if entry[0] != keyword:
    #         index.append([keyword, [url]])
    #         return
    #         for element in entry[1]:  # iterate over urls list
    #             if element[0] == url:  # if we find it, don't add.
    #                 return
    #         entry[1].append([url, 0])  # add url to keyword
    #         return
    # # If keyword isn't found, append it
    index.append([keyword, [[url, 0]]])


def make_big_index(size):
    index = []
    letters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
    while len(index) < size:
        word = make_string(letters)  # Turn letters list into string word.
        addToIndex(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':  # Then increase it
                #  increment letter. ord returns an integer representing the
                #  Unicode point of a character. i.e. ord('a') = 97.
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'  # Start over at 'a'
    return index


index1000000 = make_big_index(1000000)
print time_execution('lookup(index1000000, "udacity")')
print index1000000[-1]  # last
