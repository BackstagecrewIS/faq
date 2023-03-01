from sqlalchemy import (
    create_engine, Table, Column, Float,
    ForeignKey, Integer, String, Boolean, MetaData
)

# executing the instructions from our localhost "faq" db
db = create_engine("postgresql:///faq")

meta = MetaData(db)

# create variable for "User" table
user_table = Table(
    "User", meta,
    Column("UserId", Integer, primary_key=True),
    Column("Username", String),
    Column("Password", String),
    Column("Email", String),
    Column("Admin", Boolean),
)

# create variable for "Category" table
category_table = Table(
    "Category", meta,
    Column("CategoryId", Integer, primary_key=True),
    Column("Category", String)
)

# create variable for "Question" table
question_table = Table(
    "Question", meta,
    Column("QuestionId", Integer, primary_key=True),
    Column("CategoryId", Integer, ForeignKey("category_table.CategoryId")),
    Column("Question", String),
    Column("Answer", String),
    Column("AskedBy", Integer, ForeignKey("user_table.UserId")),
    Column("AnsweredBy", Integer, ForeignKey("user_table.UserId")),
)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    select_query = question_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)
