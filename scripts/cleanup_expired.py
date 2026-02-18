import asyncio
from database.premium import remove_expired_premium
from database.files import delete_expired_files


async def main():
    print("🔄 Cleaning expired data...")

    await remove_expired_premium()
    await delete_expired_files()

    print("✅ Cleanup complete.")


if __name__ == "__main__":
    asyncio.run(main())
