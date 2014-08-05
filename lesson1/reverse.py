def reverse(text):
    i = len(text) - 1
    result = ""
    while i >= 0:
        result += text[i]
        i -= 1
    print result

reverse("Python!")