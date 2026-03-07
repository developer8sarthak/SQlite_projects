import sqlite3

connection = sqlite3.connect('youtube_videos.db')

con = connection.cursor()


con.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
""")

def add_video(name , time):
    con.execute("INSERT INTO videos (name , time) VALUES (?, ?)" , (name , time))
    print("Video added successfully")
def delete_video(id):
    con.execute("DELETE FROM videos WHERE id = ?", (id))
    print("Video deleted successfully")
def update_video(id , name , time):
    con.execute("UPDATE videos SET name =?, time = ? WHERE id = ?", (name, time, id))
    print("Video updated successfully")
def list_videos():
    con.execute("SELECT * FROM videos ")
    for video in con.fetchall():
        print(video)

def main():
    while True:
        print("\nYoutube Manager app with DB")
        print("1.ADD VIDEO")
        print("2.SHOW VIDEOS")
        print("3.UPDATE VIDEOS")
        print("4.DELETE VIDEOS")
        print("5.EXIT")

        choice = input("Enter your choice :")

        if choice == "1":
            name = input("Enter video name :")
            time = input("Enter video time :")
            add_video(name,time)
        elif choice == "2":
           list_videos()
        elif choice == "3":
            id = input("Enter video id to update :")
            name = input("Enter new video name :")
            time = input("Enter new video time :")
            update_video(id,name,time)
        elif choice == "4":
            id = input("Enter video id to delete :")
            delete_video(id)
        elif choice == "5":
            break
        else:
            print(f"Invalid choice :{choice}")
        connection.commit()

if __name__ == "__main__":
    main()


connection.close()

