max_multiple =2520
dividers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
dividers1 = []
t = True
while t:
    for i in range (2,21):
        if max_multiple % i == 0:
            dividers1.append(i)
            

        else:
            i -= 1
            max_multiple += 2520


    if dividers1 == dividers:
        t = False


print (max_multiple)