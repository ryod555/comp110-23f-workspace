"""Practice with lists."""

grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[1] = "cereal"
grocery_list.pop(2)

print(grocery_list) 


def max(int_list: list[int]) -> int:
    """Returns the max of a list."""
    if len(int_list) == 0:
        return False
    max: int = int_list[0]
    i: int = 1
    while i < len(int_list):
        if int_list[i] > max:
            max = int_list[i]
        i += 1
    return max
