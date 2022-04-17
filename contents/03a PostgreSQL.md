PART 2: PostgreSQL 
 
# [Terminologies] 
1. PostgreSQL 
    * /post-gres-sequel/ 
    * A database management system. 
    * Also known as Postgres. 
 
# PostgreSQL Download & Installation 
1. Go to PostgreSQL download page and select your platform. [Windows](https://www.postgresql.org/download/windows/) 
2. Click the latest release link and wait until completed. 
3. Run the downloaded file. 
4. In the Welcome page, click the `Next` button. 
5. The default Installation Directory is preset, click the `Next` button. 
6. Under the Components setup, 
    * Uncheck the pgAdmin item, and 
    * Click the `Next` button. 
7. Under the Password setup, 
    * Set the password for the superuser 'postgres', then 
    * Confirm the password, and 
    * Click the `Next` button. 
8. The default Server Port number is `5432`, click the `Next` button. 
9. Under the Advanced Options, 
    * Set your desired locale, and  
    * Click the `Next` button. 
10. In the Pre-installation Summary section, click the `Next` button. 
11. In the Ready to Install section, click the `Next` button. 
12. Wait until installation is completed. 
13. Upon completion, deselect the StackBuilder option. 
14. Click the `Finish` button to close the wizard.
15. **IMPORTANT!** Copy the /bin and /data directory to the `PATH` in the system/user environmnet variables.
 
# pgAdmin Installation 
> Open Source administration and development platform for PostgreSQL 
1. Go to pgAdmin download page and select your platform. [Windows](https://www.pgadmin.org/download/pgadmin-4-windows/) 
2. Click the latest release link and doqnload the executable file, wait until completed. 
3. Run the downloaded file. 
4. Select *for all users* in the option if desired. 
5. Under the Welcome section, click the `Next` button. 
6. Read the License Agreement, 
    a. Select 'I accept the agreement', and click the `Next` button. 
    b. If otherwise, thank you for visiting the blog. 
7. The default Destination Location is preset, click the `Next` button. 
8. Under the Start Menu Folder section, click the `Next` button. 
9. Under the Ready to Install section, click the `Install` button. 
10. Wait until installation is completed. 
11. Upon completion, click the `Finish` button to close the wizard. 
12. A manual restart may be needed to formally use the software.

# pgAdmin Initialization
1. Run pgAdmin application.
2. Set/provide the pgAdmin master password.
3. **IMPORTANT!** Do not change the configurations without prior research or knowledge.
4. When getting started, use the documentation for support.

# pgAdmin Overview
1. In the pgAdmin sidebar, expand the `Servers` item.
2. Expand the `PostgreSQL` child and initially provide the Postgres superuser password to continue.
3. Right-click on the `Databases` child and click the `Create > Database` option.
4. Set the Database name.
5. Check other tabs to customize the database.
6. The SQL tab will display the SQL command that will create the database once executed or saved.
7. Click the `Save` button.
8. Expand the newly created database and expand to the `Schemas` > `public` child.
9. Creating tables and views will create it under the `Tables` and `Views` child, respectively.

# pgAdmin Usage
1. In the pgAdmin sidebar, expand to `Servers` > `PostgreSQL` > `Databases` item.
2. Under `Databases`, right-click on your desired database and select the `Query Tool` option.
3. On the `Query Tool` tab, right-click and select `Detach Panel`.
4. Tap the title bar of the panel to expand.
5. You can now write and execute SQL commands.

# PostgreSQL Best Practices
 - Use lowercase and *snake_case* on table and column names.
 - Use *identity* columns and never `SERIAL PRIMARY KEY`.
 - Use `varchar` over `text`, `varchar(n)`, `char(n)`, and `char`.
 - Use `numeric` over `float` or `money` for values that involves a lot of arithmetic operations.
 - Use `timestamptz` or ~`timestamp with time zone` over `timestamp` and `timetz`, but never `timestamp(0)` and `timestamptz(0)`.
 - Use `CURRENT_TIMESTAMP` or `now()` for `timestamptz`.
 - Use `LOCALTIMESTAMP` for `timestamp`.
 - Use `CURRENT_DATE` for `date`.
 - Use `LOCALTIME` for `time`.
 - Use `BETWEEN x AND y` for integers and dates, not for `timestamp`s.
 - Use `NOT EXIST` over `NOT IN`.
 - Never use `trust` in the `pg_hba.conf` over non-local connections.

*Resources*
 - https://wiki.postgresql.org/wiki/Don't_Do_This