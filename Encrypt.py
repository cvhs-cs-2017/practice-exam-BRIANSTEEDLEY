"""Write a code that will take (AnyString) and substitute all vowels with
character's like $#%^&* etc..... but DO NOT USE ' or " as any of your characters."""

def Steve(pie):
    CipherText = ''
    for i in pie:
        if i == 'a':
            CipherText = CipherText + '$'
        elif i == 'e':
            CipherText = CipherText + '#'
        elif i == 'i':
            CipherText = CipherText + '%'
        elif i == 'o':
            CipherText = CipherText + '^'
        elif i == 'u':
            CipherText = CipherText + '&'
        else:
            CipherText = CipherText + i
    return CipherText
print(Steve('CipherText'))
