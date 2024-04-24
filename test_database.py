import unittest
import mysql.connector
import time
import threading

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
        
       # Testes Unitários
    def test_unit(self):
        # Testar as funções de manipulação de dados individualmente
        # Defina uma função de manipulação de dados que deseja testar
        def manipulate_data():
            # Simular a função de inserção de dados
            name = "John Doe"
            address = "123 Main St"
            val = (name, address)
            cursor = self.db.cursor()
            sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
            cursor.execute(sql, val)
            self.db.commit()
            return True  # Retorna verdadeiro se a operação for bem-sucedida

        # Chame a função e verifique o resultado
        resultado = manipulate_data()
        self.assertTrue(resultado)  # Verifique se o resultado é verdadeiro
        
       # Testes de Integração
def test_integration(self):
    # Testar a integração entre diferentes partes do sistema

    # Realizar uma série de operações de banco de dados em sequência
    # Por exemplo, inserir dados, atualizar dados e, em seguida, selecionar os dados atualizados

    # Inserir dados de teste
    self.insert_test_data()

    # Atualizar os dados inseridos
    self.update_test_data()

    # Selecionar os dados atualizados e verificar se são os esperados
    updated_data = self.select_updated_data()
    expected_data = [('John Doe', 'Updated Address')]
    self.assertEqual(updated_data, expected_data)

def insert_test_data(self):
    # Função para inserir dados de teste no banco de dados
    sql = "INSERT INTO customers (name, address) VALUES ('John Doe', '123 Main St')"
    self.cursor.execute(sql)
    self.db.commit()

def update_test_data(self):
    # Função para atualizar os dados inseridos no banco de dados
    sql = "UPDATE customers SET address = 'Updated Address' WHERE name = 'John Doe'"
    self.cursor.execute(sql)
    self.db.commit()

def select_updated_data(self):
    # Função para selecionar os dados atualizados do banco de dados
    sql = "SELECT name, address FROM customers WHERE name = 'John Doe'"
    self.cursor.execute(sql)
    return self.cursor.fetchall()

# Testes Funcionais
def test_functional(self):
    # Testar as funcionalidades completas do sistema

    # Simular a inserção de um novo registro
    self.insert_data("John Doe", "123 Main St")

    # Simular a atualização do endereço do registro inserido
    self.update_data("John Doe", "456 Elm St")

    # Simular a exclusão do registro inserido
    self.delete_data("John Doe")

    # Simular a pesquisa por registros inseridos
    search_result = self.search_data("Jane Smith")
    expected_result = [('Jane Smith', '456 Elm St')]
    self.assertEqual(search_result, expected_result)

def insert_data(self, name, address):
    # Função para inserir dados no banco de dados
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name, address)
    self.cursor.execute(sql, val)
    self.db.commit()

def update_data(self, name, new_address):
    # Função para atualizar o endereço de um cliente no banco de dados
    sql = "UPDATE customers SET address = %s WHERE name = %s"
    val = (new_address, name)
    self.cursor.execute(sql, val)
    self.db.commit()

def delete_data(self, name):
    # Função para excluir um cliente do banco de dados
    sql = "DELETE FROM customers WHERE name = %s"
    val = (name,)
    self.cursor.execute(sql, val)
    self.db.commit()

def search_data(self, name):
    # Função para pesquisar clientes com base no nome
    sql = "SELECT name, address FROM customers WHERE name = %s"
    val = (name,)
    self.cursor.execute(sql, val)
    return self.cursor.fetchall()

# Testes de Desempenho
def test_performance(self):
    # Testar partes do sistema quanto ao seu desempenho

    # Medir o tempo de execução da inserção de 1000 registros
    start_time = time.time()
    self.insert_many_data(1000)
    end_time = time.time()

    # Verificar se o tempo de execução está dentro dos limites aceitáveis (por exemplo, 1 segundo)
    execution_time = end_time - start_time
    max_execution_time = 1  # Limite de 1 segundo
    self.assertLessEqual(execution_time, max_execution_time)

def insert_many_data(self, num_records):
    # Função para inserir vários registros no banco de dados
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    values = [("Customer {}".format(i), "Address {}".format(i)) for i in range(1, num_records + 1)]
    self.cursor.executemany(sql, values)
    self.db.commit()
    
   # Teste de Segurança
    def test_security(self):
        # Testar a segurança de partes sensíveis do sistema
        # Por exemplo, verificar se as credenciais de acesso são tratadas de forma segura

        # Verificar se a senha do banco de dados não está sendo exibida no console
        db_password = "ilovemv69"
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password=db_password,
            database="employee_data"
        )
        self.assertNotIn(db_password, repr(db.config()), "Database password is being exposed")
        
         # Teste de Carga
    def test_load(self):
        # Testar o sistema sob carga pesada
        # Por exemplo, enviar uma grande quantidade de solicitações ao sistema e verificar se ele continua funcionando corretamente

        # Função para executar consultas em uma thread separada
        def execute_queries():
            try:
                db = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="ilovemv69",
                    database="employee_data"
                )
                cursor = db.cursor()

                # Execute várias consultas em um loop
                for _ in range(100):
                    cursor.execute("SELECT * FROM customers")
                    cursor.fetchall()

                # Feche a conexão com o banco de dados
                db.close()
            except Exception as e:
                self.fail("Erro durante a execução da consulta: {}".format(e))

        # Crie várias threads para executar as consultas simultaneamente
        threads = []
        for _ in range(10):
            thread = threading.Thread(target=execute_queries)
            threads.append(thread)
            thread.start()

        # Aguarde todas as threads terminarem
        for thread in threads:
            thread.join()




if __name__ == '__main__':
    unittest.main()