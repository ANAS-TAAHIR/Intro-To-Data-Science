import math
def jump_search(arr, x):
    """
    This function searches for a target in a sorted list of data by jumping ahead by a fixed number of steps.

    Args:
    arr: a list of elements
    x: the element to search for in the list

    Returns:
    the index of the target if it is found in the list, -1 otherwise
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1