def insertion_sort(arr):
    """
    Insertion Sort algorithm.

    This function sorts an array by building a sorted array one item at a time.

    Parameters:
    arr (List[int]): The array to be sorted.

    Returns:
    List[int]: The sorted array.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(insertion_sort(arr))