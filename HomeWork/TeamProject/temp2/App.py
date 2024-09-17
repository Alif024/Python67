import BinFileOperation as bfo

while True:
    print("1. Show all data")
    print("2. Show specific data")
    print("3. Export report")
    print("4. Exit")
    choice = input("Enter your choice: ")
    try:
        match choice:
            case '1':
                bfo.showAllData()
            case '2':
                print("1. ID")
                print("2. Name")
                print("3. Department")
                print("4. Average Score")
                print("5. Salary")
                col = input("Enter the column to search: ")
                if col in ['4', '5']:
                    print("Example single search =>`80` or multiple search =>`80 90 100`")
                elif col == '1':
                    print("Example single search =>`0001` or multiple search =>`0001 0002 0003`")
                elif col == '2':
                    print("Example single search =>`John` or multiple search =>`John Harry Mary`")
                elif col == '3':
                    print("Example single search =>`HR` or multiple search =>`HR IT Marketing`")
                list_search = input("Enter the values to search: ").strip().split()
                bfo.showSpecificData(col, list_search)
            case '3':
                bfo.exportReport()
            case '4':
                if input("Do you want to exit? (y/n): ").lower() == 'y':
                    break
            case _:
                print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        input("Press Enter to continue...")