def spin_words(string):
    reversed_sentance = string
    list_string = string.split()
    for words in list_string:
        if len(words) >= 5:
            reverse_word = words[::-1]
            reversed_sentance = reversed_sentance.replace(words, reverse_word)
    return reversed_sentance



