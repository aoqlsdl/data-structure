
array = [1, 10, 100, 1000, 10000]

value = int(input())
for i in array:
    if i == value:
        print(value)
    elif i > value:
        print('there is no value in the array')
        break