heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']

def show_options():
    print("1. Display Heroes")
    print("2. Add Heroes")
    print("3. Insert Heroes")
    print("4. Remove Heroes")
    print("5. Display Sorted Heroes (Ascending/Descending)")
    print("6. Exit")

def display():
    print(heroes)
    input("Press Enter.....")

def add_hero():
    hero = input("Enter hero for add: ")
    heroes.append(hero)
    print("Successfully adding")
    input("Press Enter.....")

def insert_hero():
    hero = input("Enter hero for insert: ")
    position = int(input("Enter position for insert: "))
    heroes.insert(position, hero)
    print("Successfully inserting")
    input("Press Enter.....")

def remove_hero():
    hero = input("Enter hero for remove: ")
    heroes.remove(hero)
    print("Successfully removing")
    input("Press Enter.....")

def display_sorted_heroes():
    print("Select option for display")
    print("1. Ascending")
    print("2. Descending")
    while True:
        option_display = input("Enter your option: ")
        match option_display:
            case '1':
                print(sorted(heroes))
                break
            case '2':
                print(sorted(heroes, reverse=True))
                break
            case _:
                print('Enter number 1 or 2 only.')
    print("Successfully sorted displaying")
    input("Press Enter.....")

while True:
    show_options()
    options = input("Enter your options: ")
    match options:
        case '1':
            display()
        case '2':
            add_hero()
        case '3':
            insert_hero()
        case '4':
            remove_hero()
        case '5':
            display_sorted_heroes()
        case '6':
            if input("Enter 'y' for comfirm: ") == 'y':
                break
        case _:
            print('Enter number 1 to 5 only.')
            input("Press Enter.....")