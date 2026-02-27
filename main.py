import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = os.getenv("YOUR_ID: ")
api_hash = os.getenv("YOUR_HASH: ")
session_string = os.getenv("YOUR_SESSION: ")

if not api_id or not api_hash or not session_string:
    raise ValueError("Missing environment variables!")

api_id = int(api_id)

client = TelegramClient(
    StringSession(session_string),
    api_id,
    api_hash
)

@client.on(events.NewMessage)
async def handler(event):
    me = await client.get_me()

    # If someone replies to your message
    if event.is_reply:
        replied = await event.get_reply_message()
        if replied and replied.sender_id == me.id:
            await event.reply(
                "👋 Thanks for tagging my message!",
                quote=True
            )

    # If someone mentions you
    if event.mentioned:
        await event.reply(
            "👋 I saw you mentioned me!",
            quote=True
        )

async def main():
    print("Userbot is running...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
