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