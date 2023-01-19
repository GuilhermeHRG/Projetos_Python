def crypt(phrase):
    traducer = ""
    for letter in phrase:
        if letter in "Aa":
            traducer = traducer + "4"
        elif letter in "Bb":
            traducer = traducer + "8"
        elif letter in "Cc":
            traducer = traducer + "₢"
        elif letter in "Dd":
            traducer = traducer + "D"
        elif letter in "Ee":
            traducer = traducer + "3"
        elif letter in "Ff":
            traducer = traducer + "7"
        elif letter in "Gg":
            traducer = traducer + "6"
        elif letter in "Hh":
            traducer = traducer + "#"
        elif letter in "Ii":
            traducer = traducer + "1"
        elif letter in "Jj":
            traducer = traducer + "!"
        elif letter in "Kk":
            traducer = traducer + "~"
        elif letter in "Ll":
            traducer = traducer + "0"
        elif letter in "Mm":
            traducer = traducer + "n"
        elif letter in "Nn":
            traducer = traducer + "m"
        elif letter in "Oo":
            traducer = traducer + "°"
        elif letter in "Pp":
            traducer = traducer + "ç"
        elif letter in "Qq":
            traducer = traducer + "@"
        elif letter in "Rr":
            traducer = traducer + "*"
        elif letter in "Ss":
            traducer = traducer + "$"
        elif letter in "Tt":
            traducer = traducer + "T"
        elif letter in "Uu":
            traducer = traducer + "u"
        elif letter in "Vv":
            traducer = traducer + "V"
        elif letter in "Ww":
            traducer = traducer + "w"
        elif letter in "Xx":
            traducer = traducer + "x"
        elif letter in "Yy":
            traducer = traducer + "y"
        elif letter in "Zz":
            traducer = traducer + "z"
        else:
            traducer = traducer + letter
    return f'Old phrase: {phrase} ' \
           f'\nNew phrase: {traducer}'


print("E N C R Y P T O R\n")
print(crypt(input("Type it a phrase: ")))
