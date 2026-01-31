def longest_word(text):
    longest_word = None
    len_l_word = 0

    for word in text:
        len_word = len(word)
        if longest_word == None or len_word > len_l_word:
            longest_word = word
            len_l_word = len(longest_word)

    return longest_word


s = input().lower().split()
result =  longest_word(text=s)
print(result)



#same program using while loop
def longest_word(text):
    
    longest_word = None
    len_l_word = 0

    i = 0

    while i < len(text):

        word = text[i]
        len_word = len(word)
        if longest_word == None or len_word > len_l_word:
            longest_word = word
            len_l_word = len(longest_word)

        i += 1
    return longest_word


s = input().lower().split()
result =  longest_word(text=s)
print(result)