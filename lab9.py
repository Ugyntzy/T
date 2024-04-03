def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    return [replacement if x == target else x for x in arr]

def main():
    # Prompt the user to input an array of integers
    input_array = input("Enter an array of integers separated by spaces: ")
    # Store the elements in an array in a Python list
    arr = list(map(int, input_array.split()))
    
    # Sort the input array in ascending order using quick sort
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    
    # Allow the user to specify a target element to search for in the sorted array
    target = int(input("Enter the target element to search for: "))
    
    # Check if the target element is in the sorted array
    if target in sorted_arr:
        # Prompt the user to input a replacement element
        replacement = int(input("Enter the replacement element: "))
        # Replace all occurrences of the target element with the replacement element
        modified_arr = replace_elements(sorted_arr, target, replacement)
        print(f"Modified array after replacing elements: {modified_arr}")
    else:
        print(f"Target element {target} not found in the array.")

if __name__ == "__main__":
    main()
