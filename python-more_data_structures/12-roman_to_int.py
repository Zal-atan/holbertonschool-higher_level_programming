#!/usr/bin/python3

def roman_to_int(roman_string):
    rom_dict = {"M": 1000, "D": 500, "C": 100,
                "L": 50, "X": 10, "V": 5, "I": 1}
    if roman_string is None or type(roman_string) != str:
        return int(0)
    len_str = len(roman_string)
    sum = 0
    i = 0
    while(i < len_str):
        if i < (len_str - 1) and (rom_dict[roman_string[i]] <
                                  rom_dict[roman_string[i + 1]]):
            if (roman_string[i] == "I") and (roman_string[i + 1] == "V" or
                                             roman_string[i + 1] == "X"):
                sum += (rom_dict[roman_string[i + 1]] -
                        rom_dict[roman_string[i]])
                i += 2
            elif (roman_string[i] == "X") and (roman_string[i + 1] == "L" or
                                               roman_string[i + 1] == "C"):
                sum += (rom_dict[roman_string[i + 1]] -
                        rom_dict[roman_string[i]])
                i += 2
            elif (roman_string[i] == "C") and (roman_string[i + 1] == "" or
                                               roman_string[i + 1] == "M"):
                sum += (rom_dict[roman_string[i + 1]] -
                        rom_dict[roman_string[i]])
                i += 2
            else:
                return 0
        else:
            sum += rom_dict[roman_string[i]]
            i += 1
    return sum
