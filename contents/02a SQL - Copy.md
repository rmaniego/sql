PART 2: SQL Basics

# Terminologies

**SQL** `/se-quel/` 
 - Structured Query Language
 - A declarative language.
 - Developed in the 1970s by IBM researchers, Raymond Boyce and Donald Chamberlin.
 - A language that allows reading or manipulation of a database.
 - Some may call it as a `4th Generation` programming language, but some argues that querying is not the same as programming.
 - SQL is better than a spreadsheet based on speed.

**CRUD** 
 - Create, Read, Update, Delete

**ACID** (Transaction) 
 - Guarantees data validity despite errors.
 - Atomicity - each transaction either succeeds or fails completely.
 - Consistency - data written to the database must be valid according to defined rules.
 - Isolation - separate transactions must not interfere with each other.
 - Durability - committed transactions remains in non-volative memory even after system failures.

# Structured Query Language
 - allows users to create Databases and Tables,
 - select pieces of data,
 - make changes,
 - remove data,
 - and more.

# Naming Convention
 ***NOTE:*** May differ depending on the RDBMS being used, the specifics will be addressed the appropriate wiki.
 - There should be no spaces between words.
 - Title casing can be used to improve readability, other `DBMS` prefer lowercase and `snake_case`.
 - Attributes are called fields or columns.
 - Rows are called as records or tuples.
 - Be consisted throughout the database.

# Initial Setup
1. Enable the server
2. Run the Database Management System (DBMS).
3. Connect to the database.
4. Perform operations.

# SQL Commands
1. Data Query Language (DQL)
 - SELECT - Retrieve data from table(s)
2. Data Manipulation Language (DML)
 - A group of commands to store, modify, or delete data:
     * INSERT - Insert a row (or multiple rows) into a table.
     * UPDATE - Update all rows or a specific row(s) in table based on a condition. Conditional or complete update.
     * DELETE - Delete a row from table directly or based on a condition. Conditional or complete deletion.
3. Data Definition Language (DDL)
 - Are commands that defines the data structure:
     * CREATE - Create database object
     * ALTER - Modify database object, or alter the number of columns of a table.
     * TRUNCATE - Delete all rows (table data only) and free up space, but not the structure.
     * RENAME - Change the name of a table.
     * DROP - Delete database object, or a table including its structure and the data inside it.
4. Transaction Control Language (TCL)
 - Directly impacts the `DML` commands:
    * COMMIT - Confirms the DML transaction as permanent.
    * SAVEPOINT - Is a temporary save option to rollback if required.
    * ROLLBACK
5. Data Control Language (DCL)
 - Implement security measures in a database:
     * GRANT - Assign privileges or access to a specific user.
     * REVOKE - Restrict or remove privileges or access to a specific user.

# SQL Data Types
 - Common data types are available on most DBMS.
 - Different DMBS may differ in the set of other native data types.
 - Users may create custom data types.
 - Refer to the appropriate documentation for naming convention.
 - Data Types, equivalents, and aliases:
    * int
    * decimal, numeric
    * real, float4
    * float8
    * varchar
    * timestamptz

# Constraints
 - NULL: By default, allows records to successfully insert a null value to this attribute or column.
 - NOT NULL: Defines that an attribute or column does not allow an empty or null value and will cause an error if so.
 - UNIQUE: Defines that each value of the attribute or the column throughout the database is unique.
 - PRIMARY KEY: Is the combination of `UNIQUE NOT NULL` constraints, prevents duplicate records.
 - DEFAULT: Assign a default value if the column is not specified in the `INSERT` command.
 - CHECK: Add additional check of value being insert to a specific column, restricting it if it fails the condition.

# Manipulating the Database
***NOTE:*** Follow the appropriate syntax (or structure) in writing SQL commands, then end it with a semicolon `;`.
1. a. Initially create a database: ```CREATE DATABASE db;```
1. b. Set the default database: ```USE db;```
2. Create new tables:
 - Format:
        ``` CREATE TABLE tbl (
            column {DATATYPE} {PRIMARY KEY} {DEFAULT X} {NOT NULL}); ```
 - Execute command:
        ``` CREATE TABLE tbl (
            id INT PRIMARY KEY,
            column VARCHAR(128); ```
3. Add a new table column:
 - Execute command: ```ALTER TABLE tbl ADD col4 VARCHAR(1024);```
4. Remove an existing table column:
 - Execute command: ```ALTER TABLE tbl DROP COLUMN col4;```
5. Remove an existing table column:
 - Execute command: ```ALTER TABLE tbl DROP col4;```
6. Rename an existing table:
 - Execute command: ```ALTER TABLE tbl RENAME TO name;```
7. Rename an existing column in table:
 - Execute command: ```ALTER TABLE tbl RENAME column TO name;```
8. Clear all data from an existing table:
 - Execute command: ```TRUNCATE TABLE tbl;```
9. Delete an existing table:
 - Execute command: ```DROP TABLE tbl;```
10. Delete the database:
 - Execute command: ```DROP DATABASE db_name;```

# Notes
 - A comman acts as a separator, it can be used to define and separate columns or set of values in an SQL command.

# Comments
```sql
-- This is a comment
/* This is a multiline comment
   This is a multiline comment */
```

# Operators
 > Are symbols or words that impacts the results in a certain manner.
 1. Logical operators - Used in the WHERE clause, it derives a logical (True or False) output depending on the operator used.
    - AND: Is only true if the conditions are ALL true.
    - OR: Will become true if at least one condition is true, all conditions must be satisfied.
    - NOT: Inverts the logical value of the (set of) conditions it is referring to, at least one condition is satisfied.
 2. Arithmetic operators - Processes the data arithmetically.
 3. Comparison operators - Evaluates or derives a logical (True or False) output depending on the values being compared.
```sql
    SELECT * FROM tbl WHERE column>=value;
```
 4. Patterns:
    - LIKE operator: Lists the records containing a value similar to a pattern.
    - NOT LIKE operator: Lists the records not containing a value similar to a pattern.
```sql
    SELECT * FROM tbl WHERE column { NOT } LIKE "%PATTERN%";
```
 5. Listing operators
    - IN: Lists records that has a value in the specified set.
    - NOT IN: Lists the records that has a value not in the specified set.
```sql
    SELECT * FROM tbl WHERE column { NOT } IN (value1, value2, value3);
```
 6. Range oeprators
    - BETWEEN: Lists all the records that has a value falling within the the specified range.
    - NOT BETWEEN: Excludes the records that falls in the specified range.
```sql
    SELECT * FROM tbl WHERE column { NOT } BETWEEN value1 and value2;
```

# SQL Clauses
1. WHERE - Appy conditions to filter out data from a table.
2. GROUP BY - Groups the data based on the specified column.
3. ORDER BY - Sorts the data based on the order of the specified set of columns.

# Sorting
 - ASC: Ascending order
 - DESC: Descending order.

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
 1. ```SELECT - FROM users;```
 2. ```SELECT name, age, gender FROM users;```
 3. ```SELECT COUNT(*) FROM users;```

# Sub-Query
 - Is a `SELECT` command nested inside a parenthesis, and surrounded with another SQL command.
 - The outer query can be a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` command.
 - The inner query can be a simple `SELECT` or a complex command with functions and/or joins.
```sql
    SELECT * FROM tbl1 WHERE column1=>(SELECT MAX(column2) FROM tbl2);
```

# AGGREGATE FUNCTIONS
 - `AVG(\*)` - returns the average of the selected column.
 - `COUNT(\*)` - count the number of rows in the selected column.
 - `SUM(\*)` - sums the values in the selected column.
 - `MAX(\*)` - get the maximum value in the selected column.
 - `MIN(\*)` - get the minimum value in the selected column.
 - `ROUND(\*)` - returns an integer result from a float value.


# Adding New Table Data
1. Add new row:
 - Execute command:
        ```INSERT INTO tbl (tbl_id, column, col2, col3, col4)
            VALUES
                { (DEFAULT, 'a', 'b', 'c', 'd'), }
                (DEFAULT, 'a', 'b', 'c', 'd')
            { RETURNING - };```
**Notes:** Multi-row command allows faster batch inserts.

# Update Table Data
# Format
```sql
UPDATE tbl
SET {column=123456, }
    {column=2*column, }
    col2='value'
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
 - A virtual table created by a query, that collects matching data from multiple tables.
 - Can be used to conceal sensitive or confidential data fromt hose who are not allowed to view it.
 - Allows administrators simplify complex table relationships and/or provide privileged access to certain data from programmers who are allowed to access it.
 1. Simple View: Display pre-defined data from one base table.
 2. COmplex View: displays certain pre-defined datafrom multiple base tables.

**View Operations**
```sql
CREATE VIEW name AS
SELECT column1, column2
FROM tbl;

REPLACE VIEW name AS
SELECT column1, column2, column3
FROM tbl WHERE column='value';

DROP VIEW name;
DELETE VIEW name;
```

# Indices
 - Instead of the slow WHERE clause that looks up on every single record,
    creating an index makes queries fast and efficient on larger tables.
 - Restrict indices to columsn frequently queried upon.
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