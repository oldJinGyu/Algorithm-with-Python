results = []
    
def _perm_swap (arr, depth, r):
    if (depth == r):
        print(arr)
        results.append(arr[:])
        return
 
    for i in range(depth, len(arr)):
            # 위치를 바꿈
        arr[i], arr[depth] = arr[depth], arr[i]
        _perm_swap(arr, depth+1, r)
            # 다시 되돌림
        arr[i], arr[depth] = arr[depth], arr[i]

_perm_swap([1,2,3,4], 0, 2)
print(results)