fullname = input()

splited_name = fullname.split(' ')


for part_of_name in splited_name:
    if len(part_of_name) > 4 and splited_name.index(part_of_name) != 0 and splited_name.index(part_of_name) != len(splited_name) - 1:
        splited_name[splited_name.index(part_of_name)] = part_of_name[0] + "."


print(" ".join(splited_name))