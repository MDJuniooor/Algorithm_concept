# Sequantial Search

# List : 찾을 자료, key : 찾고자 하는 숫자
def sequentail_search(List, key):
    for i in range(len(List)):
        # 정렬이 되어 있는 경우
        # if List[i] > key: break
        if List[i] == key:
            return i
    return -1
