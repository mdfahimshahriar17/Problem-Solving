def first_non_repeating_character(text):
    freq = {}

    for cha in text:
        if cha not in freq:
            freq[cha] = 1

        else:
            freq[cha] += 1

    for k, v in freq.items():
        if v == 1:
            return k
    

    return -1

s = input().lower()
result = first_non_repeating_character(text=s)
print(result)