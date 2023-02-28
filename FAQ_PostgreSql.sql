
/*******************************************************************************
   FAQ Database - Version 1.0
   Script: FAQ_PostgreSql.sql
   Description: Creates and populates the FAQ database.
   DB Server: PostgreSql
   Author: David Jones
   License: FREE
********************************************************************************/


/*******************************************************************************
   Create Tables
********************************************************************************/
CREATE TABLE "Category"
(
    "CategoryId" INT NOT NULL,
    "Category" VARCHAR(25) NOT NULL,
    CONSTRAINT "PK_Category" PRIMARY KEY  ("CategoryId")
);

CREATE TABLE "Question"
(
    "QuestionId" INT NOT NULL,
    "CategoryId" INT NOT NULL,
    "Question" VARCHAR(150) NOT NULL,
    "Answer" VARCHAR(255) NOT NULL,
    "AskedBy" INT NOT NULL,
    "AnsweredBy" INT NOT NULL,
    CONSTRAINT "PK_Question" PRIMARY KEY  ("QuestionId")
);

CREATE TABLE "User"
(
    "UserId" INT NOT NULL,
    "Username" VARCHAR(25) NOT NULL,
    "Password" VARCHAR(110) NOT NULL,
    "Email" VARCHAR(25) NOT NULL,
    "Admin" BOOLEAN NOT NULL,
    CONSTRAINT "PK_User" PRIMARY KEY  ("UserId")
);

/*******************************************************************************
   Create Primary Key Unique Indexes
********************************************************************************/

/*******************************************************************************
   Create Foreign Keys
********************************************************************************/

ALTER TABLE "Question" ADD CONSTRAINT "FK_QuestionCategory"
    FOREIGN KEY ("CategoryId") REFERENCES "Category" ("CategoryId") ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX "IFK_QuestionCategoryId" ON "Question" ("CategoryId");

ALTER TABLE "Question" ADD CONSTRAINT "FK_QuestionAskedBy"
    FOREIGN KEY ("AskedBy") REFERENCES "User" ("UserId") ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX "IFK_QuestionAskedBy" ON "Question" ("AskedBy");

ALTER TABLE "Question" ADD CONSTRAINT "FK_QuestionAnsweredBy"
    FOREIGN KEY ("AnsweredBy") REFERENCES "User" ("UserId") ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX "IFK_QuestionAnsweredBy" ON "Question" ("AnsweredBy");

/*******************************************************************************
   Populate Tables
********************************************************************************/
INSERT INTO "User" ("UserId", "Username", "Password", "Email", "Admin") VALUES (1, 'Admin', 'Password', 'email@test.com', TRUE);

INSERT INTO "Category" ("CategoryId", "Category") VALUES (1, 'Pricing');
INSERT INTO "Category" ("CategoryId", "Category") VALUES (2, 'Hosting');

INSERT INTO "Question" ("QuestionId", "CategoryId", "Question", "Answer", "AskedBy", "AnsweredBy") VALUES (1, 1, 'How much is a basic website', 'Prices start from £250', 1, 1);