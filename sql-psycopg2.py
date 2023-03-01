import psycopg2


# connect to "faq" database
connection = psycopg2.connect(database="faq")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "User" table
# cursor.execute('SELECT * FROM "User"')

# Query 2 - select only the "Username" column from the "User" table
# cursor.execute('SELECT "Username" FROM "User"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
