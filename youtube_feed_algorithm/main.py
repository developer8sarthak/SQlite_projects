from tagger_module import extract_keywords
import sqlite3

connection = sqlite3.connect("youtube.db")
c = connection.cursor()

search = input("enter your search query: ")
keywords = extract_keywords(search)

if not keywords:
    print("No valid keywords found!")
    connection.close()
    exit()

placeholders = " OR ".join(["tag LIKE ?"] * len(keywords))
query = f"SELECT title, tag FROM videos WHERE {placeholders}"

params = [f"%{kw}%" for kw in keywords]

c.execute(query, params)
titles = c.fetchall()

print(f"Videos matching your keywords ({', '.join(keywords)}):")
for tag, title in titles:
    print(f"[{title}] - {tag}")

connection.close()