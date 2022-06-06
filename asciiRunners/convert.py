from svgpathtools import svg2paths
import numpy as np
from collections import Counter

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

def grayscale_array(svg, ascii, message):

    array = [[]]
    y_old = "000"
    rgb_weights = [0.2989, 0.5870, 0.1140]

    paths, attributes = svg2paths(svg)
    for dict in attributes:
        colour = dict['fill']
        colour_rgb = hex_to_rgb(colour)
        colour_grayscale = np.dot(colour_rgb, rgb_weights)
        y = dict['y']
        if y != y_old:
            array.append([colour_grayscale])
            y_old = y
        else:
            array[-1].append(colour_grayscale)
    flat_list = []
    for sublist in array:
        for item in sublist:
            flat_list.append(item)
    c = Counter(flat_list).most_common(5)
    common = [i[0] for i in c]
    common_sort = common.sort()
    index = 10
    if message != 0:
        background_colour = array[0][0]
        for i in c:
            if i[0] != background_colour:
                message_colour = i[0]
                break
        index = common.index(message_colour)
    ascii_values = list(zip(common, ascii))
    print(index)
    return array, ascii_values, index, message

def grayscale_array_to_string(array, ascii_values, index, message, ascii, contrast_type):
    string = ""
    for row in array:
        for pixel in row:
            if contrast_type == 2:
                closest = min([i[0] for i in ascii_values], key=lambda x:abs(x-pixel))
                string += [ascii_values[i][1] for i in range(5) if ascii_values[i][0] == closest][0]
            elif contrast_type == 1:
                string += ascii[int(pixel/255*5)]
        string += "\n"
    count = 0
    print(index)
    if index != 10:
        position = 0
        for pixel in string:
            if pixel == ascii[index][0]:
                string = string[:position]+message[count]+string[position+1:]
                count = count + 1
            position = position + 1
    return string

def select_characters():
    ascii = input("""Select character type: 

    1. Block elements ██▓▓▒▒░░
    2. Special characters @ & / * .
    3. Terraforms biome #85 ♛ ♜ ♖ ░ ♘
    4. Terraforms biome #22 🏔 ☎ ▒ ░ ☆  
    5. Terraforms biome #27 🖳 ♖ ░ 🗠
    6. Terraforms biome #41 🕱 ⛓ 🕈 ▒ ░
    7. Kanji 亹 乨 乃 个 丷
    8. Custom characters: type 5 characters from darkest to lightest with a comma between each character (no spaces)
    
    """)
    if ascii == "1":
        return ["██", "▓▓", "▒▒", "░░", "  "]
    elif ascii == "2":
        return ["@@", "&&", "//", "**", ".."]
    elif ascii == "3":
        return ["♛♛","♜♜","♖♖","░░","♘♘"]
    elif ascii == "4":
        return ["🏔🏔","☎☎","▒▒","░░","☆☆"]
    elif ascii == "5":
        return ["🖳🖳","♖♖","░░","░░","🗠🗠"]
    elif ascii == "6":
        return ["🕱🕱","⛓⛓","🕈🕈","▒▒","░░"]
    elif ascii == "7":
        return ["亹","乨","乃","个","丷"]
    else:
        custom = ascii.split(",")
        custom_final = []
        for custom_char in custom:
            custom_final.append(custom_char[0]*2)
        return custom_final






