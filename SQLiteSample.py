import pprint
from shutil import _StrOrBytesPathT
import sqlite3
from sqlite3 import Connection, Cursor, Error as SQLiteError
import os
from typing import Iterable
import SQLStatements as Asset

pp = pprint.PrettyPrinter(indent=4)
database = r".\Lohnverrechnung.db"


def dumpDB(db_file: _StrOrBytesPathT) -> None:
    """deletes the provided Database file

    Args:
        db_file (_StrOrBytesPathT): Path to Database file
    """
    try:
        os.remove(db_file)
    except:
        None


def createConn(db_file: str) -> Connection:
    """create Database connection

    Args:
        db_file (str): Path to Database file

    Returns:
        Connection: The created connection
    """
    try:
        return sqlite3.connect(db_file)
    except SQLiteError as e:
        print(e)


def commitAndCloseConn(conn: Connection) -> None:
    """Commit and Close the Connection

    Args:
        conn (Connection): Database Connection Object

    Returns:
    """
    try:
        conn.commit()
        return conn.close()
    except SQLiteError as e:
        print(e)


def commitConn(conn: Connection) -> None:
    """Commit the Connection

    Args:
        conn (Connection): Database Connection Object

    Returns:
    """
    try:
        conn.commit()
    except SQLiteError as e:
        print(e)


def execSQL(cur: Cursor, sqlStatement: str, values: Iterable[Iterable] = None) -> None:
    """Execute SQL Querys

    Args:
        cur (Cursor): Cursor
        sqlStatement (str): SQL Query
        values (Iterable[Iterable], optional): If provided, a executemany is executed. Defaults to None.

    Returns:

    """
    try:
        if values != None:
            return cur.executemany(sqlStatement, values)
        cur.execute(sqlStatement)
    except SQLiteError as e:
        print(e, sqlStatement)


def printTables(cur: Cursor):
    """print all Tables

    Args:
        cur (Cursor): Cursor

    Returns:
    """
    try:
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for [table] in cur.fetchall():
            if table == "sqlite_sequence":
                continue
            cur.execute("SELECT * FROM " + table + ";")
            pp.pprint(cur.fetchall())
    except SQLiteError as e:
        print(e)
        return None


def setupDatebase(cur: Cursor) -> None:
    """setup the Database

    Args:
        cur (Cursor): Cursor
    """
    execSQL(cur, Asset.sqlCreateLocationsTable)
    execSQL(cur, Asset.sqlCreateLokoTable)
    execSQL(cur, Asset.sqlCreatePersTable)
    execSQL(cur, Asset.sqlCreatePhoneTable)


def fillDatebase(cur: Cursor) -> None:
    """fill the Database

    Args:
        cur (Cursor): Cursor
    """
    execSQL(cur, Asset.sqlInsertIntoLocations, Asset.sqlLocations)
    execSQL(cur, Asset.sqlInsertIntoLoko, Asset.sqlLoko)
    execSQL(cur, Asset.sqlInsertIntoPers, Asset.sqlPers)
    execSQL(cur, Asset.sqlInsertIntoPhone, Asset.sqlPhone)


def main():
    dumpDB(database)
    conn = createConn(database)
    if conn is None:
        return print("Error! Cannot create DB Connection")
    cur = conn.cursor()
    setupDatebase(cur)
    commitConn(conn)
    fillDatebase(cur)
    printTables(cur)
    commitAndCloseConn(conn)


if __name__ == "__main__":
    main()
