import sqlite3
from os.path import join, isfile

DATABASE_PATH = 'animal.db'
SQL_DIR_PATH = 'sql'
INIT_MIGRATION_FILE_PATH = 'init.sql'
DATE_MIGRATION_FILE_PATH = 'migration.sql'


def get_sql_from_file(file_name):
    """
    Получает чистый SQL из файла
    :param file_name: полный путь до файла.
    :return: Строка с запросами
    """
    content = ''
    if isfile(file_name):
        with open(file_name) as file:
            content = file.read()
    return content


def main():
    """
    Основная функция, выполняет миграцию данных
    """

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Создаем структуру базы данных
    init_sql = get_sql_from_file(join(SQL_DIR_PATH, INIT_MIGRATION_FILE_PATH))
    cursor.executescript(init_sql)

    # Заполняем данными.
    date_sql = get_sql_from_file(join(SQL_DIR_PATH, DATE_MIGRATION_FILE_PATH))
    cursor.executescript(date_sql)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
