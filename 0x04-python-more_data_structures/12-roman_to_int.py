#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
    roman_keys = list(roman_dict.keys())
    roman_string = roman_string[::-1]
    value = roman_dict[roman_string[0]]
    for i in range(1, len(roman_string)):
        r = roman_string[i]
        s = roman_string[i - 1]
        if r in roman_keys and s in roman_keys:
            if roman_dict[r] >= roman_dict[s]:
                value += roman_dict[r]
            else:
                value -= roman_dict[r]
    return value
