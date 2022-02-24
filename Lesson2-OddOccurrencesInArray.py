def solution(A):
    lst = [i for i in A if A.count(i)%2!=0]
    return lst[0]

# Code below to test the code
lst = solution([9, 3, 9, 3, 9, 7, 9])
print(lst)
