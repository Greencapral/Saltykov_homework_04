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
import aiohttp
from sqlalchemy import text
import asyncio
from random import randint

from .jsonplaceholder_requests import fetch_json
from homework_04.models.db import engine
from homework_04.models.base import Base
from homework_04.models.user import User
from homework_04.models.post import Post



async def async_main():
    async with aiohttp.ClientSession() as session:
        k=randint(1, 7)

        user_data_task = asyncio.create_task(fetch_json(session, "user"))
        print(k)
        new_posts = ['post']*k
        post_tasks =[]

        for _ in new_posts:
            post_data_task = asyncio.create_task(fetch_json(session, "post"))
            post_tasks.append(post_data_task)
        user_data, *post_data = await asyncio.gather(user_data_task, *post_tasks)

        new_user = User(
            id=user_data["id"],
            name=user_data["name"],
            username=user_data["username"],
            email=user_data["email"],
        )
        print(new_user)
        new_post = Post(
            title=post_data[0]["title"],
            body=post_data[0]["body"],
            user_id=new_user.id,

        )

        print(new_post)
        print(post_data)



def main():
    with engine.connect() as conn:
        res = conn.execute(text("select now();"))
        print(res.scalar())
    print(Base.metadata.tables.keys())
    print(Base.metadata.tables)


if __name__ == "__main__":
    # main()
    asyncio.run(async_main())
