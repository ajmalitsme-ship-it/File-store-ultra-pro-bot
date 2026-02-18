import asyncio
from database.admins import add_admin


async def main():
    try:
        user_id = int(input("Enter Telegram User ID: "))
        await add_admin(user_id)
        print("✅ Admin added successfully.")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
