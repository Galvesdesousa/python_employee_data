import unittest
import mysql.connector

class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        # Configurar a conexão com o banco de dados
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="ilovemv69",
            database="employee_data"
        )
        self.cursor = self.db.cursor()

    def tearDown(self):
        # Fechar a conexão com o banco de dados após cada teste
        self.db.close()

    def test_create_record(self):
        # Testar a criação de um registro e verificar se os dados estão corretos
        sql = "INSERT INTO customers (name, address) VALUES ('John Doe', '123 Main St')"
        self.cursor.execute(sql)
        self.db.commit()

        # Verificar se o registro foi criado corretamente
        self.assertEqual(self.cursor.rowcount, 1)

        # Verificar se os dados do registro correspondem ao esperado
        sql = "SELECT name, address FROM customers WHERE customer_id = %s"
        self.cursor.execute(sql, (self.cursor.lastrowid,))
        result = self.cursor.fetchone()
        self.assertEqual(result, ('John Doe', '123 Main St'))

    def test_duplicate_id(self):
        # Testar a criação de um registro com um ID duplicado
        sql = "INSERT INTO customers (customer_id, name, address) VALUES (1, 'Jane Smith', '456 Elm St')"

        # Executar a consulta SQL
        self.cursor.execute(sql)
        self.db.commit()

        # Verificar se a exceção IntegrityError é levantada
        with self.assertRaises(mysql.connector.errors.IntegrityError):
            self.cursor.execute(sql)
            self.db.commit()

    def test_delete_existing_record(self):
        # Testar a exclusão de um registro existente
        sql = "DELETE FROM customers WHERE customer_id = 1"
        self.cursor.execute(sql)
        self.db.commit()

        # Verificar se o registro foi excluído corretamente
        self.assertEqual(self.cursor.rowcount, 1)

    def test_delete_non_existing_record(self):
        # Testar a exclusão de um registro inexistente
        sql = "DELETE FROM customers WHERE customer_id = 1000"  # Garantir que não haja registros com esse ID
        self.cursor.execute(sql)
        self.db.commit()

        # Verificar se nenhum registro foi excluído
        self.assertEqual(self.cursor.rowcount, 0)

    def test_insert_multiple_records(self):
        # Testar a inserção de 10 registros
        data = [
            ('Alice', '789 Oak St'),
            ('Bob', '101 Pine St'),
            ('Carol', '202 Maple St'),
            ('Dave', '303 Cedar St'),
            ('Eve', '404 Walnut St'),
            ('Frank', '505 Birch St'),
            ('Grace', '606 Spruce St'),
            ('Henry', '707 Fir St'),
            ('Ivy', '808 Chestnut St'),
            ('Jack', '909 Willow St')
        ]

        sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        self.cursor.executemany(sql, data)
        self.db.commit()

        # Verificar se os registros foram inseridos corretamente
        self.assertEqual(self.cursor.rowcount, 10)


if __name__ == '__main__':
    unittest.main()