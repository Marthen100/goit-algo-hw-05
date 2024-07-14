def binary_search(arr, value):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] < value:
            left = mid + 1
        elif arr[mid] > value:
            right = mid - 1
        else:
            # Exact match found, setting upper_bound to this index
            upper_bound = mid
            # Continue to search for lower bounds of the same number to get the smallest 'greater or equal' index
            right = mid - 1
    
    # If no exact match is found, set upper_bound to the left index which will be the smallest number >= value
    if upper_bound is None:
        if left < len(arr):
            upper_bound = left
        else:
            upper_bound = -1  # When 'value' is greater than all elements in the array

    return (iterations, arr[upper_bound] if upper_bound != -1 else None)

# Example usage:
arr = [0.1, 1.5, 3.5, 4.2, 7.8, 9.0]
value = 4.2
result = binary_search_with_upper_bound(arr, value)
print(result)  # Output should show the number of iterations and the upper bound element