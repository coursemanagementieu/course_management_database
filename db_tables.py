from sqlite3 import *

connectDatabase = connect("cms.db")
db_cursor = connectDatabase.cursor()

# Entity tables


def create_entity_tables():
    # Semester table declared
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS semester(
                         name text PRIMARY KEY,
                         week text
                         )WITHOUT ROWID""")
    # Course table declared
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS course(
                         ID integer PRIMARY KEY,
                         name text,
                         code text,
                         book text,
                         referenceBook text,
                         syllabusLink text
                         )""")
    # Section table declared
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS section(
                         ID integer PRIMARY KEY,
                         classroom text,
                         hour text,
                         day text
                         )""")
    # Announcement table declared
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS announcement(
                         ID integer PRIMARY KEY,
                         date text,
                         head text,
                         announcement text
                         )""")
    # Subject table declared
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS subject(
                         ID integer PRIMARY KEY,
                         subject text,
                         reference text,
                         week text
                         )""")
    # Evaluation table declared
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS evaluation(
                         ID integer PRIMARY KEY,
                         name text,
                         percentage integer
                         )""")
    # Student table declared
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS student(
                         ID text PRIMARY KEY,
                         name text
                         ) WITHOUT ROWID""")
    # Note table declared
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS note(
                         ID integer PRIMARY KEY,
                         head text,
                         note text,
                         date text
                         )""")
# Create relation tables


def create_relation_tables():
    # Semester - Course relationship
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS courseIn(
                         semesterID text,
                         courseID integer,
                         FOREIGN KEY (semesterID)
                         REFERENCES semester(name)
                         ON UPDATE CASCADE 
                         ON DELETE CASCADE,
                         FOREIGN KEY (courseID) 
                         REFERENCES course(ID) 
                         ON UPDATE CASCADE 
                         ON DELETE CASCADE                     
                         )""")
    # Semester - Course - Section relationship
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS sectionIn(
                         semesterID text REFERENCES semester(name) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         courseID integer REFERENCES course(ID) ON UPDATE CASCADE ON DELETE CASCADE,
                         sectionID integer REFERENCES section(ID) ON UPDATE CASCADE ON DELETE CASCADE
                         )""")
    # Semester - Course - Announcement relationship
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS announcementIn(
                         semesterID text REFERENCES semester(name) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         courseID integer REFERENCES course(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         announcementID integer REFERENCES announcement(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE
                         )""")

    # Semester - Course - Evaluation relationship
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS evaluationIn(
                         semesterID text REFERENCES semester(name) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         courseID integer REFERENCES course(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         evaluationID integer REFERENCES evaluation(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE
                         )""")

    # Semester - Course - Subject relationship
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS subjectIn(
                         semesterID text REFERENCES semester(name) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         courseID integer REFERENCES course(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         subjectID integer REFERENCES subject(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE
                         )""")

    # Semester - Course - Section - Student relationship
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS studentIn(
                         semesterID text REFERENCES semester(name) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         courseID integer REFERENCES course(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         sectionID integer REFERENCES section(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         studentID text REFERENCES student(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE
                         )""")

    # Semester - Course - Evaluation - Student relationship
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS studentEvaluationIn(
                         semesterID text REFERENCES semester(name) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         courseID integer REFERENCES course(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         evaluationID integer REFERENCES evaluation(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         studentID text REFERENCES student(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         evaluation double
                         )""")

    # Semester - Course - Student - Note relationship
    db_cursor.execute("""CREATE TABLE IF NOT EXISTS noteIn(
                         semesterID text REFERENCES semester(name) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         courseID integer REFERENCES course(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         studentID text REFERENCES student(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE,
                         noteID integer REFERENCES note(ID) ON UPDATE CASCADE
                         ON DELETE CASCADE
                         )""")
