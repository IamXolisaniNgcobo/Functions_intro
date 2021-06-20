def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    backwards = string[::-1].casefold()
    return backwards == string.casefold()


def palindrome_sentence(pal_sentence):
    string =''
    for char in pal_sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

word = input('Please enter word to check: ')
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
