def cezar(text, key, alphabet=None):
    letters_low = 'abcdefghijklmnopqrstuvwxyz'
    letters_upp = letters_low.upper()
    if alphabet is None:
        alphabet = []
    result = ""
    for i in text:
        if len(alphabet) != 0:
            if i == alphabet[0] or i == alphabet[0].upper():
                i = alphabet[1]
                result += i
            else:
                result += i.lower()
        else:
            if i == " " or i.isalpha() == False:
                result += i.lower()
            else:
                if i in letters_low:
                    result += letters_low[(letters_low.index(i)+key) % len(letters_low)]
                elif i in letters_upp:
                    result += letters_upp[(letters_upp.index(i)+key) % len(letters_upp)].lower()

    return result


data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"
enc = cezar(data, 5, ["a", "B"])
print(enc)
