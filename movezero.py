# Move all Zero at the end 
num = [0,1,0,3,12]

def move(num):
    insert_pos = 0
    for i in range(len(num)):
        if num[i] !=0:
            if i != insert_pos:
                num[insert_pos] = num[i]
                num[i] = 0
            insert_pos += 1

   