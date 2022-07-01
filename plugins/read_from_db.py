import mysql.connector
from airflow.models import Variable
from mysql.connector.constants import ClientFlag


class SQLConnection:
    def __init__(self):
        self.res = None
        self.cursor = None
        self.config = {'user': "root",
                       'password': "Mala_das1965",
                       'host': "34.123.180.99",
                       'client_flags': [ClientFlag.SSL],
                       'database': 'reddit'}
        self.connection_sql = mysql.connector.connect(**self.config)

    def get_subreddits(self):
        self.cursor = self.connection_sql.cursor()
        self.cursor.execute("SELECT * FROM subreddits")
        self.res = self.cursor.fetchall()
        return self.serialize(self.res)

    def serialize(self, serialized_list):
        import json
        return json.dumps(serialized_list)


def main():
    return SQLConnection().get_subreddits()


if __name__ == "__main__":
    print(main())
