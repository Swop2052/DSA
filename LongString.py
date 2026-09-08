# def longestUniqueSubstr(s):
#     n = len(s)
#     res = 0

#     for i in range(n):

#         # Initializing all characters as not visited
#         vis = [False] * 26

#         for j in range(i, n):

#             # If current character is visited
#             # Break the loop
#             if vis[ord(s[j]) - ord('a')] == True:
#                 break

#             # Else update the result if this window is larger,
#             # and mark current character as visited.
#             else:
#                 res = max(res, j - i + 1)
#                 vis[ord(s[j]) - ord('a')] = True
#     return res
  

# if __name__ == "__main__":
#     s = "geeksforgeeks"
#     print(longestUniqueSubstr(s))


# def count_digits(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n = n // 10
#     return count

# n = 5438
# result = count_digits(n)
# print(result)  # Output: 4


# Palindrome
# n = 1234
# num = n  
# result = 0
# while num > 0:
#     ld = num % 10
#     result = result * 10 + ld 
#     num = num // 10
# print(n == result)  


# Amstrong Number :- Number = Sum of its digits raised to power of (number of digits)
'''
ex:-  153 = 1^3 + 5^3 + 3^3
    = 1 + 125 + 27
    = 153 ✅ ARMSTRONG!

'''
n = 153
num = n  
total = 0
node = len(str(n))
while num > 0:
    ld = num % 10
    total = total + (ld ** node)
    num = num // 10
print(total == n)  