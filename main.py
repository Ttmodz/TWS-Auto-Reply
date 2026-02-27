import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = os.getenv("38855554")
api_hash = os.getenv("be58dccadc5db92c02f36b9281fd07c4")
session_string = os.getenv("1BVtsOGUBu21ctDA9Nx7
2dpwyEhpX0PIf
fJ
хо4Q6mKvCх5Lr1bgN4хwIdVwvF4ТJPgMykuH4kHyNJ8FfaZPdąyіWWWе0AkMab2yd-еzsSBrPf_SYqDХЕ7gdВАрb05_
_BRwMCqBHXc0bDpe_4r8-kS650pMmak5ENZWYB4tiIU_WIRNgINzKM
_9fZ2GSNjK44n8tizL2ugcоSW₽tbZhyХd·9oXV5Bmх52JFmIОЕd16BtS2×HDI£wЕеubqіd9₽BAН£OуtCУvJ2ЕC-i0UTKаR_A3₽4dbХе_vnTIiiZw69mRHR-wFНgqoJv4nXvaPRLT6pjXpWdD_2Byt
OPQqiR2sdY2usawpbwro=")

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
