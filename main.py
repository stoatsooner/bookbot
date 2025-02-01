def main():
    word_count = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            word_count += 1


        print (word_count)

if __name__ == "__main__":
    main()