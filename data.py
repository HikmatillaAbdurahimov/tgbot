import os
from dotenv import load_dotenv
import psycopg2
load_dotenv()

class Database:
    @staticmethod
    async def connect(query,query_type):
        with psycopg2.connect(database=os.getenv('database'),
                              user=os.getenv('user'),
                              password=os.getenv('password'),
                              host=os.getenv('host'),
                              port=os.getenv('port')
                              ) as conn:
            with conn.cursor() as cur:
                data = ["insert", "delete"]
                cur.execute(query)
                if query_type in data:
                    conn.commit()
                    if query_type == "insert":
                        print("malumot qo'shildi")
                    else:
                        print(cur.fetchall())

        @staticmethod
        def create_table():
            with psycopg2.connect(database=os.getenv('database'),
                                  user=os.getenv('user'),
                                  password=os.getenv('password'),
                                  host=os.getenv('host'),
                                  port=os.getenv('port')
                                  ) as conn:
                with conn.cursor() as cur:
                    create_table_query="""
                    create table if not exists data_tg(
                    id              serial primary key,
                    frist_name      varchar(255),
                    create_at       timestamp default current_timestamp,
                    user_id         uniqu,
                    );
                    """
                    cur.execute(create_table_query)
                    conn.commit()
        create_table()




