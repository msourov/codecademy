def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')


def get_size(dt):
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if dt == 'brewed coffee':
        if res == 'a':
            return 'small', dt, 2
        elif res == 'b':
            return 'medium', dt, 3
        elif res == 'c':
            return 'large', dt, 4
        else:
            print_message()
            return get_size(dt)
    elif dt == 'mocha':
        if res == 'a':
            mocha_type, price1 = order_mocha(3)
            return 'small', mocha_type, price1
        elif res == 'b':
            mocha_type, price1 = order_mocha(3.5)
            return 'medium', mocha_type, price1
        elif res == 'c':
            mocha_type, price1 = order_mocha(4)
            return 'large', mocha_type, price1
        else:
            print_message()
            return get_size(dt)
    elif dt == 'latte':
        if res == 'a':
            latte_add_on, price1 = order_latte(3.5)
            return 'small', latte_add_on, price1
        elif res == 'b':
            latte_add_on, price1 = order_latte(4)
            return 'medium', latte_add_on, price1
        elif res == 'c':
            latte_add_on, price1 = order_latte(4.5)
            return 'large', latte_add_on, price1
        else:
            print_message()
            return get_size(dt)


def order_mocha(price1):
    while True:
        res = input('Would you like to try our limited-edition peppermint mocha? \n'
                    '[a] Sure! (Costs +1$)\n[b] Maybe next time!\n[d] Exit \n>')
        if res == 'a':
            return 'peppermint mocha', price1+1
        elif res == 'b':
            return 'mocha', price1+0
        elif res == 'exit':
            exit()
        else:
            return order_mocha(price1)
        print_message()


def order_latte(price1):
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')

    if res == 'a':
        return 'latte', price1+0.5
    elif res == 'b':
        return 'non-fat latte', price1+0.0
    elif res == 'c':
        return 'soy latte', price1+1
    else:
        print_message()
        return order_latte(price1)


price = 0


def total_price(val):
    global price
    price += val
    return price
