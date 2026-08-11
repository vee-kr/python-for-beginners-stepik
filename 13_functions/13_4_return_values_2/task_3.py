def is_one_away(word1, word2):
    not_equal = []
    for i in range(len(word1)):
        if len(word1) == len(word2):
            if word1[i] != word2[i]:
                not_equal.append(word1[i])
    return len(not_equal) == 1 and len(word1) == len(word2)


word1, word2 = input(), input()

print(is_one_away(word1, word2))
