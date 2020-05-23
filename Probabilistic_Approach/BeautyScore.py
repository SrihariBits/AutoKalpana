
def beautyScore_8(shingle):
    s = shingle

    # Tha Tha Kita Thi Thi Kita
    if s[0] == s[1] and s[4] == s[5]:
        return 1

    # Tha Tha Tha Tha Ki Ta Tha Ka
    elif s[0] == s[1] == s[2] == s[3]:
        return 1

    # Tha Tha Ki Ta Ki Ta Tha Ka
    elif s[0] == s[1] and s[2] == s[4] and s[3] == s[5]:
        return 1

    # Tha Ka Tha Ri Ki Ta Tha Ka
    elif s[0] == s[2] and s[1] != s[3]:
        return 1

    # Tha Ka Jo Nu Tha Tha Ki Ta
    elif s[5] == s[6]:
        return 1

    # Tha Tha Thi Thi Thom Thom Nam Nam
    elif s[0] == s[1] and s[2] == s[3] and s[4] == s[5] and s[6] == s[7]:
        return 1

    # Tha Ka Thi Mi Tha Ka Ju Nu
    elif s[0] == s[4] and s[1] == s[5]:
        return 1

    # Num Num Tha Ka Tha Ka Thi Mi
    elif s[0] == s[1] and s[2] == s[4] and s[3] == s[5]:
        return 1

    # Tha Din Din Ki Ki Tha Tha Thom
    elif s[1] == s[2] and s[3] == s[4] and s[5] == s[6]:
        return 1

    # Tha Tha Ka Tha Thi Ki Na Thom
    elif s[0] == s[1] == s[3] and s[0] != s[2]:
        return 1

    # Tha Ki Ta Tha Ka Tha Ki Ta
    elif s[0] == s[5] and s[1] == s[6] and s[2] == s[7]:
        return 1

    # Tha Ki Ta Tha Ki Ta Tha Ka
    elif s[0] == s[3] and s[1] == s[4] and s[2] == s[5]:
        return 1

    else:
        return 0


def sim(a, b, k, dist):
    flag = True
    for i in range(1, k):
        if dist[int(a[i])][int(b[i])] != dist[int(a[i-1])][int(b[i-1])]:
            flag = False
    return flag


def beautyScore_16(shingle, dist):
    # 7 + 7 + 2
    for i in range(3):
        str1 = shingle[i:i+7]
        str2 = shingle[i+7:i+14]
        if sim(str1, str2, 7, dist):
            return 1

    # 3 + 3 + 3 + 7
    for i in range(8):
        str1 = shingle[i:i+3]
        str2 = shingle[i+3:i+6]
        str3 = shingle[i+6:i+9]
        if sim(str1, str2, 3, dist) and sim(str2, str3, 3, dist) and dist[int(str1[0])][int(str2[0])] == dist[int(str2[0])][int(str3[0])]:
            return 1

    # 6 + 6 + 4
    for i in range(5):
        str1 = shingle[i:i+6]
        str2 = shingle[i+6:i+12]
        if sim(str1, str2, 6, dist):
            return 1

    # 5 + 5 + 6
    for i in range(7):
        str1 = shingle[i:i+5]
        str2 = shingle[i+5:i+10]
        if sim(str1, str2, 5, dist):
            return 1

    # 5 + 5 + 5 + 1
    for i in range(2):
        str1 = shingle[i:i+5]
        str2 = shingle[i+5:i+10]
        str3 = shingle[i+10:i+15]
        if sim(str1, str2, 5, dist) and sim(str2, str3, 5, dist) and dist[int(str1[0])][int(str2[0])] == dist[int(str2[0])][int(str3[0])]:
            return 1

    # 4 + 4 + 4 + 4
    for i in range(5):
        str1 = shingle[i:i+4]
        str2 = shingle[i+4:i+8]
        str3 = shingle[i+8:i+12]
        if sim(str1, str2, 4, dist) and sim(str2, str3, 4, dist) and sim(str1, str3, 4, dist):
            return 1

    # 3 + 3 + 3 + 3 + 4
    for i in range(5):
        str1 = shingle[i:i+3]
        str2 = shingle[i+3:i+6]
        str3 = shingle[i+6:i+9]
        str4 = shingle[i+9:i+12]
        # Relaxed rule
        if sim(str1, str2, 3, dist) and sim(str2, str3, 3, dist) and sim(str3, str4, 3, dist):
            return 1

    return 0
