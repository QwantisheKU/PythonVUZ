def f21(x):
    if x[2] == 'fancy':
        if x[0] == 1976:
            if x[1] == 'vcl':
                return 6
            elif x[1] == 'oz':
                return 7
            else:
                return 8
        else:
            return 9
    else:
        if x[0] == 1976:
            if x[3] == 'click':
                return 0
            elif x[3] == 'toml':
                return 1
            else:
                return 2
        else:
            if x[1] == 'vcl':
                return 3
            elif x[1] == 'oz':
                return 4
            else:
                return 5
print(f21([1976, 'vcl', 'self', 'click']))
        