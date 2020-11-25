# write your code here
with open("salary.txt", "r") as f_in, open("salary_year.txt", "w") as f_out:
    f_out.writelines(str(int(x) * 12) + "\n" for x in f_in.readlines())
