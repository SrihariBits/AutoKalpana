def rhythmPatternHelper(s):
    # Tha Tha Kita Thi Thi Kita
    if s[0] == s[1] and s[4] == s[5]:
        return True

    # Tha Tha Tha Tha Ki Ta Tha Ka
    elif s[0] == s[1] == s[2] == s[3]:
        return True

    # Tha Tha Ki Ta Ki Ta Tha Ka
    elif s[0] == s[1] and s[2] == s[4] and s[3] == s[5]:
        return True

    # Tha Ka Tha Ri Ki Ta Tha Ka
    elif s[0] == s[2] and s[1] != s[3]:
        return True

    # Tha Ka Thi Mi Tha Ka Ju Nu
    elif s[0] == s[4] and s[1] == s[5]:
        return True

    # Tha Din Din Ki Ki Tha Tha Thom
    elif s[1] == s[2] and s[3] == s[4] and s[5] == s[6]:
        return True

    # Tha Tha Ka Tha Thi Ki Na Thom
    elif s[0] == s[1] == s[3] and s[0] != s[2]:
        return True

    # Tha Ki Ta Tha Ka Tha Ki Ta
    elif s[0] == s[5] and s[1] == s[6] and s[2] == s[7]:
        return True

    # Tha Ki Ta Tha Ki Ta Tha Ka
    elif s[0] == s[3] and s[1] == s[4] and s[2] == s[5]:
        return True

    else:
        return False


def partitionHelper(n):
    if n == 5:
        return [[3, 2], [2, 3]]
    elif n == 6:
        return [[4, 2], [2, 4]]
    elif n == 7:
        return [[5, 2], [2, 5], [4, 3], [3, 4], [3, 2, 2], [2, 3, 2], [2, 2, 3]]
    else:
        return [[6, 2], [2, 6], [5, 3], [3, 5], [4, 2, 2], [2, 4, 2], [2, 2, 4], [3, 3, 2], [3, 2, 3], [2, 3, 3]]
