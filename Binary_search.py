# Binary Search Algorithm in Python

def binary_search(arr, target):
    """
    This function searches for 'target' inside the sorted list 'arr'.
    If found, it returns the index of the target.
    If not found, it returns -1.
    """

    # Step 1: Set the starting and ending positions
    left = 0
    right = len(arr) - 1

    # Step 2: Keep checking while there is still a search space
    while left <= right:
        # Step 3: Find the middle index
        mid = (left + right) // 2

        # Step 4: Check if the middle element is the target
        if arr[mid] == target:
            return mid  # Found the target

        # Step 5: If target is smaller, search in the left half
        elif arr[mid] > target:
            right = mid - 1

        # Step 6: If target is bigger, search in the right half
        else:
            left = mid + 1

    # Step 7: If we exit the loop, the target was not found
    return -1


# Example Usage
numbers = [1, 3, 5, 7, 9, 11, 13]
target_number = 7

result = binary_search(numbers, target_number)

if result != -1:
    print(f"Number {target_number} found at index {result}")
else:
    print(f"Number {target_number} not found in the list")
