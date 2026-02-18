from pyrogram import Client

@Client.on_chat_join_request()
async def auto_approve(client, request):
    await request.approve()
