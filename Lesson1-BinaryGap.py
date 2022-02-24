def solution(N):
    # write your code in Python 3.6
    global bin_gap
    bin_gap = 0
    count = 0
    st = 0
    x = str(bin(N))[2:]
    for i in x:
        i = int(i)
        #print(i)
        if ((i == 0) & (st == 1)):
            count = count + 1
        elif(i == 1):
            if count > bin_gap:
                bin_gap = count
            count = 0
            st = 1
            #print("No")
    #print("Binary gap: " + str(bin_gap))
    return bin_gap 

# The code below is to test 
import random
num = random.randint(0, 500)
solution(num)

