import BinFileOperation as bfo

while True:
    print("1. Show all data")
    print("2. Show specific data")
    print("3. Export report")
    print("4. Exit")
    print("Ctrl+C to cancel or go to the main menu")
    try:
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                bfo.showAllData()
            case '2':
                print("1. ID")
                print("2. Name")
                print("3. Department")
                print("4. Average Score")
                print("5. Salary")
                print("Ctrl+C to cancel or go to the main menu")
                col = input("Enter the column to search: ")
                column_choice = ['ID', 'Name', 'Department', 'Average Score', 'Salary'][int(col) - 1]
                if col == '1':
                    print("Input a single value or multiple values to search. example =>`0001` or `0001 0002 0003`")
                elif col == '2':
                    print("Input a single value or multiple values to search. example =>`John` or `John Peter`")
                elif col == '3':
                    print("Input a single value or multiple values to search. example =>`HR` or `HR IT`")
                if col in ['4', '5']:
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
                            print("Input a single value or multiple values to search. example =>`80` or `80 90 100`")
                        case _:
                            print("Input a single value to search. example =>`80`")
                    list_search = input(f"Enter the values for {column_choice} to search values that are {compare_choice}: ").strip().split()
                    bfo.showSpecificData(col, list_search, choice)
                elif col in ['1', '2', '3']:
                    list_search = input(f"Enter the values for {column_choice} to search: ").strip().split()
                    bfo.showSpecificData(col, list_search)
                else:
                    print("Invalid choice. Please try again.")
            case '3':
                bfo.exportReport()
            case '4':
                if input("Do you want to exit? (y/n): ").lower() == 'y':
                    break
            case _:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("Operation cancelled.")
    else:
        input("Press Enter to continue...")