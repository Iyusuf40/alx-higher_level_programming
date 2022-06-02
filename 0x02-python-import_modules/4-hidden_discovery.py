#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_ = dir(hidden_4)
    for _ in list_:
        if _[0] != "_":
            print("{}".format(_))
