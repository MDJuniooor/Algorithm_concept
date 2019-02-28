# Bubble Sort
def bubble_sort(List):
    for loop in range(len(List)-1):
        for i in range(len(List)-loop-1):
            # 인접한 원소가 작으면 교환한다.
            if List[i] > List[i+1]:
                List[i],List[i+1] = List[i+1],List[i]
    print(List)

# time complexity : O(n**2)
# example
# bubble_sort([3,2,4,5,1])
# result : [1,2,3,4,5]