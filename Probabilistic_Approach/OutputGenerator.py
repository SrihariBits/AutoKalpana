import random
import winsound
import time

flag_8 = True
flag_16 = True


def getValue(c):
    '''
    if c == '1':
        return 262
    elif c == '2':
        return 293
    elif c == '3':
        return 311
    elif c == '4':
        return 392
    elif c == '5':
        return 440
    else:
        return 523
    '''
    notes = ""
    if c == '1':
        notes = notes + "S"+"\u2193"+"-"
    elif c == '2':
        notes = notes + "R"+"\u2193"+"-"
    elif c == '3':
        notes = notes + "G"+"\u2193"+"-"
    elif c == '4':
        notes = notes + "P"+"\u2193"+"-"
    elif c == '5':
        notes = notes + "D"+"\u2193"+"-"
    if c == '6':
        notes = notes + "S"+"-"
    elif c == '7':
        notes = notes + "R"+"-"
    elif c == '8':
        notes += "G"+"-"
    elif c == '9':
        notes = notes + "P"+"-"
    elif c == '10':
        notes = notes + "D"+"-"
    if c == '11':
        notes = notes + "S"+"\u2191"+"-"
    elif c == '12':
        notes = notes + "R"+"\u2191"+"-"
    elif c == '13':
        notes = notes + "G"+"\u2191"+"-"
    elif c == '14':
        notes = notes + "P"+"\u2191"+"-"
    elif c == '15':
        notes = notes + "D"+"\u2191"+"-"
    return notes


def outputGenerator(twoGraph, fourGraph, eightGraph, sixteenGraph):
    notes = ""
    previous_2 = "12"
    previous_4 = "3231"
    previous_8 = "23234345"
    previous_16 = "3323212212132312"
    output = ""
    iter = 0
    while iter < 100:
        randNum = random.randint(1, 1000)

        if len(output) > 2:
            previous_2 = output[-2:]
        flag_2 = False
        for grams in twoGraph[previous_2][1]:
            if twoGraph[previous_2][1][grams] > randNum:
                previous_2 = grams
                flag_2 = True
                break
        if not flag_2:
            previous_2 = grams

        if len(output) > 4:
            previous_4 = output[-4:]
        for grams in fourGraph[previous_4][1]:
            if fourGraph[previous_4][1][grams] > randNum:
                previous_4 = grams
                break

        if len(output) > 8:
            previous_8 = output[-8:]
        try:
            flag_8 = True
            for grams in eightGraph[previous_8][1]:
                if eightGraph[previous_8][1][grams] > randNum:
                    previous_8 = grams
                    break
        except KeyError:
            flag_8 = False

        if len(output) > 16:
            previous_16 = output[-16:]
        try:
            flag_16 = True
            for grams in sixteenGraph[previous_16][1]:
                if sixteenGraph[previous_16][1][grams] > randNum:
                    previous_16 = grams
                    break
        except KeyError:
            flag_16 = False

            '''
        for character in previous:
            winsound.Beep(getValue(character), 500)
            time.sleep(0.100)
            '''

        if previous_16[0:8] == previous_8 and flag_8 and flag_16:
            output += previous_16
            # print(previous_16)
        elif previous_8[0:4] == previous_4 and flag_8:
            output += previous_8
            # print(previous_8)
        elif previous_4[0:2] == previous_2:
            output += previous_4
            # print(previous_4)
        elif previous_16[0:4] == previous_4 and flag_16:
            output += previous_4
            # print(previous_4)
        else:
            output += previous_2
            # print(previous_2)

        iter += 1
    for i in range(len(output)):
        notes = notes + getValue(output[i])

    print(notes)

    # return output
