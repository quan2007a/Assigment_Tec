def check_hex(color):

    if len(color) != 7:
        return False

    if color[0] != '#':
        return False

    for i in range(1, 7):
        ch = color[i]

        if ('0' <= ch <= '9') or ('A' <= ch <= 'F') or ('a' <= ch <= 'f'):
            pass
        else:
            return False

    return True


# test
print(check_hex("#1A2b3C"))   # True
print(check_hex("#ABCDEF"))   # True
print(check_hex("#123abz"))   # False