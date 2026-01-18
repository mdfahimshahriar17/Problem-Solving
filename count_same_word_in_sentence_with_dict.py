
def count_same_word_in_sentence(sentence):

    freq = {}

    for word in sentence.split():
        if word not in freq:
            freq[word] = 1

        else:
            freq[word] += 1

    return freq

sentence = "python is easy and python is powerful"
result = count_same_word_in_sentence(sentence)

print(result)