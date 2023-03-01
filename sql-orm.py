from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String, Boolean
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///faq")
base = declarative_base()


# create a class-based model for the "User" table
class User(base):
    __tablename__ = "User"
    UserId = Column(Integer, primary_key=True)
    Username = Column(String)
    Password = Column(String)
    Email = Column(String)
    Admin = Column(Boolean)


# create a class-based model for the "Category" table
class Category(base):
    __tablename__ = "Category"
    CategoryId = Column(Integer, primary_key=True)
    Category = Column(String)


# create a class-based model for the "Question" table
class Question(base):
    __tablename__ = "Question"
    QuestionId = Column(Integer, primary_key=True)
    CategoryId = Column(Integer, ForeignKey("Category.CategoryId"))
    Question = Column(String)
    Answer = Column(String)
    AskedBy = Column(Integer, ForeignKey("User.UserId"))
    AnsweredBy = Column(Integer, ForeignKey("User.UserId"))


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "User" table
# users = session.query(User)
# for user in users:
#     print(user.UserId, user.Username, sep=" | ")

# Query 2 - select question where the AskedBy is "Admin" from "Question" table
questions = session.query(Question).filter_by(AskedBy=1)
for question in questions:
    print(
        question.QuestionId,
        question.Question,
        question.Answer,
        sep=" | "
    )
