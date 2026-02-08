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

from sqlalchemy import text
from homework_04.models.db import engine
from homework_04.models.base import Base


async def async_main():
    pass


def main():
    # with engine.connect() as conn:
    #     res = conn.execute(text("select now();"))
    #     print(res.scalar())
    print(Base.metadata.tables.keys())


if __name__ == "__main__":
    main()
