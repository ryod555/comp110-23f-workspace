"""Excercise 6, Dictionary Functions."""

__author__ = "730660144"


def invert(diction: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, inverts the keys and its values."""
    inverted: dict[str, str] = dict()
    for key in diction:
        inverted[diction[key]] = key
    return inverted


def favorite_color(names_colors: dict[str, str]) -> str:
    """Given a dictionary of names and colors, will respond the color with the most frequency."""
    colors: dict[str, int] = {}
    for key in names_colors:
        if names_colors[key] in colors:
            colors[names_colors[key]] += 1
        else:
            colors[names_colors[key]] = 1
    print(colors)
    favorite_val: int = 0
    fav_col: str = ()
    for key in colors:
        if int(colors[key]) > favorite_val:
            favorite_val = int(colors[key])
            fav_col = key
    return fav_col
        

def count(strings: list[str]) -> dict[str, int]:
    """Given a list of strings, creates a dictionary with a count of the frequency of each string in the list."""
    vals: dict[str, int] = {}
    for i in range(len(strings)):
        if strings[i] in vals:
            vals[strings[i]] += 1
        else:
            vals[strings[i]] = 1
    return vals
                   

def alphabetizer(strings: list[str]) -> dict[str, list[str]]:
    """Given a list[str], this function will produce a dict[str, list[str]] where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    alpha: dict[str, list[str]] = {}
    for i in range(len(strings)):
        if ((strings[i])[0]).lower() in alpha:
            alpha[(strings[i])[0]].append(strings[i])
        else:
            alpha[(strings[i])[0].lower()] = [(strings[i])]
    return alpha


def update_attendance(diction: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    if day in diction:
        diction[day].append(student)
    else:
        diction[day] = student
    return diction


def main():
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    update_attendance(attendance_log, "Wednesday", "Kaleb")
    print(attendance_log)


if __name__ == "__main__":
    main()
