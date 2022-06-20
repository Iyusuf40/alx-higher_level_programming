#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
            res = my_list_1[index] / my_list_2[index]
            new_list.append(res)
        except ZeroDivisionError:
            res = 0
            new_list.append(res)
            print("division by 0")
        except IndexError:
            res = 0
            new_list.append(res)
            print("out of range")
        except TypeError:
            res = 0
            new_list.append(res)
            print("wrong type")
        finally:
            pass

    return new_list


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
