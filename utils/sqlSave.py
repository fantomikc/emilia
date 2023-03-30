import sqlite3
from custom_class.CErrorDialog import CErrorDialog


def sqlSave(path, TABLE):
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE HOST(IP, DOMAIN, NAME, CODE, INTER)")
        table_model = TABLE.model()
        for x in range(table_model.rowCount()):
            data_row = []
            for y in range(table_model.columnCount()):
                index_table = table_model.index(x, y)
                data_row.append(table_model.data(index_table))
            cursor.execute("INSERT INTO HOST VALUES (?, ?, ?, ?, ?)", (data_row[0],
                                                                       data_row[1],
                                                                       data_row[2],
                                                                       data_row[3],
                                                                       data_row[4]))
        connection.commit()
        cursor.close()

    except Exception as exc:
        CErrorDialog(f"{exc}", f"{type(exc)}")
