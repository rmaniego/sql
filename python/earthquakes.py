import csv
import psycopg2
from maguro import Maguro
from arkivist import Arkivist


class Database():
    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
 
    def __enter__(self):
        if not isinstance(dbname, str) and isinstance(user, str) and isinstance(password, str):
            assert False, "Database parameters mus be in string format."
        self.connection = psycopg2.connect(f"dbname={self.dbname} user={self.user} password={self.password}")
        if self.connection is not None:
            self.cursor = self.connection.cursor()
        return self
    
    def set_client_encoding(self, encoding):
        if self.connection is not None:
            self.connection.set_client_encoding(encoding)
        
    def execute(self, query):
        if None not in (self.connection, self.cursor):
            self.cursor.execute(query)
            self.connection.commit()
        
    def mogrify(self, query, data):
        if None not in (self.connection, self.cursor):
            if isinstance(query, str) and isinstance(data, (list, set, tuple)):
                self.cursor.mogrify(query, data)
                self.connection.commit()

    def __exit__(self, type, value, traceback):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()

authfile = "data/postgres-superuser-auth.txt"
postgres = Arkivist("data/postgres-superuser.json", authfile=authfile)
# get credentials
user = postgres.get("user")
dbname = postgres.get("dbname")
password = postgres.get("password")


sql_earthquakes = "INSERT INTO earthquakes (occurred_on, latitude, longitude, depth, magnitude, calculation_method, network_id, place, cause)\nVALUES "
earthquakes  = Maguro("data/earthquakes.csv", newline="\n", delimiter=",", has_header=True, quote_strings=True)
header = earthquakes.get_header()
earthquakes.behead()

sql_earthquake_values = []
for earthquake in earthquakes:
    item = []
    for part in earthquake:
        if isinstance(part, str):
            part = f"'{part}'"
        item.append(str(part))
    sql_earthquake_values.append("(" + ",".join(item[1:]) + ")")
sql_earthquakes += ",\n".join(sql_earthquake_values) + ";"
earthquakes.set_header(header)

with Database(dbname, user, password) as db:
    new_earthquake_table = """
        CREATE TABLE IF NOT EXISTS earthquakes (
            earthquake_id integer GENERATED ALWAYS AS IDENTITY NOT NULL,
            occurred_on timestamptz,
            latitude float,
            longitude float,
            depth float,
            magnitude float,
            calculation_method varchar,
            network_id varchar,
            place varchar,
            cause varchar); """
    db.execute(new_earthquake_table)
    # db.execute(sql_earthquakes)