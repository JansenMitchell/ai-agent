from functions.get_files_info import get_files_info


def main():
    current_dir = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(current_dir)

    pkg_dir = get_files_info("calculator", "pkg")
    print("\nResult for 'pkg' directory:")
    print(pkg_dir)

    outside = get_files_info("calculator", "/bin")
    print("\nResult for '/bin' directory:")
    print(outside)

    parent = get_files_info("calculator", "../")
    print("\nResult for '../' directory:")
    print(parent)


if __name__ == "__main__":
    main()
