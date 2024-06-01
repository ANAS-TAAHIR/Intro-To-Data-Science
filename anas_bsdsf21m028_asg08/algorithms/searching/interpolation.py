def interpolation_search(arr, x):
    """
    This function searches for a target in a sorted list of data by estimating the position of the target.

    Args:
    arr: a list of elements
    x: the element to search for in the list

    Returns:
    the index of the target if it is found in the list, -1 otherwise
    """
    n = len(arr)
    low, high = 0, n - 1

    while low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1
