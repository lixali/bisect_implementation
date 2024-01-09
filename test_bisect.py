from bisectMy import bisectMy

arr = [1,2,3,4,5,5,5,6,6,7]
b = bisectMy()
target_idx_1 = b.bisect_left(arr, 7)
print(target_idx_1)

target_idx_2 = b.bisect_right(arr, 5)
print(target_idx_2)