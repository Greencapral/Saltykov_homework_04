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
from pprint import pprint

import asyncio
from random import randint

from jsonplaceholder_requests import fetch_data
from homework_04.models.db import async_engine, ASYNC_Session
from homework_04.models.base import Base
from homework_04.models.user import User
from homework_04.models.post import Post



async def create_users(users):
    new_users_list = []
    async with ASYNC_Session() as session:
        for user in users:
            new_user = User(
            name = user["name"],
            username = user["username"],
            email = user["email"]
            )
            new_users_list.append(new_user)
            pprint(new_user)
        session.add_all(new_users_list)
        await session.commit()
    pprint(new_users_list)
    return users

async def create_posts(posts, users):
    new_posts_list = []
    async with ASYNC_Session() as session:
        for post in posts:
            new_post = Post(
            user_id = randint(1,users.__len__()),
            title = post["title"][:Post.max_title_len],
            body = post["body"][:Post.max_body_len],
            )
            new_posts_list.append(new_post)
            pprint(new_post)
        session.add_all(new_posts_list)
        await session.commit()
    pprint(new_posts_list)
    return users

async def async_main():
    if Base.metadata.tables:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


    user_data = await fetch_data(7,'user')
    await create_users(user_data)

    post_data = await fetch_data(18,'post')
    await create_posts(post_data,user_data)



if __name__ == "__main__":
    asyncio.run(async_main())
