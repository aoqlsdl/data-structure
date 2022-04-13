array = [1,2,3,4,5,6,7,8,9]
value = int(input())

lower_bound = array[0]
upper_bound = len(array) - 1

while True:
    midpoint = (lower_bound + upper_bound) / 2
    print(midpoint)

    if value > midpoint:
        lower_bound = midpoint + 1
        continue
    elif value < midpoint:
        upper_bound = midpoint - 1
        continue
    else:
        print(midpoint)
