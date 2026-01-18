def most_frequent_element(elements):
    freq = {}

    for elm in elements:
        freq[elm] = freq.get(elm, 0) + 1

    max_freq = max(freq.values())

    answer = None
    for key, val in freq.items():
        if val == max_freq:
            if answer is None or key < answer:
                answer = key

    return answer


elements = [5, 5, 1, 1, 3]
result = most_frequent_element(elements)
print(result)