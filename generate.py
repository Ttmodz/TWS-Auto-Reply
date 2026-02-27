from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(input("38855554 "))
api_hash = input("be58dccadc5db92c02f36b9281fd07c4 ")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\nYour SESSION_STRING:\n")
    print(client.session.save())
