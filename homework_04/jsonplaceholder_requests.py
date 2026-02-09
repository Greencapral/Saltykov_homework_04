"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def fetch_json(session, number: int, tp: str) -> dict | None:
    if tp == "user":
        url = f"{USERS_DATA_URL}{number}"
    elif tp == "post":
        url = f"{POSTS_DATA_URL}{number}"
    async with session.get(url) as response:
        return await response.json()
