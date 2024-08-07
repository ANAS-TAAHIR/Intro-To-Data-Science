def bubble_sort(arr):
    """
    Bubble Sort algorithm.

    This function sorts an array by repeatedly stepping through the list, 
    comparing adjacent elements and swapping them if they are in the wrong order. 

    Parameters:
    arr (List[int]): The array to be sorted.

    Returns:
    List[int]: The sorted array.
    """
            
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))