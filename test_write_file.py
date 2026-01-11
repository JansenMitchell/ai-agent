from functions.write_file import write_file

def main():
    lorem = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(lorem)

    more_lorem = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(more_lorem)

    temp = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(temp)

if __name__ == "__main__":
    main()
