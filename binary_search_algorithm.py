# Programe of Binary Search Algorithm.

def binary_search(my_list, element):
    """
    Perform a binary search on a sorted list to find the index of the target element.

    Parameters:
    my_list (list): A list of sorted integers.
    element (int): The target integer to search for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    start = 0
    end = len(my_list) -1
    steps = 1

    while start <= end:
        print(f"Step {steps}: {my_list[start : end + 1]}")
        steps += 1

        middle = (start + end) // 2

        if element == my_list[middle]:
            return middle
        
        elif element < my_list[middle]:
            end = middle - 1

        else:
            start = middle + 1
    
    return -1

def main():
    while True:
        try:
            # Take input and convert to list of integers
            my_list = [int(x) for x in input("Enter numbers with spaces: ").split()]
            # Sort the list
            my_list.sort()
            # Take the target element input
            target = int(input("Enter the target number: "))
        
            
            # Perform binary search
            result = binary_search(my_list, target)
    
            # Print the result
            if result != -1:
                print(f"Element is found at index {result}")
            else:
                print("Element not found!")
            break
        except ValueError:
            print("Error: Please enter valid Numbers!")

if __name__ == "__main__":
    main()