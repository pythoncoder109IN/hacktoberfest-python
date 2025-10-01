# Reverses an array in Python using simple methods

# Example array
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

# Using slicing
reversed_arr = arr[::-1]
print("Reversed array (slicing):", reversed_arr)

# Using reverse() method
arr_copy = arr.copy()  # make a copy to keep original intact
arr_copy.reverse()
print("Reversed array (reverse method):", arr_copy)

# Manual swapping
manual_arr = arr.copy()
start, end = 0, len(manual_arr) - 1
while start < end:
    manual_arr[start], manual_arr[end] = manual_arr[end], manual_arr[start]
    start += 1
    end -= 1
print("Reversed array (manual swap):", manual_arr)
