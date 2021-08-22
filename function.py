# Flatten function

clean_list = []
a = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]


def list_cleaner(l):
    x = [clean_list.append(i) if type(i) != list else list_cleaner(i) for i in l]
    return clean_list


print(list_cleaner(a))

#####################

# Reverse function


b = [[1, 2], [3, 4], [5, 6, 7]]


def list_reverser(k):
    reversed_list = []
    x = [reversed_list.append(list_reverser(i)) if type(i) == list else reversed_list.append(i) for i in k]
    reversed_list.reverse()
    return reversed_list


print(list_reverser(b))
