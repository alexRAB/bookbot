def get_num_words(text):
    number_of_words = len(text.split())
    return number_of_words

def get_num_chars(text):
    list_of_words = text.lower().split()
    dict_of_chars = {}
    for word in list_of_words:
        for char in word:
            if char in dict_of_chars:
                dict_of_chars[char] += 1
            else:
                dict_of_chars[char] = 1
    return dict_of_chars

def sorted_dict(dict_of_chars):
    sorted_dict = dict(sorted(dict_of_chars.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict