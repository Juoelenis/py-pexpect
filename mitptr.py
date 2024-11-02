c = ['12', '-', '24', '/', '6', '+', '7']
match c:
    case [*before_div, '/', *after_div]:
        ...
The other option would be matching against the general case and trying to find this character to split the list at its index. Like this:

match c:
    case [*_]:
    try:
        i = c.index("/")
        before_div, after_div = c[:i], c[i+1:]
        ...
    except ValueError:
        pass
