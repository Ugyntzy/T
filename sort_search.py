def bubble_sort_2d(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    n = rows * cols
    
    def get_value(index):
        row = index // cols
        col = index % cols
        return arr[row][col]

    def set_value(index, value):
        row = index // cols
        col = index % cols
        arr[row][col] = value

    for i in range(n):
        for j in range(0, n - i - 1):
            if get_value(j) > get_value(j + 1):
                temp = get_value(j)
                set_value(j, get_value(j + 1))
                set_value(j + 1, temp)

def search_element(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                print(f"Element {target} found at position: ({i}, {j})")
                return
    print(f"Element {target} not found in the array.")

def main():
    # Initialize a sample 2D array
    arr = [
        [34, 7, 23, 32],
        [5, 62, 31, 1],
        [2, 45, 67, 8]
    ]
    print("Original array:")
    for row in arr:
        print(row)

    # Sort the 2D array
    bubble_sort_2d(arr)
    print("\nSorted array:")
    for row in arr:
        print(row)

    # Ask the user to enter the element to search for
    target = int(input("\nEnter the element you want to search for: "))
    
    # Search for the element in the sorted array
    search_element(arr, target)

if __name__ == "__main__":
    main()
