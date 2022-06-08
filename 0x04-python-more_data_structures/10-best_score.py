#!/usr/bin/python3
def best_score(a_dictionary):
    list_ = []
    if a_dictionary:
        for item in a_dictionary.items():
            list_.append(item[1])
        list_ = sorted(list_, reverse=True)
        max_val = list_[0]
        for key, val in a_dictionary.items():
            if val == max_val:
                return key


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
