#!/usr/bin/python3
def roman_to_int(roman_string):
    num_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    if not roman_string or type(roman_string) != str or \
            len(roman_string) == 0:
        return 0
    res = 0
    roman_string = roman_string.upper()
    list_ = []
    for elem in roman_string:
        list_.append(elem)

    prev = None
    for elem in list_:
        if elem == "V":
            if prev == "I":
                res -= num_dict[prev]
                res += 4
            else:
                res += num_dict[elem]
        elif elem == "X":
            if prev == "I":
                res -= num_dict[prev]
                res += 9
            else:
                res += num_dict[elem]
        elif elem == "C":
            if prev == "X":
                res -= num_dict[prev]
                res += 90
            else:
                res += num_dict[elem]
        elif elem == "D":
            if prev == "C":
                res -= num_dict[prev]
                res += 400
            else:
                res += num_dict[elem]
        elif elem == "M":
            if prev == "C":
                res -= num_dict[prev]
                res += 900
            else:
                res += num_dict[elem]
        else:
            res += num_dict[elem]
        prev = elem
    return res


if __name__ == "__main__":
    roman_to_int = __import__('12-roman_to_int').roman_to_int

    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "CM"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "XCIX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
