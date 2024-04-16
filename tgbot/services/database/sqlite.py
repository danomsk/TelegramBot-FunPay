import sqlite3


class Database:

    def __init__(self, path = "E:\Bot\FPBD\FunPay.db"):
        self.path = path

    @property
    def connection(self):
        return sqlite3.connect(self.path)

    def execute(self, sql:str, parameters:tuple=None, fetchone:bool=False, fetchall:bool=False):
        data = None

        connection = self.connection
        cursor = connection.cursor()
        if(parameters == None):
            cursor.execute(sql)
        else:
            cursor.execute(sql, parameters)

        if(fetchone):
            data = cursor.fetchone()

        if(fetchall):
            data = cursor.fetchall()

        cursor.close()
        connection.commit()
        connection.close()

        return data

    def get_acc(self, login, password, game, email, value):
        sql = "INSERT INTO Accounts (loginSteam, passwordSteam, game, email, isUse) VALUES (?, ?, ?, ?, ?)"
        parameters = (login, password, game, email, value)
        self.execute(sql, parameters)

    def get_email(self, login_email, email_password):
        sql = "INSERT INTO Email (emailLogin, emailPassword) VALUES (?, ?)"
        parameters = (login_email, email_password)
        self.execute(sql, parameters)

    def email_id(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT MAX(id) FROM Email")
        email_id = cursor.fetchone()[0]
        cursor.close()

        return email_id

    def get_count_acc(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Accounts")
        acc_count = cursor.fetchone()[0]
        cursor.close()

        return acc_count

    def get_count_hell(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Accounts WHERE game = 1")
        hell_count = cursor.fetchone()[0]
        cursor.close()

        return hell_count

    def get_count_busy_hell(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Accounts WHERE isUse = 1")
        busy_hell_count = cursor.fetchone()[0]
        cursor.close()

        return busy_hell_count