
def linear_search(data, target):
    """
    This function searches for a target in a list of data by checking each element in the list.

    Args:
    data: a list of elements
    target: the element to search for in the list

    Returns:
    True if the target is found in the list, False otherwise
    """
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False
