def anti_vowel(text):
    vowels = ["A", 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = ''
    for t in text:
        if t not in vowels:
            result += t
    print result

anti_vowel("Hey you")