Python MySQL Operations

This Python program demonstrates basic operations with MySQL using the mysql.connector library. It includes functionalities to connect to a MySQL database, create a database, create tables, insert data, retrieve data, update data, and delete data.

-----Installation-----

1. Clone the repository:
git clone https://github.com/Galvesdesousa/python-mysql-operations.git

2. Navigate to the project directory:
cd python-mysql-operations

3. Install the required dependencies:
pip install mysql-connector-python

-----Usage-----

1. Ensure you have a MySQL server installed and running on your machine.
   
2. Configure the database connection parameters in the Python-MySql DB.py file (host, username, password, database name).
   
3. Run the program:
python Python-MySql DB.py

4. Follow the instructions in the console to perform various database operations.

-----Testing-----

To run the test suite, execute the following command:

python test_database.py

The test_database.py file contains unit tests for the database operations implemented in "Python-MySql DB.py." It verifies the functionality and ensures the correctness of the program.

-----Database Schema-----
The program operates on a simple database schema with a single table named customers. The schema of the customers table is as follows:

CREATE TABLE customers (

  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  
  name VARCHAR(255),
  
  address VARCHAR(255)
  
);
