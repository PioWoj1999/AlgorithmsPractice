"""Binary search algorithm implementation in Python."""

def binary_search_iterative_method(array:list, x:int) -> int:
# Repeat until the pointers low and high meet each other
    low = 0
    high = len(array)

    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive_method(array:list, x: int, low:int, high:int) -> int|None:
    if high >= low:
        mid = low + (high - low)//2
        # If found at mid, then return it
        if array[mid] == x:
            return mid
        # Search the left half
        elif array[mid] > x:
            return binary_search_recursive_method(array, x, low, mid-1)
        # Search the right half
        else:
            return binary_search_recursive_method(array, x, mid + 1, high)
    else:
        return None


def main() -> None: 
    array = [3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Binary search interactive method, for 4: {binary_search_iterative_method(array=array, x=4)}")
    print(f"Binary search recursive method, for 2: {binary_search_recursive_method(array, 2, 0, len(array))}")

if __name__ == "__main__":
    main()