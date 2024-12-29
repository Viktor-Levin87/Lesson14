import sqlite3


def initiate_db():
    connection = sqlite3.connect('database_14_5.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL
        )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INT NOT NULL
        )
        ''')
    for i in range(1, 5):
        cursor.execute(''' INSERT INTO Products (title, description, price) VALUES (?, ?, ?) ''',
                       (f'Продукт{i}', f'Описание{i}', i * 100))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database_14_5.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products ')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect('database_14_5.db')
    cursor = connection.cursor()
    cursor.execute('''
            INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)''',
                   (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('database_14_5.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
    connection.commit()
    connection.close()
    if check_user is None:
        return False
    else:
        return True


initiate_db()  # закомментировать после первого запуска
