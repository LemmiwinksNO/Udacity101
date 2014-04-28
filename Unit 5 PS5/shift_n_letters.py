# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    if (ord(letter) + n) > ord('z'):
        print ord(letter) + n
        over = ord(letter) + n - ord('z')
        print over
        return chr(ord('a') + over - 1)
    elif (ord(letter) + n) < ord('a'):
        under = ord(letter) + n - ord('a')
        return chr(ord('z') + under + 1)
    else:
        return chr(ord(letter) + n)


print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
print shift_n_letters('a', -1)
#>>> z