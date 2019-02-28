# Counting Sort
def count_sort(List):
    # 각 숫자를 셀 리스트 생성 ( 최댓값을 찾아서 그만큼 배열 공간 생성)
    MAX_VALUE = max(List)
    counts = [0]*(MAX_VALUE+1)
    tmp = [0]*(len(List))

    # 각 항목들 발생 횟수 세기
    for i in range(len(List)):
        counts[List[i]] += 1
    
    # 각 항목들 위치 설정을 위한 누적합 구하기
    for i in range(1,MAX_VALUE+1):
        counts[i] = counts[i] + counts[i-1] 
    
    # 카운트를 사용하여 각 항목 위치 설정
    for i in range(len(List)-1,-1,-1):
        counts[List[i]] -= 1
        tmp[counts[List[i]]] = List[i]
    
    print(tmp)

# time complexity : O(n+k)
#
# 단점 : 최댓값이 엄청 크면, 메모리를 많이 잡아 먹는다.
#        숫자 크기에 따라 시간복잡도가 매우 차이난다.
#
# 사용 용도 : 특정한 범위 안에 있을 때 효과적
#            ex) 알파벳 Suffix array를 얻는 경우, O(nlogn)에 얻는 것이 가능하다.
#
# example
# count_sort([4,3,1,3,3,6,7,7,1])
# result : [1, 1, 3, 3, 3, 4, 6, 7, 7]