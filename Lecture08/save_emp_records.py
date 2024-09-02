# get the number of employee records to be create.
num_emps = int(input("How many employee records do you want to create? "))
with open("Lecture08/employees.txt", "w") as emp_file:
    for count in range(1, num_emps + 1):
        print(f"Enter deta for employee #", count, sep="")
        name = input("Name: ")
        id_num = input("ID number: ")
        dept = input("Department: ")
        emp_file.write(name + "\n")
        emp_file.write(id_num + "\n")
        emp_file.write(dept + "\n")
        print()

print("Employee records written to employees.txt.")