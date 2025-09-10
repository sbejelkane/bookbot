import sys
#print(sys.argv)
#sys.exit(0)

from stats import get_book_text
from stats import word_count
from stats import character_count
#from stats import sort_on
from stats import sorted_stat_list


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        number_of_words = word_count(text)
        characters_counted = character_count(text)
        final_stat_list = sorted_stat_list(characters_counted)

        print("============BOOKBOT============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count -----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count ---------")


        for item in final_stat_list:
            if not item["char"].isalpha():
                continue
            print(f"{item['char']}: {item['num']}")

        print("============= END =============")

'''
final_stat_list = sorted_stat_list(characters_counted)
#print(final_stat_list)
for i in range(0, len(final_stat_list)):
    print(final_stat_list[i]["char"] + ": " + str(final_stat_list[i]["num"]))
'''

main()
