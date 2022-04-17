PART 4: Python 
 
# Initial Setup 
    1. Make sure Python is install and is ready for use. 
    2. Launch command prompt, and run: 
        ```pip install -U psycopg2``` 
    3. Create a Python project directory. 
    4. Create a Python application file. 

# Psycopg2
 * [Basic Usage](https://www.psycopg.org/docs/usage.html)
 * Is a PostgreSQL database adapter for Python.

## Python + PostgresSQL 
```python 
import psycopg2 
from arkivist import Arkivist


credentials = "arkivist-key.txt"
json = Arkivist("password.json", encrypted=True, credentials=credentials)
password = json.get("password")
 
database = psycopg2.connect(f"dbname=temp user=postgres password={password}") 
cursor = database.cursor() 
 
query = "SELECT * FROM tbl LIMIT 1" 
cursor.execute(query) 
database.commit() 
 
cursor.close() 
database.close() 
```