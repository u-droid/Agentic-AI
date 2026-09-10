# Check if list is sorted
def check_sorted(arr):
    """Return True when the list is sorted in non-decreasing order."""
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# Directional
def check_sorted_directional(arr, reverse=False):
    """Return True when the list is sorted ascending or descending."""
    if reverse:
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                return False
    else:  
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
    return True

# Better one
import operator

def check_sorted_directional_clean(arr, reverse=False):
    """Return True when the list follows the requested sort direction."""
    op = operator.lt if reverse else operator.gt
    for i in range(len(arr)-1):
        if op(arr[i], arr[i+1]):
            return False
    return True


if __name__=="__main__":
    sorted = [1,2,3,4,5]
    assert check_sorted(sorted)==True
    unsorted = [2,3,4,1]
    assert check_sorted(unsorted)==False
    dups = [1,2,2,3,4,5]
    assert check_sorted(dups)==True

    print("code runs successfully")