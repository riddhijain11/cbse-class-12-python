import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='bookshop',
                                         user='root',
                                         password='book1234')
    mySql_insert_query = "insert into book (book id , book name , author's name , quantity , price) 
                           VALUES 
                           (108956, 'gulliver"s travels ', " ", '58','135') "

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into  book table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into book table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

