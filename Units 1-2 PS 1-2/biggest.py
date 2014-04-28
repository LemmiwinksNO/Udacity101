# A function that takes a list of numbers and returns the biggest number

def biggest(list):
    biggest = list.pop()
    # print len(list)
    while len(list) > 0:
        new = list.pop()
        if new > biggest:
            biggest = new
    print biggest 


biggest([5,2,5,6,7,21,23456,547,4,4,2,4,67,7,3])