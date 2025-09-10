def get_book_text(filepath):
    with open(filepath) as file:
        file_text = file.read()
        return file_text

#text = get_book_text(filepath)

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

#word_count(text)

def character_count(text):
    lower_characters = text.lower()
    character_dictionary = {}
    for char in lower_characters:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary

#print(character_count(text))

# make a separate dictionary for each letter and then append them into a list of dictionaries
#

#char_dict = character_count(text)
#print(char_dict)


# Helper function from Ch3 L1
def sort_on(items):
    return items["num"]

# function to make a list of dictionaries sorted by value
def sorted_stat_list(char_dict):
    stat_list = []
    for entry in char_dict:
        if entry.isalpha():
            stat_list.append({"char": entry, "num": char_dict[entry]})
    stat_list.sort(reverse=True, key=sort_on)
    return stat_list

#print(sorted_stat_list(char_dict))
