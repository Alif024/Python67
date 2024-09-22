import BinFileOperation as bfo
from os import system
from numpy import asarray, isin, sort
from pandas import DataFrame

while True:
    print("1. Show all data")
    print("2. Show specific data")
    print("3. insert data")
    print("4. Edit data")
    print("5. Delete data")
    print("6. Export report")
    print("7. Exit")
    print("Ctrl+C to cancel or go to the main menu")
    try:
        choice = input("Enter your choice: ")
        match choice:
            case '1':   # Show all data
                print("1. Show average score")
                print("2. Show score distribution")
                choice = input("Enter your choice: ")
                bfo.showAllData(choice)
            case '2':   # Show specific data
                print("1. ID")
                print("2. Name")
                print("3. Department")
                print("4. Average Score")
                print("5. Score")
                print("6. Salary")
                print("Ctrl+C to cancel or go to the main menu")
                col = input("Enter the column to search: ")
                column_choice = ['ID', 'Name', 'Department', 'Average Score', 'Score', 'Salary'][int(col) - 1]
                if col == '1' or col == '5':
                    print("Input a single ID or multiple ID to search. example =>`0001` or `0001 0002 0003`")
                elif col == '2':
                    print("Input a single name or multiple name to search. example =>`John` or `John Peter`")
                elif col == '3':
                    print("Input a single Department or multiple Department to search. example =>`HR` or `HR IT`")
                if col in ['4', '6']:
                    print("1. More than")
                    print("2. More than or equal to")
                    print("3. Less than")
                    print("4. Less than or equal to")
                    print("5. Equal to (default)")
                    print("Ctrl+C to cancel or go to the main menu")
                    choice = input(f"Input your choice for {column_choice}: ")
                    compare_choice = ['More than', 'More than or equal to', 'Less than', 'Less than or equal to', 'Equal to'][int(choice) - 1]
                    match choice:
                        case '5':
                            print(f"Input a single {column_choice} or multiple {column_choice} to search. example =>`80` or `80 90 100`")
                        case _:
                            print(f"Input a single {column_choice} to search. example =>`80`")
                    list_search = input(f"Enter the values for {column_choice} to search values that are {compare_choice}: ").strip().split()
                    bfo.showSpecificData(col, list_search, choice)
                elif col == '5':
                    list_search = input(f"Enter the ID for {column_choice} to search: ").strip().split()
                    bfo.showSpecificData(col, list_search)
                elif col in ['1', '2', '3']:
                    list_search = input(f"Enter the values for {column_choice} to search: ").strip().split()
                    bfo.showSpecificData(col, list_search)
                else:
                    print("Invalid choice. Please try again.")
            case '3':   # Insert data
                pass
            case '4':   # Edit data
                print("1. Name")
                print("2. Department")
                print("3. Score")
                print("4. Salary")
                print("Ctrl+C to cancel or go to the main menu")
                col = input("Enter the column to edit by ID: ")
                column_choice = ['Name', 'Department', 'Score', 'Salary'][int(col) - 1]
                multi_id = input("Enter a single ID or multiple ID to edit. example =>`0001` or `0001 0002 0003`: ")
                multi_id = tuple(multi_id.strip().split())
                match column_choice:
                    case 'Name':
                        print(f"Input new name for {multi_id} to edit. example =>`John` or `John Peter`")
                        new_name = input("Enter the new name: ")
                        new_name = tuple(new_name.strip().split())
                        bfo.editData(column_choice,multi_id,new_name)
                    case 'Department':
                        print(f"Input department for {multi_id} to edit. example =>`HR` or `HR IT`")
                        new_department = input("Enter the new department: ")
                        new_department = tuple(new_department.strip().split())
                        bfo.editData(column_choice,multi_id,new_department)
                    case 'Score':
                        choice_edit_score = input("1. Add new score\n2. Edit existing score\nEnter your choice: ")
                        all_user_data = bfo.readDataFromBinFile()
                        all_user_data = [(user_data[0],user_data[1] , f"[{', '.join(list(map(str, user_data[3])))}]") for user_data in all_user_data]
                        dtype = [('ID', 'U20'),             # 4-character string for ID
                                ('Name', 'U20'),           # 10-character string for Name
                                ('Score', 'U30')]
                        all_user_data_fltr = asarray(all_user_data, dtype=dtype)
                        data_fltr = all_user_data_fltr[isin(all_user_data_fltr['ID'], multi_id)]
                        sorted_data = sort(data_fltr, order='ID')
                        df_data_fltr = DataFrame(data=sorted_data)
                        print(df_data_fltr.to_string(index=False))
                        multi_new_score = []
                        match choice_edit_score:
                            case '1':
                                for id in multi_id:
                                    new_score = input(f"Enter the new score (max 4 value) for {id}. Example=> `80 90 100 95`\n:")
                                    new_score = tuple(new_score.strip().split())
                                    multi_new_score.append(new_score)
                                bfo.editData(column_choice,multi_id,multi_new_score,choice_edit_score)
                            case '2':
                                multi_index = []
                                all_user_data = bfo.readDataFromBinFile()
                                all_user_id = [user_data[0] for user_data in all_user_data]
                                for id in multi_id:
                                    if id not in all_user_id:
                                        print(f"ID {id} not found can't edit score for {id}.")
                                        continue
                                    index = input(f"Enter the index of score to edit for {id}. Example=> `0 1 2 3`:")
                                    index = tuple(index.strip().split())
                                    if len(index) == 0:
                                        print(f"Index not found can't edit score for {id}.")
                                        continue
                                    multi_index.append(index)
                                    new_score = input(f"Enter the new score according to position of index {index} for {id}.\n:")
                                    new_score = tuple(new_score.strip().split())
                                    if len(new_score) == 0:
                                        print(f"Score not found can't edit score for {id}.")
                                        continue
                                    elif len(new_score) != len(index):
                                        print(f"Score and index length not same can't edit score for {id}.")
                                        continue
                                    multi_new_score.append(new_score)
                                bfo.editData(column_choice,multi_id,multi_new_score,choice_edit_score, multi_index)
                            case _:
                                print("Invalid choice. Please try again.")
                    case 'Salary':
                        choice_edit_salary = input("1. Add new salary\n2. Cut salary\n3. Edit existing salary\nEnter your choice: ")
                        match choice_edit_salary:
                            case '1':
                                print(f"Input new salary for ID ['{", ".join(multi_id)}'] to add.")
                                try:
                                    new_salary = float(input("Enter 1 number only for add salary: "))
                                except ValueError:
                                    print("Input 1 number only.")
                                else:
                                    bfo.editData(column_choice,multi_id, new_salary, choice_edit_salary)
                            case '2':
                                print(f"Input new salary for ID ['{", ".join(multi_id)}'] to cut.")
                                try:
                                    new_salary = float(input("Enter 1 number only for cut salary: "))
                                except ValueError:
                                    print("Input 1 number only.")
                                else:
                                    bfo.editData(column_choice,multi_id, new_salary, choice_edit_salary)
                            case '3':
                                print(f"Input new salary for {multi_id} to edit.")
                                new_salary = input("Enter the new salary according to ID:")
                                new_salary = tuple(map(float, new_salary.strip().split()))
                                if len(new_salary) == 0:
                                    print(f"Salary not found can't edit salary for {multi_id}.")
                                elif len(new_salary) != len(multi_id):
                                    print(f"Salary and ID length not same can't edit salary for {multi_id}.")
                                else:
                                    bfo.editData(column_choice,multi_id, new_salary, choice_edit_salary)
                            case _:
                                raise Exception("Invalid choice. Please try again.")
                    case _:
                        print("Invalid choice. Please try again.")
            case '5':   # Delete data
                pass
            case '6':   # Export report
                bfo.exportReport()
            case '7':   # Exit
                if input("Do you want to exit? (y/n): ").lower() == 'y':
                    break
            case _:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to continue...")
    except KeyboardInterrupt:
        print("Operation cancelled.")
    else:
        input("Press Enter to continue...")
    finally:
        system('cls')