import json
from dataclasses import dataclass

import psycopg2
from psycopg2.extensions import connection

from config.config import config


@dataclass
class BaseQueriesMixin:
    conn: connection

    def get_row_by_query(self, query: str, values: tuple = None) -> tuple:
        with self.conn.cursor() as cursor:
            cursor.execute(query, values)
            result = cursor.fetchone()
        if result:
            return result
        return (None,)

    def execute_query_and_commit(self, query, values=None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, values)
            self.conn.commit()


class UserInterface(BaseQueriesMixin):

    def _exists(self, user_id: int) -> bool:
        query = "SELECT EXISTS(SELECT 1 FROM users WHERE user_id = %s);"
        values = (user_id,)
        result = self.get_row_by_query(query, values)
        return result[0]

    def create_if_not_exists(
            self,
            user_id: int,
            username: str,
            name: str,
    ) -> None:
        if not self._exists(user_id):
            query = '''
            INSERT INTO users (user_id, username, name)
            VALUES (%s, %s, %s);
            '''
            values = (user_id, username, name)

            self.execute_query_and_commit(query, values)

            print('Пользователь сохранён')

# @dataclass
# class User:
#     user_id:int
#     username:str
#     name:str


class Database(BaseQueriesMixin):
    def __init__(self):
        self.conn = psycopg2.connect(
            host=config.db.db_host,
            port=config.db.db_port,
            database=config.db.database,
            user=config.db.db_user,
            password=config.db.db_password,
        )
        self.user_interface = UserInterface(self.conn)
        # self.book_interface = BookInterface(self.conn)

    def get_table_data_as_dict(self, table_name: str) -> dict[int:tuple]:
        with self.conn.cursor() as cursor:
            query = f"SELECT * FROM {table_name};"
            cursor.execute(query)
            results: dict[int:tuple] = {x[0]:x[1:] for x in cursor.fetchall()}
            return results


bot_database = Database()

# print(bot_database.get_table_data_as_dict('users'))