"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from dataclasses import dataclass
from pprint import pprint

import aiohttp
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from random import randint

from jsonplaceholder_requests import fetch_json
from homework_04.models.db import async_engine, ASYNC_Session
from homework_04.models.base import Base
from homework_04.models.user import User
from homework_04.models.post import Post


async def fetch_user_data() -> list:
    async with aiohttp.ClientSession() as session:
        q_of_users = 5
        k = randint(1, 7)
        user_tasks = []
        for number in range(1, q_of_users + 1):
            user_data_task = asyncio.create_task(fetch_json(session, number, "user"))
            user_tasks.append(user_data_task)
        user_data = await asyncio.gather(*user_tasks)
    return user_data


async def create_users(users: list) -> list:
    new_users_list = []
    async with ASYNC_Session() as session:
        for user in users:
            new_user = User(
            name = user["name"],
            username = user["username"],
            email = user["email"]
            )
            new_users_list.append(new_user)
        session.add_all(new_users_list)
    await session.commit()
    return users


async def async_main():
    Base.metadata.drop_all(async_engine)
    # Base.metadata.create_all(async_engine)


    # user_data = await fetch_user_data()
    # await create_users(user_data)
    # pprint(user_data)
    # new_posts = ["post"] * k
    # post_tasks = []
    #
    # for number in new_posts:
    #     post_data_task = asyncio.create_task(fetch_json(session, "post"))
    #     post_tasks.append(post_data_task)
    # post_data = await asyncio.gather(user_data_task, *post_tasks)

    # new_user = User(
    #     id=user_data["id"],
    #     name=user_data["name"],
    #     username=user_data["username"],
    #     email=user_data["email"],
    # )
    # print(new_user)
    # new_post = Post(
    #     title=post_data[0]["title"],
    #     body=post_data[0]["body"],
    #     user_id=new_user.id,
    # )
    #
    # print(new_post)
    # print(post_data)

    # async with async_engine.connect() as conn:
    #     res = await conn.execute(text("select now();"))
    #     print(res.scalar())
    #


if __name__ == "__main__":
    asyncio.run(async_main())
