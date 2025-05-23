from loguru import logger
import sqlite3

connection = sqlite3.connect("history.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    primer TEXT NOT NULL
)
''')

# Готово только создание самой таблицы и то возможно она изменится, т.к. 
# картинка, как это должно работать не появилась...
# Да я делал это долго, но мне просто дали задачу которую я вообще не знаю
# как её реализовать, это как дизайнеру сказали починить кран....
# Но я честно исправлюсь, и изучу инфу на эту тему.
