# Check whether a string is palindrome.
# input = madam
# output = True
# A palindrome is a word, phrase, number, or sequence of symbols that reads the exact same forwards and backwards

# def palin(s):
#     return s == s[::-1]

# print(palin("Swop"))



##################################################################

#  Move all zeroes to end.
# i/p = [0,1,0,3,12]
# o/p = [1,3,12,0,0]
# Logic Using two Pointer

def move(num):
    pos = 0

    for i in range(len(num)):
        if num[i] != 0:
            num[pos],num[i] = num[i],num[pos]
            pos += 1

    return num
print(move([0,1,0,3,12]))