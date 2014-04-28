# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def rotate(s, n):
    output = []
    for ch in s:  # Loop through each character
        if ch == ' ':  # If blank, don't fuck with it.
            output.append(ch)
        else:  # otherwise, shift the letters and append.
            output.append(shift_n_letters(ch, n))
    return ''.join(output)


def shift_n_letters(letter, n):
    if (ord(letter) + n) > ord('z'):
        over = ord(letter) + n - ord('z')
        return chr(ord('a') + over - 1)
    elif (ord(letter) + n) < ord('a'):
        under = ord(letter) + n - ord('a')
        return chr(ord('z') + under + 1)
    else:
        return chr(ord(letter) + n)


print rotate('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu', 13)
#>>> 'sarah'
print rotate('dave', 5)
#>>>'ifaj'
print rotate('ifaj', -5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17)
#>>> ???
