def character_frequency(text):
    freq = {}

    for char in text:
        if char == " ":
            continue
        if char not in freq:
            freq[char] = 1

        else:
            freq[char] += 1

    return freq

text = "python is easy and python is powerful"
result = character_frequency(text)

print(result)





def frequency_of_characters(text):
    freq = {}

    for cha in text:
        if cha not in freq:
            freq[cha] = 1

        else:
            freq[cha] += 1

    return freq
#input text without space
text = input().lower()
result = frequency_of_characters(text=text)
if result:
    for key, val in result.items():
        print(f"{key} {val}")
