from peewee import DatabaseProxy, SqliteDatabase

database_proxy = DatabaseProxy()  # Create a proxy for our db.

def database_connect(url):
    return SqliteDatabase(url)