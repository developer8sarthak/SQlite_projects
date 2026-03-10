import sqlite3
import requests 
import json
connection = sqlite3.connect("chat.db")
c = connection.cursor()
c.execute(""" CREATE TABLE IF NOT EXISTS conversation(
               id INTEGER PRIMARY KEY,
        prompt TEXT NOT NULL,
        content TEXT NOT NULL
)
""")

url = 'http://localhost:11434/api/chat' 


content   = " "
exit = 'c'
while exit != 'n':
        prompt = input("enter your folow up:")
        
        f_prompt = f"{prompt} , your last reply was : {content}"
        payload = {
                "model"  : "smollm:360m",
                "messages" : [
        {
                "role" : "system",
                "content"  : "you area a simple  chat  assistant , tkae in a polite and engaging way"
        },
        {
                "role" : "user",
                "content" : f_prompt
        }
        ],
        "stream" : False
        }

        response = requests.post(url ,  json=payload)
        data = response.json()
        content = data['message']['content']

        if response.status_code == 200:
                print(f">> {content}")
        else:
                print(f"Requests failed  : {response.text}")
        c.execute("INSERT INTO  conversation(prompt , content) VALUES(? , ?)" , (prompt , content))
        connection.commit()
        exit =  input("enter 'n' to exit the chat or continue by entring 'c' ")
        
