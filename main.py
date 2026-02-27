import os
from telethon import TelegramClient, events

api_id = int(os.getenv("38855554"))
api_hash = os.getenv("be58dccadc5db92c02f36b9281fd07c4")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    me = await client.get_me()

    if event.is_reply:
        replied = await event.get_reply_message()
        if replied.sender_id == me.id:
            await event.reply("👋 Thanks for tagging my message!", quote=True)

    if event.mentioned:
        await event.reply("👋 I saw you mentioned me!", quote=True)

print("Bot running...")
client.start()
client.run_until_disconnected()
