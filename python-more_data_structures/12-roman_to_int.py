#!/usr/bin/python3

def roman_to_int(roman_string):
    rom_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    len_str = len(roman_string)
    if roman_string == None or len_str < 1:
        return None
    sum = 0
    i = 0
    while(i < len_str):
        if i < (len_str - 1) and rom_dict[roman_string[i]] < rom_dict[roman_string[i + 1]]:
            sum += (rom_dict[roman_string[i + 1]] - rom_dict[roman_string[i]])
            i += 2
        else:
            sum += rom_dict[roman_string[i]]
            i += 1
    return sum
