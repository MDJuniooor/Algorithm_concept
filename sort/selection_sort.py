# Selection Sort

def selection_sort(List):
    n = len(List)
    for i in range(n):
        MIN = i
        for j in range(i+1,n):
            if List[MIN] > List[j]:
                MIN = j
        if MIN != i:
            List[MIN],List[i] = List[i],List[MIN]
    print(List)
# 평균 O(n**2) , 최악 O(n**2)
# 특징 : 교환의 회수가 버블, 삽입정렬보다 작다.

print(selection_sort([3,3,5,11,2,4]))