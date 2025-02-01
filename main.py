def main():
    word_count = 0
    character_count = {}
    char_list = []

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
    
    for key, value in character_count.items():
        if key.isalpha():
            char_list.append({"character": key, "count": value})

    def sort_on(item):
        return item["count"]

    char_list.sort(reverse=True, key=sort_on)        

    print (f"--- Begin report of books/frankenstein.txt ---")
    print (f"This document has {word_count} words.")
    
    for item in char_list:
        char = item["character"]
        count = item["count"]
        print (f"The '{char}' character was found {count} times.")

    print("--- End report ---")
    
if __name__ == "__main__":
    main()