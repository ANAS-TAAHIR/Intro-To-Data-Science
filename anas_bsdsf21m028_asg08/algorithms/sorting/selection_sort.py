def selection_sort(arr):
    """
    Selection Sort algorithm.

    This function sorts an array by dividing the input list into a sorted and an unsorted sublist. 
    It finds the smallest element in the unsorted sublist and swaps it with the leftmost unsorted element.

    Parameters:
    arr (List[int]): The array to be sorted.

    Returns:
    List[int]: The sorted array.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(selection_sort(arr))