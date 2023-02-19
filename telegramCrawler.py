import asyncio
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram import filters

#請至https://my.telegram.org/apps申請
api_id = "xxx"
api_hash = "xxx"
app = Client("my_account", api_id=api_id, api_hash=api_hash)

#輸入你要爬的群組id或user_id
userId = "jesus"
group1Id = -123
group2Id = -456

# filter過濾器
f = filters.chat(group1Id) | filters.chat(group2Id) | filters.chat(userId)
@app.on_message(f)
async def my_handler(client, message):
    print(message)

    chatContent = message.text
    print(chatContent)
    trigger = str(chatContent).find("yourTriggerRule1")
    trigger2 = str(chatContent).find("yourTriggerRule2")
    if -1 != trigger or -1 != trigger2:
      # 會將message轉寄給自己
      await message.forward("me")

app.run()