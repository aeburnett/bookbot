def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    words = text.split()
    for word in words:
        for w in word:
            w = w.lower()
            if (w not in character_count ):
                character_count[w] = 1
            else: character_count[w] += 1
    return character_count


def sort_on(dict):
    return dict["num"]

def get_sorted_dict(dict):
    sorted_list = []
    for k in dict:
        sorted_list.append({"char": k, "num": dict[k]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list