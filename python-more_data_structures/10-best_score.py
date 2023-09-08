#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = 0
    highest = ""
    for key in a_dictionary:
        if a_dictionary[key] > max_score:
            highest = key
            max_score = a_dictionary[key]
    if max_score == 0:
        return None
    return highest


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
