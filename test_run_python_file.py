from functions.run_python_file import run_python_file


def main():
    basic_run = run_python_file("calculator", "main.py")
    print(basic_run)

    with_args = run_python_file("calculator", "main.py", ["3 + 5"])
    print(with_args)

    tests = run_python_file("calculator", "tests.py")
    print(tests)

    outside = run_python_file("calculator", "../main.py")
    print(outside)

    missing = run_python_file("calculator", "nonexistent.py")
    print(missing)

    not_python = run_python_file("calculator", "lorem.txt")
    print(not_python)


if __name__ == "__main__":
    main()
