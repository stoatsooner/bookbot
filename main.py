def main():
    word_count = 0
    character_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            word_count += 1
        lowered_case_book = file_contents.lower()
        for character in lowered_case_book:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1



        print (f"This book has {word_count} words. Here's a counter for every character: {character_count}")

if __name__ == "__main__":
    main()