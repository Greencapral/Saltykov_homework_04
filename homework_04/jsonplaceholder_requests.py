"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def fetch_json(session, number: int, tp: str) -> dict | None:
    url =""
    if tp == "user":
        url = f"{USERS_DATA_URL}{number}"
    elif tp == "post":
        url = f"{POSTS_DATA_URL}{number}"
    async with session.get(url) as response:
        return await response.json()

async def fetch_data(q_of_data:int, typo: str):
    async with aiohttp.ClientSession() as session:
        tasks_list = []
        for number in range(1, q_of_data + 1):
            data_task = asyncio.create_task(fetch_json(session, number, typo))
            tasks_list.append(data_task)
        data_received = await asyncio.gather(*tasks_list)
    return data_received

