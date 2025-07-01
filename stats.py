def num_of_words(string):
    return len(string.split())

def num_of_characters(string):

    dict = {}

    for i in string:
        i = i.lower()

        if i in dict.keys():
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1

    return dict

def sort_on(item):
    return item["num"]

def sorted_list(input_dict):
    sort_list = []

    for key, value in input_dict.items():
        sort_list.append({"char": key, "num": value})

    sort_list.sort(reverse=True, key=sort_on)
    return sort_list