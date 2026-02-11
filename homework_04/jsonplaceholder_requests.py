"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def fetch_json(session, number: int, tp: str) -> dict | None:
    """
    Получение JSON-данных с сервера по указанному типу ресурса (пользователь или пост).

    :param session: Объект клиентской сессии aiohttp.
    :param number: Номер ресурса (идентификатор пользователя или поста).
    :param tp: Тип ресурса ('user' или 'post').
    :return: Словарь с полученными JSON-данными или None в случае ошибки.
    """
    url = ""
    if tp == "user":
        url = f"{USERS_DATA_URL}{number}"
    elif tp == "post":
        url = f"{POSTS_DATA_URL}{number}"
    async with session.get(url) as response:
        return await response.json()


async def fetch_data(q_of_data: int, typo: str):
    """
    Параллельная загрузка данных (пользователей или постов) посредством группы асинхронных запросов.

    :param q_of_data: Количество элементов, которые нужно загрузить.
    :param typo: Тип ресурсов ('user' или 'post').
    :return: Список полученных JSON-данных.
    """
    async with aiohttp.ClientSession() as session:
        tasks_list = []
        for number in range(1, q_of_data + 1):
            data_task = asyncio.create_task(fetch_json(session, number, typo))
            tasks_list.append(data_task)
        data_received = await asyncio.gather(*tasks_list)
    return data_received
