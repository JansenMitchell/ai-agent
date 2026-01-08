from functions.get_files_info import get_files_info

result = get_files_info("calculator", ".")
print("Result for current directory:")
print(f"  {result}")

result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(f"  {result}")

result = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(f"  {result}")

result = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(f"  {result}")
