"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/1"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/1"


async def fetch_json(session,tp: str) -> dict|None:
    if tp == "user":
        url = USERS_DATA_URL
    elif tp == "post":
        url = POSTS_DATA_URL
    async with session.get(url) as response:
        return await response.json()

