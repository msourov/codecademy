def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')


def get_size(dt):
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if dt == 'brewed coffee':
        if res == 'a':
            return 'small', 2
        elif res == 'b':
            return 'medium', 3
        elif res == 'c':
            return 'large', 4
        else:
            print_message()
            return get_size(dt)
    elif dt == 'mocha':
        if res == 'a':
            return 'small', 3
        elif res == 'b':
            return 'medium', 3.5
        elif res == 'c':
            return 'large', 4
        else:
            print_message()
            return get_size(dt)
    elif dt == 'latte':
        if res == 'a':
            return 'small', 3.5
        elif res == 'b':
            return 'medium', 4
        elif res == 'c':
            return 'large', 4.5
        else:
            print_message()
            return get_size(dt)


def order_mocha():
    while True:
        res = input('Would you like to try our limited-edition peppermint mocha? \n'
                    '[a] Sure! (Costs +1$)\n[b] Maybe next time!\n[d] Exit \n>')
        if res == 'a':
            return 'peppermint mocha', 1
        elif res == 'b':
            return 'mocha', 0
        elif res == 'exit':
            exit()
        else:
            return order_mocha()
        print_message()


def order_latte():
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

    if res == 'a':
        return 'latte', 0.5
    elif res == 'b':
        return 'non-fat latte', 0.0
    elif res == 'c':
        return 'soy latte', 1
    else:
        print_message()
        return order_latte()

