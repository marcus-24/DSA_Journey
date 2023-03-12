list_type = list[float | int]

# %% Bubble sort
def swap(arr: list_type, left_pos: int, right_pos: int) -> None:
    """Swaps list elements in place"""
    arr[left_pos], arr[right_pos] = arr[right_pos], arr[left_pos]


def bubble_sort(arr: list_type):
    """Sorts in ascending order by scanning through the list N times 
    and swapping elements so the second element is higher than the first.
    Performance is O(N^2) since outer loop is N and inner loop is N-1. Great
    for smaller list or list already sorted."""
    for _ in arr:  # needs to iterate through array multiple times for multiple swaps
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                swap(arr, idx, idx + 1)
    return arr

# %% Merge sort
def merge(left: list_type, 
          right: list_type) -> list_type:
    """Iteratively adds the smaller first element out of 
    the two split lists to a new sorted list"""
    result = []  # sorted list
    while (left and right): 

        '''Add smaller value to result'''
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)  # remove first element from list
        else:
            result.append(right[0])
            right.pop(0)

    '''Add remaining value(s) to end of sorted list'''
    if left:
        result += left
    if right:
        result += right

    return result


def merge_sort(lst: list_type) -> list_type:
    """This is a divide and conquer algorithm where a list is 
    divided into smaller lists. Then sorting and merging the smaller lists. 
    The performance is O(N*logN) since splitting is Log N and merging is N.
    Great for list that are large and unordered to start with."""
    if len(lst) <= 1: # break recursion condition
        return lst 

    '''Split list in half'''
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    '''recursion calls'''
    sleft = merge_sort(left)
    sright = merge_sort(right)
    return merge(sleft, sright)

