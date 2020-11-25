# write your code here
for i in range(10):
    with open(f"file{i + 1}.txt", "w") as f:
        f.write(str(i + 1))
