PART 2: SQL Basics

# Terminologies
1. SQL `/se-quel/`
 * Structured Query Language
 * A declarative language.
 * A language that allows reading or manipulation of a database.
2. CRUD
 * Create, Read, Update, Delete
3. ACID (Transaction)
 * Guarantees data validity despite errors.
 * Atomicity - each transaction either succeeds or fails completely.
 * Consistency - data written to the database must be valid according to defined rules.
 * Isolation - separate transactions must not interfere with each other.
 * Durability - committed transactions remains in non-volative memory even after system failures.

# SQL
 - allows users to create Databases and Tables,
 - select pieces of data,
 - make changes,
 - remove data,
 - and more.

# Initial Setup
1. Enable the server
2. Run the Database Management System (DBMS).
3. Connect to the database.
4. Perform operations.

# SQL Commands
1. Data Query Language (DQL)
  * SELECT - Retrieve data from table(s)
2. Data Manipulation Language (DML)
  * INSERT - Insert data into table
  * UPDATE - Update data in table
  * DELETE - Delete data from table
3. Data Definition Language (DDL)
  * CREATE - Create database object
  * ALTER - Modify database object
  * DROP - Delete database object
4. Data Control Language (DCL)
  * GRANT - Assign privilege
  * REVOKE - remove privilege

# SQL Data Types
 * Common data types are available on most DBMS.
 * Different DMBS may differ in the set of other native data types.
 * Users may create custom data types.
 * Refer to the appropriate documentation for naming convention.
 * Data Types, equivalents, and aliases:
     - int
     - decimal, numeric
     - real, float4
     - float8
     - varchar
     - timestamptz

# Manipulating the Database
1. Initially create a database:
 * Execute command: ```CREATE DATABASE db;```
2. Create new tables:
 * Format:
        ``` CREATE TABLE tbl (
            column {DATATYPE} {PRIMARY KEY} {DEFAULT X} {NOT NULL}); ```
 * Execute command:
        ``` CREATE TABLE tbl (
            id INT PRIMARY KEY,
            column VARCHAR(128); ```
3. Add a new table column:
 * Execute command: ```ALTER TABLE tbl ADD col4 VARCHAR(1024);```
4. Remove an existing table column:
 * Execute command: ```ALTER TABLE tbl DROP COLUMN col4;```
5. Remove an existing table column:
 * Execute command: ```ALTER TABLE tbl DROP col4;```
6. Rename an existing table:
 * Execute command: ```ALTER TABLE tbl RENAME TO name;```
7. Rename an existing column in table:
 * Execute command: ```ALTER TABLE tbl RENAME column TO name;```
8. Clear all data from an existing table:
 * Execute command: ```TRUNCATE TABLE tbl;```
9. Delete an existing table:
 * Execute command: ```DROP TABLE tbl;```
10. Delete the database:
 * Execute command: ```DROP DATABASE db_name;```

# Comments
```sql
-- This is a comment
/* This is a multiline comment
   This is a multiline comment */
```

# Selecting Table Data
```sql

SELECT { DISTINCT } {*  or columns, } { or AGGREGATE(column) }
FROM tbl
{INNER | LEFT | RIGHT | FULL OUTER | CROSS} JOIN tbl ON
WHERE condition { AND | OR conditions } { or column BETWEEN x AND y }
GROUP BY column
HAVING condition { AND | OR conditions }
ORDER BY column {ASC* | DESC } {, column ASC* | DESC }
LIMIT n
OFFSET n;

SELECT *
FROM (Sub Query) AS subquery
WHERE condition


```
**SELECT** - columns and/or functions to display or operate on.
**DISTINCT** - defines whether only unique values will be operated on.
**FROM** - table to get records from.
**WHERE** - set of conditions to filter row data.
**HAVING** - set of conditions to filter resulting data.
**ORDER BY** - table to get records from.
**LIMIT** - maximum rows to return, prevents accidental reading of large of data.
**OFFSET** - Skips the n number of rows in the result.

**Examples:**
 1. ```SELECT * FROM users;```
 2. ```SELECT name, age, gender FROM users;```
 3. ```SELECT COUNT(*) FROM users;```

# AGGREGATE FUNCTIONS
 - `AVG(\*)` - returns the average of the selected column.
 - `COUNT(\*)` - count the number of rows in the selected column.
 - `SUM(\*)` - sums the values in the selected column.
 - `MAX(\*)` - get the maximum value in the selected column.
 - `MIN(\*)` - get the minimum value in the selected column.
 - `ROUND(\*)` - returns an integer result from a float value.


# Adding New Table Data
1. Add new row:
 * Execute command:
        ```INSERT INTO tbl (tbl_id, column, col2, col3, col4)
            VALUES
                { (DEFAULT, 'a', 'b', 'c', 'd'), }
                (DEFAULT, 'a', 'b', 'c', 'd')
            { RETURNING * };```
**Notes:** Multi-row command allows faster batch inserts.

# Update Table Data
# Format
```sql
UPDATE tbl
{ SET column=123456, }
{ SET column=2*column, }
SET col2='value'
WHERE condition { AND | OR condition2 } { or column IN (val1, val2, ...) };
```

# Delete Table Data
# Format
```sql
DELETE FROM tbl
WHERE condition { AND|OR condition2 };
```

# Joins
 - Allows selection of multiple data from across different tables.

# Views
 - A virtual table that collects matching data from multiple tables.

# Create a view
```sql
CREATE VIEW name(column, col2)
AS SELECT column, col2
FROM tbl
```

# Delete a view
```sql
DELETE VIEW name
```

# Indices
 - Instead of the slow WHERE clause that looks up on every single record,
    creating an index makes queries fast and efficient on larger tables.
 - Use indices wisely, it requres additional storage and will take time to revise the index when inserting new data.
```sql
CREATE INDEX { tbl_{column_}col2_idx }
ON tbl ({ column, } col2)
```

# Transactions 
 - Allows undoing the series of previous commands if one command fails. 
 

*References* 
* https://www.sqlshack.com/an-overview-of-sql-server-data-types/
* https://www.postgresql.org/docs/current/datatype.html