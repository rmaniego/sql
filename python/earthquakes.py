import csv
import psycopg2
from maguro import Maguro
from presql import PreSQL
from arkivist import Arkivist

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

with PreSQL(dbname, user, password) as db:
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