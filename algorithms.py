import random

'''
Implementation of basic search and sort algorithms.

-   program generates list of random numbers using given range,
-   program sorts generated list using selection sort algorithm,
-   program searches for given number using binary search algorithm,
-   program outputs number of tries and result

'''

def generate_random():

    random_list = []
    for i in range(2000):
        # Generate random list of numbers and append them to the list
        random_list.append(random.randrange(1, 9999, 1))

    return random_list

def selection_sort(random_list):

    limit = len(random_list)

    # Implementation of selection sort algorithm
    for i in range(limit - 1):
        min_value_index = i

        for j in range(i + 1, limit):
            if random_list[j] < random_list[min_value_index]:
                min_value_index = j

        if min_value_index != i:
            random_list[i], random_list[min_value_index] = random_list[min_value_index], random_list[i]

    return random_list

def binary_search(sorted_list, target):

    l = 0
    r = len(sorted_list)-1
    mid = 0
    count = 0

    # Implementation of binary search algorithm
    if mid == target:

        # Count first try
        count += 1
        print("Moves: ", count)
        return True

    while l <= r:
        mid = int(l + ((r - l)/ 2))

        # Count rest of tries
        count += 1

        if sorted_list[mid] == target:

            # Inform user how many tries has been used to find the number and return True.
            print(f"Found {target} in {count} moves.")
            return True

        elif sorted_list[mid] < target:
            l = mid + 1

        else:
            r = mid - 1

    # Inform user how many tries it took to determine that the number
    # is not in the list and return False
    print(f"Not found. Number of moves: {count}.")
    return False


print("Sorted list: ")
sorted_list = (selection_sort(generate_random()))
print(sorted_list)

# Perform binary search on sorted list in order to find given number.
print(binary_search(sorted_list, 6349))