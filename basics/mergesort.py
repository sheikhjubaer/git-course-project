def debug_print(debug_msg=None, **kwargs):
    """Helper function to print debug information."""
    if debug_msg:
        print(debug_msg)

    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


def mergesort(array):
    if len(array) <= 1:
        return array

    # Debug: Print the array being split
    debug_print(array=array)

    m = len(array) // 2
    debug_print(m=m)

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists."""
    merged = []

    # Debug: Indicate that merging is starting
    debug_print(debug_msg="Merging...")
    debug_print(left=left, right=right)

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # Add remaining elements
    if len(left) > 0:
        merged += left
    else:
        merged += right

    # Debug: Show the merged result
    debug_print(merged=merged)
    return merged


if __name__ == "__main__":
    # Read user input
    input_str = input("Enter numbers, separated by ',': ").strip()

    # Remove square brackets if present
    if input_str.startswith("[") and input_str.endswith("]"):
        input_str = input_str[1:-1]

    # Split the input into a list
    input_list = input_str.split(",")

    # Debug: Show input list
    debug_print(input_list=input_list)

    # Convert strings to integers
    value_list = []
    for x in input_list:
        try:
            value_list.append(int(x.strip()))  # Strip extra spaces
        except ValueError as err:
            print("Invalid input.")
            quit(1)

    # Debug: Show parsed value list
    debug_print(value_list=value_list)

    # Sort the list
    sorted_list = mergesort(value_list)

    # Print the final sorted list
    print(sorted_list)
