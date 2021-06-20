import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting the user until
    valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return:The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print('{0} is not a valid number! try again'.format(temp))


print(input.__doc__)
print("*" * 80)
help(get_integer)
print("*" * 80)
print(get_integer.__doc__)
print('*' * 80)
highest = 1000
answer = random.randint(1, highest)
print(answer)  # TODO: remove after testing
guess = 0  # initialise to any number that is not equal to answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(': ')
    if guess == 0:
        print("Game over!")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess > answer:
            print("Please guess lower")
        elif guess < answer:
            print("Please guess higher")
        guess = int(input())
