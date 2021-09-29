/* 

FUNDAMENTALS OF RELATIONAL DATABASES - Scott Simpson


DATABASE

- A database is a structure that stores information in an organized,
consistent, reliable, and searchable way.

- A database gives us a way to add structure to data and to define rules
that the data must follow and a database gives us the tools both to
protect data and to use data to answer questions.

Why use a database?

- work with large amounts of data efficiently,
- they make updating data easy and reliable,
- they help to ensure accuracy,
- they offer security features to control access to information,
- they help us avoid redundancy.

RELATIONAL DATABASE

- A database that organizes data into relations or tables of related data.
In a relational database, tables are made up of rows, which represent instances
of a given entity, and columns, which represent attributes of each entity.
The set of columns is called a relation.

- Realtional database:
    - Tables:
        - Rows (instances of a given entity)
        - Columns (attributes of each entity)

- The structure of tables in the database is called the Schema.

- Columns data types:
    - Number,
    - String,
    - Date,
    - Boolean,
    - Binary.

UNIQUE VALUE

- In a database, a unique value is a value that doesn't show up in any other row
in a given column. So there's one and only one of any particular value for that
particular field. Most DBMS tools will allow us to set this constraint,
or limitation, on columns in our tables. So if we tried to enter a record with a
value that's already in the table, the database will reject it until the information
is changed to be unique.

- DBMS (DataBase Management Software) - a DBMS is the software, like SQL Server,
MySQL or Access, we use to interact with the database.

KEY

    - Unique value,
    - Primary key,
    - Synthetic/Surrogate key,
    - Composite key,
    - Foreign key.

- Unique values can also be used as keys. A key is a value we can use to refer to
only one specific row or record. A primary key is the most important key in a table,
though there can be others as well. A table doesn't require a primary key, but
having one helps to access specific records easily.

- In many cases, there isn't a natural piece of information that can be used as a key,
so we need to provide one. We can do this by adding a column to a table and setting
that column to require a unique value.

- In many DBMS tools, this is done by making the value in the new column a number
and telling the database to increment the number for every new number that's added.
When we add a field like this, we create a synthetic key or a surrogate key.

- In some situations, we might not be able to modify the schema of the table, and
we might need to use two or more fields in the data to act as a key. This is called
a composite key.

- When you set out to define your tables, you'll need to think about what value will
be used as a key or whether you need to add one yourself. Another term is foreign key,
and this is what a primary key from one table is called when it's referenced in
another table.

RELATIONSHIPS

- As a database becomes more complex, with two or more tables containing data that
we want to connect in some way, we need to define relationships. We need to tell the
database that particular records should be associated with each other. Of course,
we can use a database without using relationships.

- Simply querying a piece of information from this table and a piece of information
from that table, but being able to connect records to each other in various ways,
lets us use data in more complex and realistic applications.

- Types of Relationships:
    - One-to-Many   (1 - n),
    - Many-to-Many  (n - n),
    - One-to-One    (1 - 1).

- One to many is by far the most common relationship. This associates one record in
one table with multiple records in another table.  In order to use this kind of
relationship, we store the key from a record on the one side of the relationship
in each of the many records which reference it.

- A many to many relationship works in a similar way and in fact, in most DBMS tools
we model it using two one to many relationships. But we create a new table called
an ASSOCIATIVE or LINKING TABLE that contains columns for the foreign keys from
the tables we're associating.

        Customers
        +------------+--------+--------+--------+--------+
    +---| CustomerID | COL_01 | COL_02 | COL_03 | COL_04 |
    |   +------------+--------+--------+--------+--------+
    |   |            |        |        |        |        |
    |   +------------+--------+--------+--------+--------+
    |
    |       CustomersEvents - ASSOCIATIVE/LINKING TABLE
    |       +------------+---------+
    +-------| CustomerID | EventID |----+
            +------------+---------+    |
            |            |         |    |
            +------------+---------+    |
                                        |
            +---------------------------+
            |
        Events
        +---------+--------+--------+--------+
        | EventID | COL_01 | COL_02 | COL_03 |
        +---------+--------+--------+--------+
        |         |        |        |        |
        +---------+--------+--------+--------+

- One to one relationship isn't too widely used. Unlike a one to many relationship,
a one to one relationship associates only one record on one table with only one
record on another table, such that the targeted record can't be associated with
another record at the same time.

TRANSACTIONS

- The data in our database needs to remain accurate and that means we need to be
careful about how we update or modify information it contains. To protect against
all kind of errors, we use transactions.

- A transaction is a set of operations that must all be completed, and if for some
reason any of the individual operations aren't completed, no changes are made to
the database. Anything that's partially done will be undone. Transactions follow
a set of principles outlined by the acronym ACID.

- ACID:
    - Atomic,
    - Consistant,
    - Isolated,
    - Durable.

- Atomic means that the transaction is indivisible, that pieces of it can't be
separated out.

- Consistency means that whatever the transaction does, it needs to leave the
database in a valid or consistent state. The actions in a transaction can't violate
integrity rules that are defined for the database.

- Isolation means that while the activities in the transaction are being completed,
nothing else can make changes to the data involved.

- Durability means that the information we change in the transaction actually gets
written to the database. When the transaction is reported as complete, the data is
there. The change has been made.

- Anytime we have an activity made up of steps that must happen together, and when
we want to ensure that we have exclusive access to certain information while we
perform a task, we'll use a transaction.

- The capability for following the ACID principles are part of DBMS already, so
instead of having to write the code into logic that makes sure these conditions are
followed, all you have to do is tell the DBMS that you're doing a transaction, and
the software takes cares of the ACID requirements for you.

SQL (Structured Query Language)

- SQL allows us to write statements which the DBMS interprets, and that's how we
interact with the data in the database, from apps, or even within the DBMS itself.

- SQL roles:
    - DML (data manipulation language) - interact with the data in the database,
    - DDL (data definition language) - creating and modifying tables,
    - DCL (data control language) - controlling access to the tables.

- RDBMS (Relational Database Management System) tools:
    - Support ANSI (American National Standards Institute) SQL,
    - Langauge that extends ANSI:
        - T-SQL (Transact-SQL used by Miscrosoft SQL Server),
        - MySQL (an open-source DBMS).

- SQL statement (SELECT FirstName, LastName FROM Customers WHERE LastName = 'Jenkins';)
    - clauses (SELECT, FROM, WHERE, ...)
        - predicates (LastName = 'Jenkins')
        - expressions ('Jenkins')

- A clause will include a keyword, specifying some action to take and something to act
on or use. Expressions and predicates set parameters within which to operate.

- Statements can be written inside of software that works directly with the database,
like SQL Server Management Studio or phpMyAdmin. Or they can be incorporated directly
into program code in order to allow an app to access data.

- To ask for data from a database, we'll ask for the fields we want information from
and we'll specify the tables that contain the information: */

SELECT FirstName, LastName FROM Customers;

/* - We might also specify how to display, sort, or associate the information. And in
return, we'll get matching records or the fields from records which match our
criteria. */

SELECT FirstName, LastName FROM Customers WHERE Birthday = '1991-02-09';

/* - This statement, for example, will show us the first name and last name of
customers with a specific birthdate. */

SELECT FirstName, LastName, Birthday FROM Customers ORDER BY Birthday;

/* - And this one would return us a list of customers names and birth dates sorted
chronologically by birthday.

- In SQL, it's common to see the keywords written in uppercase, though it's not
strictly necessary. It can help with readability.

QUERIES

- Because we're asking for information from the database or asking for the database
to do something, these statements are called Queries.

CRUD (Create, Read, Update, Delete)

Putting data into a database, retrieving information from a database, changing
records, and removing records are typically things we'll do with a SQL query of
some sort. These activities create, read, update, and delete are called CRUD, and
they're the basis of interacting with data.

- ER Diagram (Entity Relationship Diagram) - a diagram that show our tables, fields
and relationships to plan and translate into schema of our database.

NAMING CONVENTIONS

    - use plurals for tables,
    - name the tables starting with a capital letter,
    - avoid using special characters and spaces in table names,
    - fields should be named singularly,
    - use UpperCamleCase

DATA TYPES

- Strings - alphanumeric characters and text:
    - CHAR      - fixed number od charcters,
    - VARCHAR   - variable number od characters up to a maximum length,
    - other types for longer text.

- Dates and Times:
    - DATE      - 2019-03-09,
    - DATETIME  - 2019-03-09 16:51:00,
    - TIMESTAMP - saved when record is updated.

- Numbers:
    - Integers,
    - Double precision,
    - Floating point,
    - Decimals.

- Binary.

- NULL - represence the absence of a value.

-  Some databases also accommodate geographic data, graphs, objects, and other more
exotic types.

PRIMARY AND FOREIGN KEYS

- PK (Primary Key): TablenameID or TablenamePK
    - Tablename - singular and corresponds to the table,
    - ID - indetifier/Key,
    - PK - primary key.

- Referental Inregrity - databases are aware of relationships and won't allow a
user to modify data in a way that violets those relationships.

NORMALIZATION

- Noramalization is proces of organizing data in database. Normalization is based
on rules that help us to reduce redundancy and improve the integrity of our data.

- Normalization helps us prevent problems in working with our data, and the process
should be revisited whenever there's a change to the schema or the structure of a
database. 

- Normalization rules:
    - First normal form     (1NF)
    - Second normal form    (2NF)
    - Third normal form     (3NF)

- First normal form - requires that values in each cell are atomic, and that tables
have no repeating groups. This means that each field in each table has only one
value in it, and that there are no columns representing repeated kinds of data for
each row. First normal form is often extended to include the idea that there aren't
duplicate rows in a table. This also suggests that the order of rows and columns is
not important to the data.

- Second normal form - says that no value in our table should depend only on part of
a key that can be used to uniquely identify a row. This means that for every column
in the table that isn't a key, each of the values must rely on only the whole key.
The values must describe something about that row that we can't determine from just
the part of a key. This problem comes up in the context of composite keys.

- Third normal form - tells us we shouldn't be able to figure out any value in a
column from a field that isn't a key. Let's look at the dishes table here as an
example.

- These rules are sets of formal criteria, and they build on top of each other,
step by step. We move through the forms as we optimize our database to third normal
form. When a normalization rule has been applied to a database, we can say that the
database is in that normal form. 

- Once your tables all satisfy first, second, and third normal form, the database
is normalized to third normal form. This helps to guarantee that your database has
low duplication, high integrity, and will be durable when you create, update, read,
and delete entries. 

DENORMALIZATION

- While normalizing databases to third normal form is a best practice, occasionally
there may be a business need or a database performance issue that requires violating
the rules of normalization. Denormalization is the process of intentionally
duplicating information in tables in violation of normalization rules.

- Denormalization is done after normalizing a database. It doesn't mean skipping
normalization altogether. 

- Denormalization is about trade-offs. Usually a gain in speed for a reduction in
consistency and that's a decision you'll need to make based on your own business
requirements. 

*/

-- create database:

CREATE DATABASE Restaurant;


--  sometimes we need to tell a system to use our newly created database:

USE Restaurant;


-- create table:

CREATE TABLE Customers(
    ...
);


-- add information about columns:

CREATE TABLE Restaurant(
    CustomerID INT(6) NOT NULL AUTO_INCREMENT, -- primary key
    FirstName VARCHAR (200) NOT NULL,
    LastName VARCHAR(200) NOT NULL,
    Email VARCHAR(200),
    Address VARCHAR(200),
    City VARCHAR(200),
    State VARCHAR(200),
    Phone VARCHAR (200) NOT NULL,
    Birthday DATE,
    FavoriteDish INT(6) REFERENCES Dishes(DishID) -- references on foreign key
    PRIMARY KEY (CustomerID)
);


/*

SQL QUERIE EXAMPLES 

    READ DATA

*/


-- Select all values from Customers table:

SELECT * FROM Customers;


-- Select first name, last name and email from Customers table:

SELECT FirstName, LastName, Email FROM Customers;


/* Select first name, last name and state from Customers table where customers are
only from state of California (CA): */

SELECT FirstName, LastName, State FROM Customers WHERE State="CA";


/* Select first name, last name and state from Customers table where customers are
only from state of California (CA) or Colorado (CO): */

SELECT FirstName, LastName, State FROM Customers WHERE State="CA" OR State="CO";

-- or look for fields that have similar values instead of exact matches:

SELECT FirstName, LastName, State FROM Customers WHERE State LIKE "C%";


/* Select first name, last name and state from Customers table where customers are
are named "Taylor": */

SELECT FirstName, LastName, State FROM Customers WHERE FirstName="Taylor";


-- Look for all the reservations on a particular day, February 6, 2019.

SELECT * FROM Resevations WHERE 'Date' > "2019-02-06" AND 'Date' < "2019-02-07";


/* Sorting results */


-- Look at the dishes in the Dishes table in alphabetical order by name:

SELECT * FROM Dishes ORDER BY 'Name';       -- ASC ascending order

SELECT * FROM Dishes ORDER BY 'Name' DESC;  -- DESC descending order


/* Look for all the reservations on a particular day, February 6, 2019. and then
return those in a sorted order: */

SELECT * FROM Resevations
WHERE 'Date' > "2019-02-06" AND 'Date' < "2019-02-07"
ORDER BY 'Date';


/* Aggregate functions */


/* COUNT() -  returns the number of records in a particular field from rows that
match a particular condition. */

-- how many customers we have in our customers table:

SELECT COUNT(FirstName) FROM Customers;


-- how many customers we have in our customers table from state of California:

SELECT COUNT(FirstName) FROM Customers WHERE State="CA";


-- SUM() - adds up all the values of the matching criteria.

/* Sum up the prices in the dishes table to see how much it would cost if someone
orderes one of each item one our menu: */

SELECT SUM(Price) FROM Dishes;

-- AVG() - average value.

SELECT SUM(Price), AVG(Price) FROM Dishes;

-- MIN() and MAX() - values.

SELECT SUM(Price), AVG(Price), MIN(Price), MAX(Price) FROM Dishes;


/*

Joining tables

- Ability to connect records across different relations or tables. Those relationships
are part of our data model, and when we're getting data from a database, we can write
a query that uses the connections between data to return us a useful result.

*/


-- look for customers favorite dishes:

SELECT FirstName, LastName, Dishes.'Name' FROM Customers
JOIN Dishes ON Customers.FavoriteDish = Dishes.DishID;


/* create a summary of all of our orders, with the customer name and phone number,
order date, items in the order, and total cost of the order. */

SELECT OrderDsihes.OrderID, Orders.OrderDate, Customers.FirstName, Customers.LastName,
Customers.Phone, GROUP_CONCAT(Dishes.'Name' SEPARATOR ', ') AS Items,
COUNT(OrderDsihes.DishID) AS Qty,
SUM(Dishes.Price) AS Total
FROM OrderDsihes
JOIN Dishes ON OrderDsihes.DishID = Dishes.DishID
JOIN Orders ON Orders.OrderID = OrderDsihes.OrderID
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY(Orders.OrderID);


/*

MODIFY DATA

    CREATE DATA

*/

-- add new customer to the database:

INSERT INTO Customers(FirstName, LastName, Email, Phone)
VALUES ("Jane", "Smith", "janesmith@mail.com", "444-333-555");
-- any values that we didn't provide are NULL


/* 
    UPDATE DATA
*/

/* one of our customers got a new email address and we need to make that
change to the record: */ 

UPDATE Customers SET Email = "leeroyjenkins@wow.com" WHERE CustomerID = 1;


/* 
    DELETE DATA
*/

DELETE FROM Customers WHERE CustomerID = 26;

/*

INDEXES, TRANSACTIONS AND STORED PROCEDURES

- Indexes, transactions, and stored procedures are all features offered by most
DBMS tools. How they are used and how you choose to apply them will vary based on
the software and your needs.

- Just like in a book, tables in a database can have indexes, where you can look
up information quickly. A primary key acts as an index, but sometimes, especially
on large tables, you may want to look up other fields. Normally, this involves
scanning the whole table for matching terms.

- On a large table, this kind of search might take a while, as the database compares
those fields in each row with the search term. But with an index on those fields,
the database stores a reference to what each value is in those fields and where it's
located, and using that index, the database can return information much faster, but
when we add indexes, it increases the amount of time some operations, like inserting
a record, will take. So like many optimizations you might make to a database, there
is a trade-off. 

- Transactions group queries or statements into a block of activities, where, if one
of the components fails for any reason, the whole group of statements is not executed,
and anything that's partially done is rolled back. This helps to guarantee that an
action isn't only partially applied, leaving the database in an inconsistent state.

- That means you'll need to think carefully about a whole action that you're planning
to do, what steps need to be taken, what business rules need to be applied, and which
pieces of data are affected. Creating a transaction in different DBMS tools will be
done differently depending on the software, but across the different types of tools,
the concept is the same.

- A stored procedure is kind of like a program you write that's stored on the database
server. It contains a series of commands that you can then reference and use when you
interact with the database. Using a stored procedure, you can avoid having to write
out a long or detailed query if it's something you use frequently. Stored procedures
are also used to provide safe or approved ways of dealing with sensitive data.

- Instead of allowing access to data directly from manually entered SQL, which could
contain errors, a database administrator often provides a set of stored procedures
designed to take certain input, run transactions, and verify a result of a query.
In many cases, access to certain sensitive data or whole tables is only allowed
through stored procedures rather than directly. 


ACCESS CONTROL, COMPLIANCE AND INJECTION

- Most database management systems provide various access control mechanisms,
including user accounts and control over whether certain people can access certain
tables or even individual columns. In the database we can grant user varying levels
of access to hold databases, tables, and even specific actions.

- We might define the user who can create, read, update, and delete data but who is
not allowed to change the schema of the database. And we might create another user
who only has read access and who can't modify data stored in the database at all.
When you're designing a database and granting access to the database and the data
it's important to consider your business requirements. It's also very important to
consider any compliance rules you need to follow. Personally identifiable information,
or PII, is very strictly regulated in some areas and some industries.

- When you're building your database you'll need to ensure that you're design and
methods accommodate requirements that you're subject to. Not following compliance
regulations can be a very costly mistake. Even with specific access control there
can still be security issues with values we allow a user to enter into the database.

- Normally we expected a user will enter valid information into a field. But an
attacker could try to enter a value that is part of an SQL command to hijack the
query we think we're running and change how it works. This is called SQL injection.


- Proper design of access control, best practices for interacting with data, safety
features offered by programming languages, and proper processing of data that's
entered can all help to secure a database against injection attacks. But hardly a
week goes by when we don't hear of a data breach caused by SQL injection.

- There are automated tools you can run against an app to check for basic injection
attacks. But you should always be mindful of security. It's not something you just
set and forget. It's easy to procrastinate on security, but security should be part
of every step of the design, creation, and ongoing maintenance of your database.

*/