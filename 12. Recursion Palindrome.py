def palindrome(word, index):
    left = index
    right = len(word) - index - 1

    if left >= right:
        return f'{word} is a palindrome'

    left_letter = word[index]
    right_letter = word[len(word) - index - 1]

    if left_letter != right_letter:
        return f'{word} is not a palindrome'
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
