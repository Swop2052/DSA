# Append a Number to a List Without Using append()
# add 40 to [10,20,30]

num = [10,20,30]

new_list = []

for item in num:
    new_list = new_list + [item]
new_list = new_list + [40]
print(new_list)








# num = [10,20,30]
# new_list = [0]*(len(num)+1)

# for i in range(len(num)):
#     new_list[i] = num[i]
# new_list[len(num)] = 40 
# print(new_list)