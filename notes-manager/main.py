import json
import os

if not os.path.exists("notes.json"):
    with open("notes.json", "w") as notes:
        json.dump([], notes)

header = '\n===== Personal Notes Manger ====='

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
        title = input("Enter note title: ")
        content = input("Enter note content: ")

        new_note = {
            "title": title,
            "content": content
        }

        with open("notes.json", "r") as note:
            notes = json.load(note)

        notes.append(new_note)

        with open("notes.json", "w") as note:
            json.dump(notes, note, indent=4)

    elif choice == 2:
        print('📋 You chose to view all notes.\n')
        with open("notes.json", "r") as f:
            notes = json.load(f)
        
        if not notes:
            print("There are no notes present!!!")
        else:
            print("\n🗒️ Your Notes:\n")
            for index, item in enumerate(notes, start=1):
                print(f"{index}. {item['title']}")
                print(f'   {item['content']}')

    elif choice == 3:
        print('🔍 You chose to search notes by keyword.\n')
        keyword = input("🔎 Enter keyword to search: ").lower()

        with open("notes.json", "r") as f:
            notes = json.load(f)
        
        matching_notes = [
            note for note in notes
            if keyword in note['title'].lower() or keyword in note['content'].lower()
        ]

        if not matching_notes:
            print("❌ No matching notes found.\n")
        else:
            for index, note in enumerate(matching_notes, start=1):
                print(f"{index}. {note['title']}")
                print(f"   {note['content']}")
            
    elif choice == 4:
        print('✏️ You chose to update a note.\n')
    elif choice == 5:
        print('🗑️ You chose to delete a note.\n')
    elif choice == 6:
        print('👋 Exiting... Goodbye!')
        break
    else:
        print('Please enter a valid choice between 1 and 6.\n')

