# Binary Search

# List : 찾을 자료, key : 찾고자 하는 숫자
# List는 정렬되어 있다고 가정.
def binary_serach(List, key):
    left = 0
    right = len(List) - 1
    while right >= left:
        mid = int((left + right) / 2)
        print(left,right,mid)
        if List[mid] == key : return mid
        elif List[mid] > key : right = mid - 1
        else: left = mid + 1
    return -1

print(binary_serach([1,2,3,4,5,6,7,8,9,10],7))