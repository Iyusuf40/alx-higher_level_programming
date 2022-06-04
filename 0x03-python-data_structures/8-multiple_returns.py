#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    if lent != 0:
        first_char = sentence[0]
    else:
        first_char = None

    return lent, first_char


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
