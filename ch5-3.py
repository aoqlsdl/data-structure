numlist = [3, 5, 2, 1, 9]
a = len(numlist) - 1
set = False
minimum = 0

while (set==True):
    for i in numlist:
        if (numlist[i] < numlist[i+1]):
            # set==False
            continue
        elif (numlist[i] > numlist[i+1]):
            minimum = numlist[i+1]
            
            set==False

print(numlist)

# 모르겠음...