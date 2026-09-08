# # Tuple are immutable
# tuple = (1,2,3)
# num = 4
# t = tuple + (num,)
# # (num,)- is a tuple with one element
# # (num)- is just an integer
# print(t)


n = (1,2,3)
a = ()
for item in n:
    a = a + (item,)
a = a + (4,)
print(a)