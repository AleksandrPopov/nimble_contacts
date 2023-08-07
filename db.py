import psycopg2

from config import HOST_DB, PORT_DB, NAME_DB, USER_DB, PASS_DB


class DB:
    """ This is a class for working with a database """
    __instance = None

    def __new__(cls, *args, **kwargs):
        """ Create a new instance if it does not exist, otherwise, return the existing one """

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @staticmethod
    def __connect_db():
        """ Method for connecting to the database """

        return psycopg2.connect(
            host=HOST_DB,
            port=PORT_DB,
            dbname=NAME_DB,
            user=USER_DB,
            password=PASS_DB
        )

    def add_contacts(self, contacts: list) -> int:
        """
        Add contacts if they do not already exist
        :return count added contacts
        """
        count = 0
        with self.__connect_db() as db:
            cursor = db.cursor()
            query = (
                "INSERT INTO contacts (first_name, last_name, email) "
                "VALUES (%s, %s, %s) "
                "ON CONFLICT (email) DO NOTHING "
                "RETURNING first_name"
            )
            for contact in contacts:
                cursor.execute(query, contact)
                count = count + 1 if cursor.fetchone() is not None else count + 0

        return count

    def search_contacts(self, substring: str) -> list:
        """
        Search contacts in db on query
        :return list searched contacts
        """
        with self.__connect_db() as db:
            cursor = db.cursor()
            query = (
                "SELECT * FROM contacts "
                "WHERE to_tsvector(first_name) || to_tsvector(last_name) @@ to_tsquery(%s)"
            )
            cursor.execute(query, (substring,))

            return cursor.fetchall()
