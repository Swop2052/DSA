# Reverse string using for loop
# text = 'Hello'
# rev = ""
# for char in text:
#     rev = char + rev
# print(rev)

# Reverse using index and Range
text = 'Hello'
rev = ""
for i in range(len(text)-1,-1,-1):
    # range(start, stop, step)
    # 4,3,2,1,0 = 0-1= 0,1-1=1,2-1=1,3-1=2,4-1=3
    rev = rev +text[i]
print(rev)