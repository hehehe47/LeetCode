def Morse(words):
    m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    l = []
    for word in words:
        morse = ''
        for letter in word:
            morse += m[ord(letter) - 97]
        l.append(morse)
    s = set(l)
    return len(s)


print(Morse(["gin", "zen", "gig", "msg"]))
