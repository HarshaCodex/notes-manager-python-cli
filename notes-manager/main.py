import json
import os

if not os.path.exists("notes.json"):
    with open("notes.json", "w") as notes:
        json.dump([], notes)

header = '===== Personal Notes Manger ====='

menu = '''1. Add a new note
2. View all notes
3. Search notes by keyword
4. Update a note
5. Delete a note
6. Exit
'''

while True:

    print(header)
    print(menu)

    try:
        choice = int(input("Choose your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.\n")
        continue

    if choice == 1:
        print('📌 You chose to add a new note.\n')
    elif choice == 2:
        print('📋 You chose to view all notes.\n')
    elif choice == 3:
        print('🔍 You chose to search notes by keyword.\n')
    elif choice == 4:
        print('✏️ You chose to update a note.\n')
    elif choice == 5:
        print('🗑️ You chose to delete a note.\n')
    elif choice == 6:
        print('👋 Exiting... Goodbye!')
        break
    else:
        print('Please enter a valid choice between 1 and 6.\n')

