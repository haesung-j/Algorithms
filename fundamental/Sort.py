'''
[정렬]
- 데이터를 특정한 기준에 따라 순서대로 나열
- 일반적으로 문제 상황에 따라 적절한 정렬 알고리즘 사용
'''
## === 선택 정렬 [ O(N^2) ] == ##
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 "선택"해 맨 앞 데이터와 교환
# [시간 복잡도] - O(N^2)
# N번만큼 매번 가장 작은 수를 찾아서 맨 앞으로 보내야 함
# 즉, N + (N-1) + ... + 2

def selection_sort(array):
    for i in range(len(array)):
        # 가장 앞 데이터 기준
        min_idx = i
        for j in range(i+1, len(array)): # 뒤 데이터 탐색
            if array[min_idx] > array[j]: # 더 작은 데이터가 있다면
                min_idx = j        
        array[i], array[min_idx] = array[min_idx], array[i] # 교환
    return array

array = [3,2,6,5,0,4,7,9,1,8]
print(selection_sort(array))


## === 삽입 정렬 [ O(N) ~ O(N^2) ] == ##
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 "삽입"
# [시간 복잡도] - O(N) ~ O(N^2)
# 만약 이미 정렬되어 있는 배열이라면 N번 수행
# 최악의 경우, N + (N-1) + ... + 2 + 1

def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):   # 인덱스 i부터 1까지 1씩 감소
            if array[j] < array[j-1]: # 왼쪽과 비교
                array[j], array[j-1] = array[j-1], array[j]
            else:  # 왼쪽이 더 크다면 삽입을 멈춤
                break
    return array

array = [3,2,6,5,0,4,7,9,1,8]
print(insert_sort(array))


## === 퀵 정렬 [ O(NlogN) ~ O(N^2)] == ##
# 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터 위치 교환
# [시간 복잡도] - O(NlogN) ~ O(N^2)
# 평균적으로 O(NlogN)의 시간복잡도를 가짐

def quick_sort(array, start, end):
    # 종료 조건: 원소가 1개인 경우
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while (left <= right): # 교차할 때까지
        # pivot보다 큰 데이터를 찾을 때까지 left 증가
        while (left <= end) and (array[left] <= array[pivot]):
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 right 감소
        while (right > start) and (array[right] >= array[pivot]):
            right -= 1
        # 엇갈린다면, pivot과 작은 데이터 교환
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 엇갈리지 않았다면, 작은 데이터와 큰 데이터 교환
        else: 
            array[left], array[right] = array[right], array[left]
            
    # pivot 기준으로 분할된 좌측과 우측 배열에 대해 반복 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


array = [3,2,6,5,0,4,7,9,1,8]
quick_sort(array, 0, len(array)-1)
print(array)

## 파이썬 문법 활용한 퀵 정렬
def quick_sort2(array):
    if len(array) <= 1:  # 원소가 1개인 경우 종료
        return array
    
    pivot = array[0]
    rest = array[1:]
    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]
    return quick_sort2(left) + [pivot] + quick_sort2(right)

array = [3,2,6,5,0,4,7,9,1,8]
print(quick_sort2(array))


## === 계수 정렬 [ O(N+K) ] == ##
# 특정 조건이 부합할 때만 사용할 수 있지만 "매우 빠른" 정렬 알고리즘
# 특정 조건: 데이터 크기 범위가 제한되어 정수 형태로 표현 가능할 때
# [시간 복잡도] - O(N+K)
# 데이터 개수 N, 데이터 최댓값 K일 때 최악의 경우에도 보장
# 단, 데이터의 범위가 클 경우 

# 모든 원소의 값이 0이상, 9이하로 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')