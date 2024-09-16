import struct
import pandas as pd

def showAllData(pathFile: str):
    result = []
    with open(pathFile, "rb") as file:
        count = 0
        index = 1
        while True:
            if count > 9:
                df = pd.DataFrame(result)
                df.index = list(range(index, index+count))
                print(df)
                if input("Press Enter to continue, or input 'q' to exit...\n") == "q":
                    break
                result = []
                index += count
                count = 0
            
            data = file.read(struct.calcsize("20si20s"))
            if not data:
                df = pd.DataFrame(result)
                df.index = list(range(index, index+count))
                print(df)
                break
            record = struct.unpack("20si20s", data)
            record = (record[0].decode().strip('\x00'), record[1], record[2].decode().strip('\x00'))
            result.append({"name": record[0], "age": record[1], "city": record[2]})

            count += 1

if __name__ == "__main__":
    showAllData("HomeWork\\TeamProject\\data.bin")