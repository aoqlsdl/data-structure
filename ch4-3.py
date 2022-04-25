def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False #배열의 정렬 여부

    while not sorted: #배열이 정렬될 때까지 계속 실행, 각 패스스루
        #아래에서 list 값을 교환하자마자 False가 됨 -> while 절에서 다시 반복 가능. 만약 sorted = False인 상태에서 list 순서를 바꿔 True가 된다면 나머지 원소는 while절로 반복할 수 없음
        sorted = True 
        for i in range (unsorted_until_index): #인덱스 길이 만큼 반복
            if list[i] > list[i+1]:
                sorted = False #왼쪽 수가 오른쪽 수보다 큰 경우 sorted = False
                list[i], list[i+1] = list[i+1], list[i] #원소의 순서 변경
        unsorted_until_index = unsorted_until_index - 1 #정렬되지 않은 값 중에서 가장 큰 값을 가지는 원소(버블)가 정렬되었으니, 해당 원소를 제외하기 위해 -1

list = [65, 55, 45, 35, 25, 15, 10]

bubble_sort(list)
print(list)