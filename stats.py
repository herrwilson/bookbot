def word_counter(content):
    word_list = content.split()
    num_words = 0

    for i in word_list:
        num_words += 1
    
    return num_words

def character_counter(content):
    unduped = content.lower()
    char_dict = {}

    for i in unduped:
        if i in char_dict:
            char_dict[i] = char_dict[i] + 1
        else:
            char_dict[i] = 1              
    return char_dict

def dictionary_sorter(x):
    temporary_storage = sorted(x.items(), key=lambda asd: asd[1], reverse=True)
    return dict(temporary_storage)