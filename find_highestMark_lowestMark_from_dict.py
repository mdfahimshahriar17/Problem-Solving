def find_highestMark_lowestMark(students):
    highest_mark_std = {}
    lowest_mark_std = {}

    highest = 0
    lowest = 0

    for key, val in students.items():
        highest = val
        lowest = val

        highest_mark_std.update({key : val})
        lowest_mark_std.update({key : val})
        break

    for key, val in students.items():
        if val > highest:
            highest = val

            highest_mark_std.clear()
            highest_mark_std[key] = val
            
        elif val < lowest:
            lowest = val

            lowest_mark_std.clear()
            lowest_mark_std[key] = val
            

    return (highest_mark_std, lowest_mark_std)



students = {
    "Rahim": 78,
    "Karim": 85,
    "Fahim": 92,
    "Nafis": 88,
    "Zunayed": 69
}

highest, lowest = find_highestMark_lowestMark (students)

h_name, h_mark = next(iter(highest.items()))
l_name, l_mark = next(iter(lowest.items()))

print(f"Highest: {h_name} -> {h_mark}")
print(f"Lowest: {l_name} -> {l_mark}")