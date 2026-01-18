def character_frequency(text):
    freq = {}

    for char in text.strip():
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