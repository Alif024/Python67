import struct


def changeName(listData:list,index: int, newName: str):
    listData[index]['name'] = newName


def editData(path: str):
    listData = []
    with open(path, "rb") as file:
        while True:
            data = file.read(struct.calcsize("20si20s"))
            if not data:
                break
            record = struct.unpack("20si20s", data)
            record = {"name": record[0].decode().strip(
                '\x00'), "age": record[1], "city": record[2].decode().strip('\x00')}
            listData.append(record)

    name = input("Enter name to edit: ")
    for index, data in enumerate(listData):
        if data['name'] == name:
            print("Old record:", data)
            newName = input("Enter new name: ")
            changeName(listData, index, newName)
            break
    print(listData)


if __name__ == "__main__":
    editData("HomeWork\\TeamProject\\data.bin")
