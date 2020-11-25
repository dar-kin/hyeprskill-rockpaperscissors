# read test_file.txt
file = open("test_file.txt", "r", encoding="utf-16")
for line in file:
    print(line)
    break
file.close()
