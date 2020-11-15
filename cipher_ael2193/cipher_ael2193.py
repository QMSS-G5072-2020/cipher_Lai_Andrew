def cipher(text, shift, encrypt=True):
    """
        Transform words into using cipher.
    Parameters:
    -----------
    text = A string that is inputted into the function to be transformed
    shift = An integer that indicates how many places down the alphabet the word is replace with
    encrypt = A boolean value (True and False)
        If True: text will be encrypted
        If False: text will be decrypted
        
    Examples:
    -----------
    cipher("hello", 1)
    "ifmmp"
    cipher("hello", -1)
    "gdkkn"
    cipher("hello", 1, encrypt = False)
    "ifmmp"
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
