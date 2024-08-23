def sorted_squared_array(arr):
    n = len(arr)
    result = [0] * n  
    left, right = 0, n - 1
    idx = n - 1  
    
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2
        
        if left_square > right_square:
            result[idx] = left_square
            left += 1
        else:
            result[idx] = right_square
            right -= 1
        
        idx -= 1
    
    return result
