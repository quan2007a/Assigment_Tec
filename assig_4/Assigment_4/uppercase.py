def check_course(code):

    if len(code) != 6:
        return False

    # check first 3 characters (A-Z)
    for i in range(0, 3):
        if code[i] < 'A' or code[i] > 'Z':
            return False

    # check last 3 characters (0-9)
    for i in range(3, 6):
        if code[i] < '0' or code[i] > '9':
            return False

    return True


print(check_course("TEC001"))
print(check_course("TeC001"))
print(check_course("ABC12"))
print(check_course("ABCD123"))