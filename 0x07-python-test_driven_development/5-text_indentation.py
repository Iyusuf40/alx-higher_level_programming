#!/usr/bin/python3
"""
function text_indentation: inserts 2 newline characters
after any of ., : or ?
"""


def text_indentation(text):
    """
    inserts 2 newline characters after any of ., : or ?
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    double_nl = "\n\n"

    max_index = len(text) - 1
    char = 0
    while char <= max_index:
        if text[char] == "." or text[char] == "?" or text[char] == ":":
            new_str += text[char]
            new_str += double_nl
            if char != max_index:
                char += 1
            else:
                break
            while text[char] == " " and char != max_index:
                char += 1
        else:
            new_str += text[char]
            char += 1

    print(new_str, end="")


if __name__ == "__main__":
    text_indentation("first line. second line? third line:")
