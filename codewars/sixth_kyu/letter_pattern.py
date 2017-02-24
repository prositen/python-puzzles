def letter_pattern(words):
    l = len(words[0]) if words else 0
    letters = [list({word[x] for word in words}) for x in range(l)]
    return "".join([letter[0] if len(letter) == 1 else '*' for letter in letters])
