# Task 4.1

## Part 1

### 3. Select a subject area and describe the database schema, (minimum 3 tables)

My subject area is electronics store. I have 3 tables: for users, phones and orders.

The users table with contents example:

| id | email              | password                                                         | city | is_admin |
|----|--------------------|------------------------------------------------------------------|------|----------|
| 1  | example1@gmail.com | 49c7f17bd6e02132099260a1b0a448b8bbb56d466d9756c6cd9bf3b717593a58 | Kiyv | 1        |
| 2  | example2@gmail.com | 382c36b3cff1836160f5fb9f313372c9aa504b6de92369f3ac0f6e00eded0ba1 | Kiyv | 0        |
| 3  | example3@gmail.com | 65d4e36d4ffafc369c4528e85f93579fa7a26f7812ecb0ffc65f7864310919c0 | Lviv | 0        |

The products table:

| id | chassis | label                                                             | panel_resolution | cpu                      | ram | rom | price |
|----|---------|-------------------------------------------------------------------|------------------|--------------------------|-----|-----|-------|
| 1  | handset | Samsung Galaxy S21 Ultra 12/128GB Phantom Silver (SM-G998BZSDSEK) | 3200x1440        | Samsung Exynos 2100      | 12  | 128 | 30000 |
| 2  | handset | Apple iPhone 13 Pro 128GB Sierra Blue (MLVD3)                     | 2532x1170        | Apple A15 Bionic         | 6   | 128 | 38500 |
| 3  | tablet  | Samsung Galaxy Tab S7 FE LTE 4/64Gb Black (SM-T735NZKASEK)        | 2560x1600        | Qualcomm Snapdragon 750G | 4   | 64  | 15500 |

The orders table:

| id | user_id | product_id |
|----|---------|------------|
| 1  | 2       | 1          |
| 2  | 3       | 2          |
| 3  | 2       | 3          |
 
### 4. Create a database on the server through the console.

```sql
mysql> CREATE DATABASE store;
Query OK, 1 row affected (1.62 sec)

mysql> USE store;
Database changed

mysql> CREATE TABLE users(id MEDIUMINT NOT NULL AUTO_INCREMENT, email TEXT(320) NOT NULL, password TEXT(255) NOT NULL, city CHAR(120) NOT NULL, is_admin TINYINT NOT NULL,PRIMARY KEY(id));
Query OK, 0 rows affected (6.27 sec)

mysql> CREATE TABLE products(id MEDIUMINT NOT NULL AUTO_INCREMENT, chassis CHAR(20) NOT NULL,label CHAR(150) NOT NULL, panel_resolution CHAR(30) NOT NULL, cpu CHAR(50) NOT NULL, ram SMALLINT NOT NULL, rom SMALLINT NOT NULL, price MEDIUMINT NOT NULL, PRIMARY KEY(id));
Query OK, 0 rows affected (6.33 sec)

mysql> CREATE TABLE orders(id MEDIUMINT NOT NULL AUTO_INCREMENT, user_id MEDIUMINT NOT NULL, product_id MEDIUMINT NOT NULL, INDEX(product_id), INDEX(user_id), PRIMARY KEY(id), FOREIGN KEY(user_id) REFERENCES users(id), FOREIGN KEY(product_id) REFERENCES products(id));
Query OK, 0 rows affected (9.64 sec)
```

### 5. Fill in tables.

```sql
mysql> INSERT INTO users(email, password, city, is_admin) VALUES ('example1@gmail.com', '49c7f17bd6e02132099260a1b0a448b8bbb56d466d9756c6cd9bf3b717593a58', 'Kiyv', 1), ('example2@gmail.com', '382c36b3cff1836160f5fb9f313372c9aa504b6de92369f3ac0f6e00eded0ba1', 'Kiyv', 0), ('example3@gmail.com', '65d4e36d4ffafc369c4528e85f93579fa7a26f7812ecb0ffc65f7864310919c0', 'Lviv', 0);
Query OK, 3 rows affected (1.78 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> INSERT INTO products(chassis, label, panel_resolution, cpu, ram, rom, price) VALUES  ('handset', 'Samsung Galaxy S21 Ultra 12/128GB Phantom Silver (SM-G998BZSDSEK)', '3200x1440', 'Samsung Exynos 2100', 12, 128, 30000), ('handset', 'Apple iPhone 13 Pro 128GB Sierra Blue (MLVD3)', '2532x1170', 'Apple A15 Bionic', 6, 128, 38500), ('tablet', 'Samsung Galaxy Tab S7 FE LTE 4/64Gb Black (SM-T735NZKASEK)', '2560x1600', 'Qualcomm Snapdragon 750G', 4, 64, 15500);
Query OK, 3 rows affected (1.58 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> INSERT INTO orders(user_id, product_id) VALUES (2, 1), (3, 2), (2, 3);
Query OK, 3 rows affected (1.50 sec)
Records: 3  Duplicates: 0  Warnings: 0
```

### 6. Construct and execute SELECT operator with WHERE, GROUP BY and ORDER BY.

```sql
mysql> SELECT label FROM products WHERE chassis = 'handset';
+-------------------------------------------------------------------+
| label                                                             |
+-------------------------------------------------------------------+
| Samsung Galaxy S21 Ultra 12/128GB Phantom Silver (SM-G998BZSDSEK) |
| Apple iPhone 13 Pro 128GB Sierra Blue (MLVD3)                     |
+-------------------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> SELECT label FROM products GROUP BY id;
+-------------------------------------------------------------------+
| label                                                             |
+-------------------------------------------------------------------+
| Samsung Galaxy S21 Ultra 12/128GB Phantom Silver (SM-G998BZSDSEK) |
| Apple iPhone 13 Pro 128GB Sierra Blue (MLVD3)                     |
| Samsung Galaxy Tab S7 FE LTE 4/64Gb Black (SM-T735NZKASEK)        |
+-------------------------------------------------------------------+
3 rows in set (0.00 sec)

mysql> SELECT label, ram, rom, price FROM products ORDER BY ram;
+-------------------------------------------------------------------+-----+-----+-------+
| label                                                             | ram | rom | price |
+-------------------------------------------------------------------+-----+-----+-------+
| Samsung Galaxy Tab S7 FE LTE 4/64Gb Black (SM-T735NZKASEK)        |   4 |  64 | 30000 |
| Apple iPhone 13 Pro 128GB Sierra Blue (MLVD3)                     |   6 | 128 | 38500 |
| Samsung Galaxy S21 Ultra 12/128GB Phantom Silver (SM-G998BZSDSEK) |  12 | 128 | 15500 |
+-------------------------------------------------------------------+-----+-----+-------+
3 rows in set (0.00 sec)
```

### 7. Execute other different SQL queries DDL, DML, DCL.

```sql
mysql> UPDATE products SET price = 15499 WHERE id = 3;
Query OK, 1 row affected (0.53 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

### 8. Create a database of new users with different privileges. Connect to the databaseas a new user and verify that the privileges allow or deny certain actions.

```sql
mysql> CREATE USER 'reader'@'localhost' IDENTIFIED BY '12345';
Query OK, 0 rows affected (0.97 sec)

mysql> GRANT SELECT on *.* TO 'reader'@'localhost';
Query OK, 0 rows affected (1.35 sec)

mysql> CREATE USER 'writer'@'localhost' IDENTIFIED BY '54321';
Query OK, 0 rows affected (1.58 sec)

mysql> GRANT SELECT, UPDATE, INSERT on *.* TO 'writer'@'localhost';
Query OK, 0 rows affected (1.03 sec)

mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY '12121';
Query OK, 0 rows affected (0.84 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
Query OK, 0 rows affected (0.50 sec)

mysql> ^DBye
user@pc-vm:~$ mysql -u reader -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> USE store;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SELECT * FROM orders; -- should work
+----+---------+------------+
| id | user_id | product_id |
+----+---------+------------+
|  1 |       2 |          1 |
|  2 |       3 |          2 |
|  3 |       2 |          3 |
+----+---------+------------+
3 rows in set (0.00 sec)

mysql> DROP TABLE orders; -- should not work
ERROR 1142 (42000): DROP command denied to user 'reader'@'localhost' for table 'orders'
```

### 9. Make a selection from the main table DB MySQL.

```sql
mysql> USE mysql
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SELECT * FROM global_grants WHERE user = 'root';
+------+-----------+-----------------------------+-------------------+
| USER | HOST      | PRIV                        | WITH_GRANT_OPTION |
+------+-----------+-----------------------------+-------------------+
| root | localhost | APPLICATION_PASSWORD_ADMIN  | Y                 |
| root | localhost | AUDIT_ADMIN                 | Y                 |
| root | localhost | AUTHENTICATION_POLICY_ADMIN | Y                 |
| root | localhost | BACKUP_ADMIN                | Y                 |
| root | localhost | BINLOG_ADMIN                | Y                 |
| root | localhost | BINLOG_ENCRYPTION_ADMIN     | Y                 |
| root | localhost | CLONE_ADMIN                 | Y                 |
| root | localhost | CONNECTION_ADMIN            | Y                 |
| root | localhost | ENCRYPTION_KEY_ADMIN        | Y                 |
| root | localhost | FLUSH_OPTIMIZER_COSTS       | Y                 |
| root | localhost | FLUSH_STATUS                | Y                 |
| root | localhost | FLUSH_TABLES                | Y                 |
| root | localhost | FLUSH_USER_RESOURCES        | Y                 |
| root | localhost | GROUP_REPLICATION_ADMIN     | Y                 |
| root | localhost | GROUP_REPLICATION_STREAM    | Y                 |
| root | localhost | INNODB_REDO_LOG_ARCHIVE     | Y                 |
| root | localhost | INNODB_REDO_LOG_ENABLE      | Y                 |
| root | localhost | PASSWORDLESS_USER_ADMIN     | Y                 |
| root | localhost | PERSIST_RO_VARIABLES_ADMIN  | Y                 |
| root | localhost | REPLICATION_APPLIER         | Y                 |
| root | localhost | REPLICATION_SLAVE_ADMIN     | Y                 |
| root | localhost | RESOURCE_GROUP_ADMIN        | Y                 |
| root | localhost | RESOURCE_GROUP_USER         | Y                 |
| root | localhost | ROLE_ADMIN                  | Y                 |
| root | localhost | SERVICE_CONNECTION_ADMIN    | Y                 |
| root | localhost | SESSION_VARIABLES_ADMIN     | Y                 |
| root | localhost | SET_USER_ID                 | Y                 |
| root | localhost | SHOW_ROUTINE                | Y                 |
| root | localhost | SYSTEM_USER                 | Y                 |
| root | localhost | SYSTEM_VARIABLES_ADMIN      | Y                 |
| root | localhost | TABLE_ENCRYPTION_ADMIN      | Y                 |
| root | localhost | XA_RECOVER_ADMIN            | Y                 |
+------+-----------+-----------------------------+-------------------+
32 rows in set (0.00 sec)
```
