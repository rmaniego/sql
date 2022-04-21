PART 1a: Relational Databases
Sources: Socratica (YouTube), others

# Data
 - Information or facts related to an entity.
 - Mainly consisted of text and numbers in early days of computing.
 - In the modern age, there are new kinds of data such as audio, images, graphics, and video.

# Entity Relationship Model
 - Was developed by Dr. Peter Chen in 1976.
 - It simplifies the taks of understanding the data requirements.
 - It helps in designing a well-structured database.
 - An `ER` model represents a real-world object.
 - An `ER` model is comprised of entity sets, its individual attributes, and the relationships.
 - An object is an entity and a group of similar objects is an entity set, also known as a table.
 - Entity sets are represented using rounded-rectaangles with a header name.
```text
    | Student |      | Teacher |
    |---------|+----<|---------|
    |         |      |         |
```
 - Attributes are properties describing an entity (or object), represented by an ellipse.
```text
              [student]
        |--------|--------|
     (Juan)    (23)     (172cm)
```
 - Relationships are denoted with a diamond/rhombus.
```text
    [teacher]-----<teaches>-----[student]
    [student]------<owns>--------[laptop]
```

**Types of Attributes**
 1. Key Attributes - Are unique information of entities in a set, such as IDs, represented by an underline.
 2. Composite Attributes - Are attributes that consists other attribtues, such as name which is usually comprised of a first, middle, last name, and even an extension. Another example is the address attribute containing the street, city, state, and country. This is represented by sub-attribute connected to its main attribute forming a tree-like structure.
 3. Multi-valued attributes: Are information that may contain one or more values such as phone numbers, it is represented by double ellipses.
 4. Derived attributes are values that can be derived from another attribute such as age from  date of birth, denoted by a dashed ellipse.

**Types of Entities**
 > The degree of relationship can be checked by observing an `ER` model.
 1. One-to-One Relationship `1:1` - The most common relation ship in a database where one instance of an entity is associated with one instance of another entity. Example: One student can be given one laptop, and that laptop only belongs to that student.
 2. One-to-Many Relationship `1:M` - One instance of an entity is associated with many instances of another entity, such as a class that can have multiple students.
 3. Many-to-Many `M:M` - Many instances of an entity can be related to many instances of another entity. Example: Students can enroll in different courses and a course can hold different students.

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
 - As a best oractice, creating `ERD` should be part of the database design process.
 - Identify all the necessary entities and its corressponding attributes and relationships before designing the database.
 - Creating an `ERD` allows designers to find missing entities, attributes, or relationships to design a better database.
 - Keep attributes unique, descriptive, and relevant.

```text
    Entity  - Attributes
    Student - Student ID, Student Name, Student Gender, etc.
```

# ERD Representation
 > It is not the same with a flowchart.
 - Rectangle: entity
 - Rhombus: relationships
 - Ellipse: attributes
 
# Tables
 - May be called as `relations`.
 - An entity can also be broken down into two or more tables.
 - The 2-dimensional intersection of a column and a row is called a field.
 - Each table can have one or more columns, which can hold a single data type.
 - Keys are identifiers and are common attributes found in one or more tables.
    * Primary Key `PK`: A singular column, usually with a numeric attribute such that it is unique throughout its table and it cannot be left empty or `null`. It is commonly designated as the first column.
    * Foreign Key `FK`: Is a key from its main table used or refered in another table, an `FK` cannot be created if an equivalent `PK` or *candidate key* is not present in the main table. A `PK` in one table is an `FK` in an another relational table.
    * Unique Key: Similar to a `PK` but allow empty or `null` values. A table can have multiple unique keys.
 - Keys are used to create a link between tables, with a unique nature, ensures data consistency and validity in a table, and provide easier data retrieval.
 - Defining the appropriate `PK` is the role of a database designer or engineer, and not of the `RDBMS`.
 - Each record (rwo or tuple) should have an equal length of values, though a value can be empty or null.
```text
    (1, Juan, 23, 172, 68),
    (2, Pedro, 22, 168, 71)
```

**Other Types of Keys**
 1. Super keys: Is a superset of all keys. Are combinations of columns of a table that it holds a unique value, such as the ID+Name.
 2. Candidate keys: A subset of the super keys. Are combinations of columns of a table which can uniquely identify each row with minimum redunduncy, such as ID+Email.
    * Prime attribute: An attribute which is a part of the candidate key.
    * Non-prime attribute: An attribute which is not a part of the candidate key.

# Database
 - Usually controlled by a database management system.
 - A systematic collection of data, structured and organized in a meaningful way.
 - An organized collection of structured information, or data, typically stored electronically in a computer system.

# Database Management System
 - Helps in managing and organizing data efficiently.
 - A collection of programs that enables users to:
    * create and access a database,
    * manipulate the data, and
    * provide protection and security to the database.
 - May contains files such as documents, spreadsheets, photos, etc.

# Relational Database
 - A collection of tables.
 - Introduced by Edward Frank Codd in the 1970s.
 - Codd proposed a models with simple tables instead of hierarchical and navigational structures.
 - Hierarchical and navigational databases were rigid, complex, an inflexible - search operations is difficult.
 - Contains a certain relationship between tables through one or more common information.
 - Each table contains a define set of columns and rows to contain the data.
 - Each row is called a *record*.
 - Each table can be related to another table.
 - The collection of tables in a database is called a *schema*.
 - A *primary key* is a value that uniquely identifies each record in a specific table.

**Rules:**
 1. Information Rule: Data must be stored in a table format, where all the data stored must be a value of the table cell.
 2. Guaranteed Access Rule: Every data will be accessible with a combination of a table name, primary key, and attribute name only.
 3. Systematic Treatment of `NULL` values: `NULL` values must have a systematic and uniform (ssingular) mening or treatment throughout the database.
 4. Active Online Catalog: The structure definition of the entire database must be stored in an online catalog, also known as a data dictionary, and can only be accessed by only by authorized users. The same langauge should be used to access the catalog and the database itself.
 5. Comprehensive Data Sublanguage Rule: The database can only be accessed using language witha linear syntax that supports data definition, data manipulation, and transaction amanagement operations - else it is a violation. The language can be used directly or by means of other applications.
 6. All views of a databse, must be also updateable by the system.
 7. High level Insert, Update and Delete: It shpuld also support union, intersection, and minus operations to yield sets of data records.
 8. Physical Data Independence: The data stored in a database must be independent of teh applications that access the database and the physical structural changes of a databse must not have any impact on how the data is accessed by the external applications.
 9. Logical Data Independence: The logical data in a database must be independent of the external applciations, but is one of the difficult rules to apply.
 10. Integrity Independence: All the integrity contrainst must can be independently modified in the backend without changes in the front-end interface.
 11. Distibution Independence: The end-user must not be able to see that the data is distributed over various locations.
 12. Non-subversion Rule: The interface should not allow bypas of security and integrity constarints.

```text
    | Attribute / Column |
    |--------------------|
    | Field (value)      | --> Record 1 (Row)
    |                    | --> Record 2
    |                    | --> Record ...
    |                    | --> Record n
```

# Relational `DBMS` (RDBMS)
 - A system that stores and manages data in rows and columns in a table-line manner.
 - Multiple tables in an relational database maybe interelated in one way or another.
 - It allows operations on the database and its associated data.
 - Data Abstraction: Hides unrelated data and show only data relevant to the user, appropriate to its role.
 - It controls `data redundancy` by removing multiple copies of information from the different instances of the system.
 - `RDBMS` allows data manipulation by using SQL to access or manage databases.
 - Allows multiple users with different `user-levels` or privileges.
 - Data Security: Users can be created and can be given privileges or revoked, access to the database are verified first.
 - It is still the database designers and engineers role to enforce quality, optimization, and security.
 - `RDBMS` allows concurrency or multiple users accessing the database at the same time, such as retrieval and manipulation.

# Normalization
 - The process of reducing data redundancy in a database to organize the table logically.
 - Poorly planned database can cause anomalies, this can be minimized through normalization.
 - Tables can be broken down into simpler tables, these tables must be connected with a relationship or keys.
 - Normalization can remove data redundancy and improve efficiency.
 - It is an integral part of the database design process:
    1. First Normal Form: Defined in the definition of the table itself, all the attributes must have atomic domains or indivisible units. Each attribute must only have a single value from its pre-defined domain.
    2. Second Normal Form: Removing prime attributes from candidate keys removes partial dependencies, use foreign keys isnstead of candidate keys.
    3. Third Normal Form: The database must be in Second Normal Form already, and where no non-prime attributes must be dependent in prime key attributes. Remove transitive dependences by creating a separate table to hold the candidate keys, but still linking the original table with the foreign key.

**Types of Anomalies**
 > Aside from anomalies, there will also be searching and sorting issues over a poorly designed database.
 1. Insertion anomalies - Some attributes cannot be inserted into the database in the absence of anotehr attributes, this means that one attribute is dependent on another attribute.
 2. Modification anomaly - Some values of a database are updated, but not all expected instances. 
 3. Deletion anomaly - Certain attributes are lost because of the deletion of other attributes.

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