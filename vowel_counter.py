def count_vowels():
    s = input()
    vowels = "aeiouAEIOU"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    print(count)

count_vowels()