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
            records = (records[0].decode().strip('\x00'), records[1].decode().strip(
                '\x00'), records[2].decode().strip('\x00'), [float(score) for score in records[3].decode().strip('\x00').split()], records[4])
            list_records.append(records)
    return list_records


def showAllData():
    list_records = readDataFromBinFile()
    list_records = [(record[0], record[1], record[2], np.mean(record[3]), record[4]) for record in list_records]
    # Define the data types for each field
    dtype = [('ID', 'U20'),             # 4-character string for ID
             ('Name', 'U20'),           # 10-character string for Name
             ('Department', 'U20'),     # 10-character string for Department
             ('Average Score', 'f4'),   # float for Score
             ('Salary', 'f4')]          # float for Salary
    # Create a structured NumPy array
    data_arr = np.asarray(list_records, dtype=dtype)
    # Sort by the 'ID' field
    sorted_data = np.sort(data_arr, order='ID')
    # Convert to Pandas DataFrame for display
    df_data_arr = pd.DataFrame(sorted_data)
    # Display the data without the index column
    if df_data_arr.empty:
        print("No data found.")
        return
    print(df_data_arr.to_string(index=False))


def showSpecificData(col: int, list_search: list, choice=None):
    list_records = readDataFromBinFile()
    list_records = [(record[0], record[1], record[2], np.mean(record[3]), record[4]) for record in list_records]
    # Define the data types for each field
    dtype = [('ID', 'U20'),             # 4-character string for ID
             ('Name', 'U20'),           # 10-character string for Name
             ('Department', 'U20'),     # 10-character string for Department
             ('Average Score', 'f4'),   # float for Score
             ('Salary', 'f4')]          # float for Salary
    # Create a structured NumPy array
    data_arr = np.asarray(list_records, dtype=dtype)
    col = ['ID', 'Name', 'Department', 'Average Score', 'Salary'][int(col) - 1]
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
    # Convert to Pandas DataFrame for display
    # print(sorted_data)
    df_data_fltr = pd.DataFrame(data=sorted_data)
    if df_data_fltr.empty:
        print("No data found.")
        return
    print(df_data_fltr.to_string(index=False))

def exportReport():
    data_bin_file  = np.array(readDataFromBinFile(), dtype="object")
    # จัดกลุ่มตามแผนก
    departments = {}
    for record in data_bin_file:
        emp_id, name, dept, scores, salary = record
        avg_score = sum(scores) / len(scores)
        if dept not in departments:
            departments[dept] = {'employees': [], 'total_score': 0.0, 'count': 0, 'top_performer': (None, 0)}
        
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
        str_report += f"Top Performer: {top_performer} Average score = {top_score:.2f}\n"
        
        # หาว่าแผนกไหนมีคะแนนเฉลี่ยสูงสุด
        if avg_dept_score > best_department[1]:
            best_department = (dept, avg_dept_score)

    str_report += f"\nBest Department: {best_department[0]} Average score = {best_department[1]:.2f}\n"

    with open("report.txt", "w") as file:
        file.write(str_report)
    print("Report exported to report.txt successfully.")