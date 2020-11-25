file_from = open("animals.txt", "r")
file_to = open("animals_new.txt", "w")
file_to.writelines(x.replace("\n", " ") for x in file_from.readlines())

file_from.close()
file_to.close()
