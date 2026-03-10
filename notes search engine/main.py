import sqlite3

connection = sqlite3.connect("notes.db")

c = connection.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS  notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            tag TEXT      
) 
""")


while True:
    print("\n1. add  note")
    print("2.  view note")

    choice = input("enter your choice :").strip()

    if choice == "1" :
        title = input("enter the title : ")
        content = input("enter the content : ")
        tag = input("enter the tag of the content :" )

        c.execute("INSERT OR IGNORE INTO notes(title , content  , tag ) VALUES(? , ? , ? )" , (title , content  , tag))
        connection.commit()
    elif choice == "2":
        tagsearch = input("enter the tag to search the notes : ").strip()
        c.execute("SELECT id, title, content, tag FROM notes WHERE tag = ?", (tagsearch,))
        rows = c.fetchall()
        if rows:
            print(f"\nNotes with tag '{tagsearch}':")
            print("-" * 60)
            for row in rows:
                note_id, title, tag, content = row
                print(f"ID: {note_id}")
                print(f"Title: {title}")
                print(f"Tag:   {tag}")
                print(f"Content:\n{content}")
                print("-" * 60)
        else:
            print(f"No notes found with tag '{tagsearch}'.")
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")

connection.close()

