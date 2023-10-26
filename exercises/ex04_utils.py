"""EX04 - list Utility Functions."""
__author__ = "730669144"


def all(int_list: list[int], given_int: int) -> bool:
    """Given a list of ints and an int, all should return a bool indicating whether or not all the ints in the list are the same as the given int."""
    idx: int = 0  # index for checking each element in the list to see if it matches with the given int
    if len(int_list) == 0:
        return False
    while idx < len(int_list):
        if int_list[idx] != given_int:
            return False  # if the current int in the list is not equal to the given integer, return false
        else:
            idx += 1
    return True  # will only reach this part if every interger in the list matches with the given integer.


def max(input: list[int]) -> int:
    """Given a list of integers, returns the largest integer in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx_1: int = 0
    idx_2: int = 1  # initializes two index variables to compare 2 elements within the list to determ which is larger.
    while idx_1 < len(input) and idx_2 < len(input):  # while both indexes are less that the length of the list
        if input[idx_1] > input[idx_2]: 
            idx_2 += 1  # for first loop, if the first int is larger than the second, the next loop will compare the first number and the third number, continuing on.
        else: 
            idx_1 += 1  # for the first loop, if the first int is smaller than the second, the next loop will compare the second integer and the second integer, but the next next loop will compare the third and second integer.
    if idx_1 == len(input):  
        idx_1 -= 1
    if idx_2 == len(input):
        idx_2 -= 1  # if one of the indexes are equal to the length of the list(caused by how I coded the while loop), subtract one from the respective list. This prevents an index out of bounds error.
    if input[idx_1] > input[idx_2]:
        return input[idx_1]  
    else:
        return input[idx_2]  # finally, if the current "first" integer is larger than the "second" integer, return the first integer. Else return the opposite. 


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given 2 lists, compares each index of the list and returns true only if every int and every index is the same."""
    if len(list_1) != len(list_2):
        return False
    idx: int = 0
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True
        
