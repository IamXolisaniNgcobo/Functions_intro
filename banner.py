# def banner_text(text, screen_width):
# positional-or-keyword: specifies an argument that can be passed either positionally or as a keyword argument.
# This is the default kind of parameter, for example foo and bar in the following:
def banner_text(text='', screen_width=80):
    # screen_width = 50
    if len(text) > screen_width - 4:
        raise ValueError('String {0} is larger than the specified width {1}'.format(text, screen_width))

    if text == '*':
        print('*' * screen_width)
    else:
        output_string = '**{}**'.format(text.center(screen_width - 4))
        print(output_string)
        # return none, perfoming action


banner_text("*", 66)
banner_text("Always look on the bright side of life...", 66)
banner_text("If life seems jolly rotten,", 66)
banner_text("There's something you've forgotten!", 66)
banner_text("And that's to laugh and smile and dance and sing,", 66)
# keyword arguments
banner_text(screen_width=66)
banner_text("When you're feeling in the dumps,", 66)
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!", 66)
banner_text("And... always look on the bright side of life...", 66)
banner_text("*", 66)
