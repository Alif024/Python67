import struct

def addData(pathFile: str):
    while True:
        num_records = input("How many records do you want to create? ")
        try:
            num_records = int(num_records)
        except ValueError:
            if num_records == "q":
                return
            print("Number of records must be a number!")
        else:
            break

    with open(pathFile, "ab") as file:
        for num_p in range(num_records):
            num_p += 1
            name = input(f"Enter name person {num_p}: ")
            if name == "q":
                return
            while True:
                age = input(f"Enter age person {num_p}: ")
                try:
                    age = int(age)
                except ValueError:
                    if age == "q":
                        return
                    print("Age must be a number!")
                else:
                    break
            city = input(f"Enter city person {num_p}: ")
            if city == "q":
                return

            record = struct.pack("20si20s", name.encode(), age, city.encode())
            file.write(record)
            print()
    print(f"{num_records} records have been written to records.bin")

if __name__ == "__main__":
    addData("HomeWork\\TeamProject\\testAddData.bin")