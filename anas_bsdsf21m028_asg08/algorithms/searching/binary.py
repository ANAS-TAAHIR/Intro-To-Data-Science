def binary_search(arr, target):
    """
    This function searches for a target in a sorted list of data by dividing the search interval in half.

    Args:
    arr: a list of elements
    target: the element to search for in the list

    Returns:
    the index of the target if it is found in the list, None otherwise
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None