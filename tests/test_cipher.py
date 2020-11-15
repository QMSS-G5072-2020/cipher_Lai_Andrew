import pytest



def cipher(text, shift, encrypt=True):

        assert isinstance(shift, int)

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




def test_cipher():
    text = "hello"
    expected = 'ifmmp'
    actual = cipher(text, shift = 1)
    assert actual == expected

test_cipher()

def test_cipher_shift():
    text = "hello"
    expected = 'gdkkn'
    actual = cipher(text, shift = -1)
    assert actual == expected

test_cipher_shift()

def test_cipher_char():
    text = "hello!"
    expected = 'ifmmp!'
    actual = cipher(text, shift = 1)
    assert actual == expected

test_cipher_char()

def test_raise_exception():
    with pytest.raises(AssertionError):
        cipher(text = 'hello!', shift = "1")
test_raise_exception()
