import os
import sys

import psycopg2 as dbapi2

INIT_STATEMENTS = [
    """
    create table if not exists tool_list(
        id serial primary key,
        name varchar not null,
        brand varchar not null
    )
    """
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py")  # , file=sys.stderr)
        sys.exit(1)
    initialize(url)
