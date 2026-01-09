from functions.get_file_content import get_file_content


def main():
    lorem = get_file_content("calculator", "lorem.txt")
    print(lorem)

    calc_main = get_file_content("calculator", "main.py")
    print(calc_main)

    calc_code = get_file_content("calculator", "pkg/calculator.py")
    print(calc_code)

    outside = get_file_content("calculator", "/bin/cat")
    print(outside)

    missing = get_file_content("calculator", "pkg/does_not_exist.py")
    print(missing)


if __name__ == "__main__":
    main()
