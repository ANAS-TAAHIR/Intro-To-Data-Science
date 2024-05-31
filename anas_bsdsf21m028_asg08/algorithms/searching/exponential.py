def binary_search(arr, x, start, end):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, x, start, mid - 1)
        else:
            return binary_search(arr, x, mid + 1, end)
    return -1

def exponential_search(arr, x):
    """
    This function searches for a target in a sorted list of data by doubling the index of the target until it is found.

    Args:
    arr: a list of elements
    x: the element to search for in the list

    Returns:
    the index of the target if it is found in the list, -1 otherwise
    """
    if arr[0] == x:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= x:
        i = i * 2
    return binary_search(arr, x, i // 2, min(i, len(arr)-1))