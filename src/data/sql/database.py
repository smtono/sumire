"""
This module is used to define the database for the system
As well as functions used to interact with the database
This system uses a SQLite database
"""

import logging
import sqlite3
from sqlite3 import Error

class Database():
    """
    This class is used to create a database and manipulate it.
    """
    def __init__(self, db_name: str) -> None:
        self.connector = sqlite3.connect(f"src\data\{db_name}.db")
        self.cursor = self.connector.cursor()

    def create_db(self, db_name: str):
        """
        Creates a database with the given name

        Args:
            db_name: str
                The name of the database to be created
        """
        open(f'database/{db_name}.db', 'w+')

    #######################
    # Query Manipulation
    ########################
    def select_data(self, query_for: str, query_table: str, where: str=None):
        """
        Selects data from a table

        Args:
            query_for: str
                The data to be queried
            query_table: str
                The table to be queried
        """
        if where:
            try:
                self.cursor.execute(f"SELECT {query_for} FROM {query_table} WHERE {where};")
                return self.cursor.fetchall()
            except Error as err:
                if err != 0:
                    logging.warning("Problem with table Select.")
                    logging.error(f"error code: {err}")
                else:
                    logging.error("An unknown problem has occured.")
                    raise Exception("An unknown problem has occured.")
        else:
            try:
                self.cursor.execute(f"SELECT {query_for} FROM {query_table};")
                return self.cursor.fetchall()
            except Error as err:
                if err != 0:
                    logging.warning("Problem with table Select.")
                    logging.error(f"error code: {err}")
                else:
                    logging.error("An unknown problem has occured.")
                    raise Exception("An unknown problem has occured.")

    def insert_data(self, table_name: str, columns: str, data: str):
        """
        Inserts data into a table

        Args:
            table_name: str
                The name of the table to be updated
            columns: str
                The columns to be updated
            data: str
                The data to be inserted
        """
        try:
            self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({data})")
        except Error as err:
            if err != 0:
                logging.warning("Problem with Data Insertion.")
                logging.error(f"error code: {err}")
            else:
                logging.error("An unknown problem has occured.")
                raise Exception("An unknown problem has occured.")
    
    def update_row(self, table_name: str, data_args: str, where: str):
        """
        Updates a row in a table with the given name

        Args:
            table_name: str
                The name of the table to be updated
            data_args: str
                The arguments for the table to be updated
            where: str
                The where statement for the update
        """
        try:
            self.cursor.execute(f"UPDATE {table_name} SET {data_args} WHERE {where}")
        except Error as err:   
            if err != 0:
                logging.warning("Problem with table Update.")
                logging.error(f"error code: {err}")
            else:
                logging.error("An unknown problem has occured.")
                raise Exception("An unknown problem has occured.")

    def custom_query(self, sql_query: str):
        """
        Executes a custom query

        Args:
            sql_query: str
                The query to be executed
        """
        try:
            self.cursor.execute(sql_query)
        except Error as err:
            if err != 0:
                logging.warning("Problem with Custom Query.")
                logging.error(f"error code: {err}")
            else:
                logging.error("An unknown problem has occured.")
                raise Exception("An unknown problem has occured.")
        self.commit()

    #######################
    # Table Manipulation
    ########################
    def create_table(self, table_name: str, table_args: str):
        """
        Creates a table with the given name

        Args:
            table_name: str
                The name of the table to be created
            table_args: str
                The arguments for the table to be created
        """
        try:
            self.cursor.execute(f"CREATE TABLE {table_name} ({table_args});")
        except Error as err:
            if err != 0:
                logging.warning("Table already exists.")
                logging.error(f"error code: {err}")
            else:
                logging.error("An unknown problem has occured.")
                raise Exception("An unknown problem has occured.")

    def alter_table(self, table_name: str, table_args: str):
        """
        Alters a table with the given name

        Args:
            table_name: str
                The name of the table to be altered
            table_args: str
                The arguments for the table to be altered
        """
        try:
            self.cursor.execute(f"ALTER TABLE {table_name} {table_args}")
        except Error as err:
            if err != 0:
                logging.warning("Problem with table Alter.")
                logging.error(f"error code: {err}")
            else:
                logging.error("An unknown problem has occured.")
                raise Exception("An unknown problem has occured.")
    
    def clear_table(self, table_name: str):
        """
        Clears a table with the given name

        Args:
            table_name: str
                The name of the table to be cleared
        """
        try:
            self.cursor.execute(f"DELETE FROM {table_name}")
        except Error as err:   
            if err != 0:
                logging.warning("Problem with table Clear.")
                logging.error(f"error code: {err}")
            else:
                logging.error("An unknown problem has occured.")
                raise Exception("An unknown problem has occured.")

    def delete_table(self, table_name: str):
        """
        Deletes a table with the given name

        Args:
            table_name: str
                The name of the table to be deleted
        """
        try:
            self.cursor.execute(f"DROP TABLE {table_name}")
        except Error as err:   
            if err != 0:
                logging.warning("Problem with table Delete.")
                logging.error(f"error code: {err}")
            else:
                logging.error("An unknown problem has occured.")
                raise Exception("An unknown problem has occured.")

    def update_table(self, table_name:str, data_args:str):
        """
        Updates a table with the given name

        Args:
            table_name: str
                The name of the table to be updated
            data_args: str
                The arguments for the table to be updated
        """
        try:
            self.cursor.execute(f"UPDATE {table_name} SET {data_args}")
        except Error as err:   
            if err != 0:
                logging.warning("Problem with table Update.")
                logging.error(f"error code: {err}")
            else:
                logging.error("An unknown problem has occured.")
                raise Exception("An unknown problem has occured.")

    # utils
    
    def commit(self):
        """
        Commits changes to the database
        """
        self.connector.commit()
