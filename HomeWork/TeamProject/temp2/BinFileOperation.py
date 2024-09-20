import struct
import numpy as np
import pandas as pd


def readDataFromBinFile() -> list:
    with open("HomeWork\\TeamProject\\temp2\\data.bin", "rb") as file:
        record_size = struct.calcsize("20s20s20s20sf")
        list_records = []
        while True:
            data = file.read(record_size)
            if not data:
                break
            records = struct.unpack("20s20s20s20sf", data)
            records = [records[0].decode().strip('\x00'), records[1].decode().strip(
                '\x00'), records[2].decode().strip('\x00'), [float(score) for score in records[3].decode().strip('\x00').split()], records[4]]
            list_records.append(records)
    return list_records


def writeDataToBinFile(list_records: list):
    with open("HomeWork\\TeamProject\\temp2\\data.bin", "wb") as file:
        for record in list_records:
            data = struct.pack("20s20s20s20sf", record[0].encode(), record[1].encode(
            ), record[2].encode(), ' '.join(map(str, record[3])).encode(), record[4])
            file.write(data)


def editData(pointed_col: int, id: tuple, new_data: tuple, choice_edit=None, selected_col=None):
    list_records = readDataFromBinFile()
    pointed_col = ['Name', 'Department',
                   'Score', 'Salary'][int(pointed_col) - 1]
    match pointed_col:
        case 'Name':
            for i in range(len(id)):
                for index, record in enumerate(list_records):
                    if record[0] == id[i]:
                        list_records[index][1] = new_data[i]
        case 'Department':
            for i in range(len(id)):
                for index, record in enumerate(list_records):
                    if record[0] == id[i]:
                        list_records[index][2] = new_data[i]
        case 'Score':
            match choice_edit:
                case '1':   # Add
                    for i in range(len(id)):
                        for index, record in enumerate(list_records):
                            if record[0] == id[i]:
                                for score in new_data[i]:
                                    list_records[index][3].append(score)
                                    if len(list_records[index][3]) > 4:
                                        list_records[index][3].pop(0)
                case '2':   # selective update
                    for i in range(len(id)):
                        for index, record in enumerate(list_records):
                            if record[0] == id[i]:
                                # print(record, index)
                                # print(record[3])
                                # print(record[3][int(selected_col[i]) - 1])
                                for index_select_col, col in enumerate(selected_col):
                                    # print(record[3][int(col) - 1])
                                    # print(list_records[index][3][int(col) - 1], new_data[i][index_select_col])
                                    list_records[index][3][int(
                                        col) - 1] = new_data[i][index_select_col]
                                    # print(new_data[i])
                                # print(record[3], "\n")
        case 'Salary':
            match choice_edit:
                case '1':
                    for i in range(len(id)):
                        for index, record in enumerate(list_records):
                            if record[0] == id[i]:
                                list_records[index][4] += new_data[i]
                case '2':
                    for i in range(len(id)):
                        for index, record in enumerate(list_records):
                            if record[0] == id[i]:
                                list_records[index][4] -= new_data[i]
                case '3':
                    for i in range(len(id)):
                        for index, record in enumerate(list_records):
                            if record[0] == id[i]:
                                list_records[index][4] = new_data[i]
                case _:
                    print("Invalid choice. Please try again.")
                    return
        case _:
            print("Invalid choice. Please try again.")
            return
    writeDataToBinFile(list_records)


def showAllData(choice=None):
    list_records = readDataFromBinFile()
    choice = choice
    match choice:
        case '1':
            list_records = [(record[0], record[1], record[2], np.mean(
                record[3]), record[4]) for record in list_records]
            # Define the data types for each field
            dtype = [('ID', 'U20'),             # 4-character string for ID
                    ('Name', 'U20'),           # 10-character string for Name
                    ('Department', 'U20'),     # 10-character string for Department
                    ('Average Score', 'f4'),   # float for Score
                    ('Salary', 'f4')]          # float for Salary
            # Create a structured NumPy array
            data_arr = np.asarray(list_records, dtype=dtype)
        case '2':
            list_records = [(record[0], record[1], record[2], ','.join(list(map(str, record[3]))), record[4]) for record in list_records]
            # Define the data types for each field
            dtype = [('ID', 'U20'),             # 4-character string for ID
                    ('Name', 'U20'),           # 10-character string for Name
                    ('Department', 'U20'),     # 10-character string for Department
                    ('Score', 'U20'),   
                    ('Salary', 'f4')]          # float for Salary
            # Create a structured NumPy array
            data_arr = np.asarray(list_records, dtype=dtype)
        case _:
            print("Invalid choice. Please try again.")
            return
    # Sort by the 'ID' field
    sorted_data = np.sort(data_arr, order='ID')
    # Convert to Pandas DataFrame for display
    df_data_arr = pd.DataFrame(sorted_data)
    # Display the data without the index column
    if df_data_arr.empty:
        print("No data found.")
        return
    print(df_data_arr.to_string(index=False))


def showSpecificData(col: int, list_search=None, choice=None):
    list_records = readDataFromBinFile()
    col = ['ID', 'Name', 'Department', 'Average Score',
           'Score', 'Salary'][int(col) - 1]
    if col == 'Score':
        list_records = [(record[0], record[1], record[2], ','.join(list(map(str, record[3]))), record[4]) for record in list_records]
        # Define the data types for each field
        dtype = [('ID', 'U20'),             # 4-character string for ID
                ('Name', 'U20'),           # 10-character string for Name
                ('Department', 'U20'),     # 10-character string for Department
                ('Score', 'U20'),   
                ('Salary', 'f4')]          # float for Salary
        # Create a structured NumPy array
        data_arr = np.asarray(list_records, dtype=dtype)
    else:
        list_records = [(record[0], record[1], record[2], np.mean(
            record[3]), record[4]) for record in list_records]
        # Define the data types for each field
        dtype = [('ID', 'U20'),             # 4-character string for ID
                ('Name', 'U20'),           # 10-character string for Name
                ('Department', 'U20'),     # 10-character string for Department
                ('Average Score', 'f4'),   # float for Score
                ('Salary', 'f4')]          # float for Salary
        # Create a structured NumPy array
        data_arr = np.asarray(list_records, dtype=dtype)
    if col == 'Average Score' or col == 'Salary':
        choice = choice
        match choice:
            case '1':
                data_fltr = data_arr[data_arr[col] > float(list_search[0])]
            case '2':
                data_fltr = data_arr[data_arr[col] >= float(list_search[0])]
            case '3':
                data_fltr = data_arr[data_arr[col] < float(list_search[0])]
            case '4':
                data_fltr = data_arr[data_arr[col] <= float(list_search[0])]
            case _:
                list_search = [float(score) for score in list_search]
                data_fltr = data_arr[np.isin(data_arr[col], list_search)]
        sorted_data = np.sort(data_fltr, order=col)
    elif col == 'ID' or col == 'Name':
        data_fltr = data_arr[np.isin(data_arr[col], list_search)]
        sorted_data = np.sort(data_fltr, order='ID')
    elif col == 'Department':
        data_fltr = data_arr[np.isin(data_arr[col], list_search)]
        sorted_data = np.sort(data_fltr, order='Department')
    elif col == 'Score':
        data_fltr = data_arr[np.isin(data_arr['ID'], list_search)]
        sorted_data = np.sort(data_fltr, order='ID')
    # Convert to Pandas DataFrame for display
    # print(sorted_data)
    df_data_fltr = pd.DataFrame(data=sorted_data)
    if df_data_fltr.empty:
        print("No data found.")
        return
    print(df_data_fltr.to_string(index=False))


def exportReport():
    data_bin_file = np.array(readDataFromBinFile(), dtype="object")
    # จัดกลุ่มตามแผนก
    departments = {}
    for record in data_bin_file:
        emp_id, name, dept, scores, salary = record
        avg_score = sum(scores) / len(scores)
        if dept not in departments:
            departments[dept] = {
                'employees': [], 'total_score': 0.0, 'count': 0, 'top_performer': (None, 0)}

        departments[dept]['employees'].append((name, avg_score))
        departments[dept]['total_score'] += avg_score
        departments[dept]['count'] += 1

        # อัปเดตผู้ทำคะแนนสูงสุด
        if avg_score > departments[dept]['top_performer'][1]:
            departments[dept]['top_performer'] = (name, avg_score)

    # คำนวณและพิมพ์รายงาน
    best_department = (None, 0)
    str_report = ""
    str_report += "Summary Report:\n"

    for dept, info in departments.items():
        avg_dept_score = info['total_score'] / info['count']
        str_report += f"Department: {dept}\n"

        for name, avg_score in info['employees']:
            str_report += f"  {name}: Average Score = {avg_score:.2f}\n"

        top_performer, top_score = info['top_performer']
        str_report += f"Top Performer: {
            top_performer} Average score = {top_score:.2f}\n"

        # หาว่าแผนกไหนมีคะแนนเฉลี่ยสูงสุด
        if avg_dept_score > best_department[1]:
            best_department = (dept, avg_dept_score)

    str_report += f"\nBest Department: {
        best_department[0]} Average score = {best_department[1]:.2f}\n"

    with open("report.txt", "w") as file:
        file.write(str_report)
    print("Report exported to report.txt successfully.")


def main():
    # showSpecificData(1, ['0001', '0002', '0003'])
    # editData(1, ['0001', '0002', '0003'], ['Silfy', 'Vyne', 'Buck'])
    # editData(3, ['0001', '0002', '0003'], [[50, 90, 80], [
    #          45, 90, 80], [40, 90, 80]], '2', ['1', '3', '2'])
    # editData(4, ['0001', '0002', '0003'], [10000, 20000, 30000], '3')
    # showSpecificData(1, ['0001', '0002', '0003'])
    pass

main()
