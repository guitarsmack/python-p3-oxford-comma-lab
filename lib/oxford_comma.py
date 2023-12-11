def oxford_comma(items):
    if len(items) < 3:
        return ' and '.join(items)
    else:
        # first = ', '.join(items[:-1])
        # last = f' and {items[-1]}'
        # print(f'{first}{last}')
        items[-1] = 'and ' + items[-1]
        return ', '.join(items)
