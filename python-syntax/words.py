def print_upper_words(list_of_words, must_start_with):
    "Prints each word on a new line in all CAPS given a list of words"

    for word in list_of_words:
        for letter in must_start_with:
            if letter.upper() == word[0].upper():
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})