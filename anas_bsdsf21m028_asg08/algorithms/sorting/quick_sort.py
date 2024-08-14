def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort(arr, low, high):
    """
    Quick Sort algorithm.

    This function sorts an array by picking a pivot element and partitioning the array around the pivot.

    Parameters:
    arr (List[int]): The array to be sorted.
    low (int): Starting index.
    high (int): Ending index.

    Returns:
    List[int]: The sorted array.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(quick_sort(arr, 0, len(arr)-1))