from pyrogram.errors import UserNotParticipant
from database.settings import get_settings

async def check_force(client, user_id: int):
    settings = await get_settings()
    channel = settings.get("force_channel")
    force_join = settings.get("force_join_request")

    if not channel:
        return True

    try:
        member = await client.get_chat_member(channel, user_id)

        # Force Join Request Mode
        if force_join:
            return member.status in ["member", "administrator", "creator"]

        # Normal Force Subscribe
        return member.status not in ["left", "kicked"]

    except UserNotParticipant:
        return False
