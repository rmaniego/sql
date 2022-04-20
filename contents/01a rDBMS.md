PART 1a: Relational Databases
Sources: Socratica (YouTube), others

# Data
 - Information or facts related to an entity.
 - Mainly consisted of text and numbers in early days of computing.
 - In the modern age, there are new kinds of data such as audio, images, graphics, and video.

# Entity Relationship Diagram (ERD)
 - A structured representation of a database.
 - An entity can be a place, person, or an object of a conceptual existence, such as company, job, etc.
 - Each entity has one or more attributes describing it.
 - It is used as a reference, that enables better planning of attributes, keys, relationships, and other crucial aspects.
 - It is just a concept and a visual representation for database designers and for documentation only.
 - It is used to identify:
    * an entity - a bigger data object where other data can be referenced to it.
    * attributes - a part of the entity, these are the column names and the fields associated to it.
    * keys - unique attributes that can be used to connect relationships between two or more tables.
    * relationship - the link between two entities (tables), such as primary or foreign keys.
 - `ERD` is a part of the database design process.
 - Identify all the necessary entities and its corressponding attributes and relationships before designing the database.
 - Creating an `ERD` allows designers to find missing entities, attributes, or relationships to design a better database.
 - Keep attributes unique, descriptive, and relevant.

```text
    Entity  - Attributes
    Student - Student ID, Student Name, Student Gender, etc.
```

# ERD Representation
 - It is not the same with a flowchart.
 - Rectangle: entity
 - Rhombus: relationships
 - Elliptical: attributes
 
# Tables
 - May be called as `relations`.
 - The 2-dimensional intersection of a column and a row is called a field.
 - An entity can also be broken down into two or more tables.
 - Keys are identifiers and are common attributes found in one or more tables.
    * Primary Key `PK`: A singular column, usually with a numeric attribute such that it is unique throughout its table and it cannot be left empty or `null`. It is commonly designated as the first column.
    * Foreign Key `FK`: Is a key from its main table used or refered in another table, an `FK` cannot be created if an equivalent `PK` is not present in the main table. A `PK` in one table is an `FK` in an another relational table.
    * Unique Key: Similar to a `PK` but allow empty or `null` values. A table can have multiple unique keys.
 - Keys are used to create a link between tables, with a unique nature, ensures data consistency and validity in a table, and provide easier data retrieval.

# Database
 - An organized collection of structured information, or data, typically stored electronically in a computer system.
 - Usually controlled by a database management system.
 - A systematic collection of data, structured and organized in a meaningful way.

# Database Management Systems
 - Help in managing and organizing data efficiently.
 - A collection of programs that enables users to:
    * create and access a database,
    * manipulate the data, and
    * provide protection and security to the database.
 - May contains files such as documents, spreadsheets, photos, etc.

# Relational `DBMS` (RDBMS)
 - A collection of tables.
 - Contains a certain relationship between tables.
 - Each table contains a define set of columns and rows to contain the data.
 - Each row is called a *record*.
 - Each table can be related to another table.
 - The collection of tables in a database is called a *schema*.
 - A *primary key* is a value that uniquely identifies each record in a specific table.
 - Multiple tables in an `RDBMS` maybe interelated in one way or another.

# Database Server
 - The default database can be `Master`, `PostgreSQL`, etc.
 - A new database must be created and named specific to the project intended.

# Commercial
 * Paid software or service.
 * Includes: Oracle, IBM, and Microsoft  
     
# Open-Source
 * Manage by a community, 
 * Publicly available, and is 
 * Open for public use, with varying terms and conditions.
 * Licenses differs, but is usually permissive.
 * Example includes: MySQL/i, MariaDB (MySQLi), PostgreSQL, SQLite 
 
# X/LAMPP
 * X-CrossPlatform/L-inux, A-pache, M-ySQL, P-HP, P-Perl
 * Offers MySQL, now MariaDB, as `DBMS`.
 * Can be installed locally or configured in a server or vitual machine.
 
# Data and Simultaneous Access
 * Small Data/Limited Users: Locally-stored Database for control and fixed costs. 
 * Large Data/Simultaneous Access: Cloud Computing. 
 
# Local and Open-source 
 * Customizable, but requirements are limited to hardware and software availability.
 * May cost less in money in short-term.
 * Cost more in time (latency) 
 
# Cloud Services
 * Marketed as **X as a Service** (`XaaS`).
 * Allows both proprietary and open-source databases.
 * Higher requirements normally mean higher costs.
 * Requirements: Data Center, server type, and backup (among other services).
 * Other cloud services: Data/file storage, Analytics, Artificial Intelligence, Machine Learning, etc. 
 * Use of data: Train Classifiers (ML), Build ML Models, Image Recognition, or Speech Recognition
 * Depending on the plan or package:
     - Automatic adjustments to the spike of simultaneous usage.
     - Horizontal Scaling: Add more servers to handle the load.
 * Money vs Time:
     - Cost more in money 
     - Cost less in time (global access, speed)
 * Choice for companies with a sizeable budget.
 
# Migration 
 * Migration of local, open-source databases to a cloud service is straightforward
 * There are tools available to streamline the migration process.
 
# MySQL/i vs MariaDB vs PostgreSQL 
 * Difference: Not much on core features 
 * Ownership: MySQL/i is owned by Oracle (through Sun Microsystems) and development is mostly inactive.
 * Open-source `DBMS`s are actively improved by its community of developers and users.
 * Some performace claims.
 * Other unique features.
 
# Transferable Skills 
 > While experience is mostly required, database management skills are mostly transferrable.
 1. SQL 
 2. Schema Design 
 3. Database Optimization 