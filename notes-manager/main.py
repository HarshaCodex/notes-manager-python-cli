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
        with open("notes.json", "r") as f:
            notes = json.load(f)
        
        if not notes:
            print("📭 No notes to update.\n")
        else:
            print("\n Your notes:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note['title']}")

            try:
                note_to_update = int(input("Enter the note number to update: "))
                if 1 <= note_to_update <= len(notes):
                    title = input("Enter title to update: ")
                    content = input("Enter content: ")

                    notes[note_to_update - 1]['title'] = title
                    notes[note_to_update - 1]['content'] = content

                    with open("notes.json", "w") as f:
                        json.dump(notes, f, indent=4)
                    
                    print("\nNote updated successfully")
                else:
                    print("❌ Invalid note number.\n")
            except ValueError:
                print("❌ Please enter a valid note number")
    elif choice == 5:
        print('🗑️ You chose to delete a note.\n')
        with open("notes.json", "r") as f:
            notes = json.load(f)

        if not notes:
            print("📭 No notes to delete.\n")
        else:
            print("\nYour notes:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note['title']}")
            
            try:
                note_to_delete = int(input("Enter the note number to delete: "))
                if 1 <= note_to_delete <= len(notes):
                    notes.pop(note_to_delete - 1)
                    print("\nNote deleted successfully")
                    with open("notes.json", "w") as f:
                        json.dump(notes, f, indent=4)
                else:
                    print("❌ Invalid note number.\n")
            except ValueError:
                print("❌ Please enter a valid note number")
    elif choice == 6:
        print('👋 Exiting... Goodbye!')
        break
    else:
        print('Please enter a valid choice between 1 and 6.\n')

