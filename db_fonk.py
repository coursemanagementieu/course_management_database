from sqlite3 import *
# connection supplied
connectDatabase = connect("cms.db")
db_cursor = connectDatabase.cursor()


# All changes will be saved into the database
def save_changes():
    connectDatabase.commit()


# Manage semester table
def insert_semester(name, week):
    try:
        db_cursor.execute("""INSERT INTO semester VALUES(?,?)""", (name, week))
    except IntegrityError:
        print("You have already such a this column.\n")
        select_specific_semester(name)


def select_specific_semester(name):
    db_cursor.execute("""SELECT * FROM semester WHERE name=?""", (name,))
    print(db_cursor.fetchone())


def select_all_semester():
    db_cursor.execute("""SELECT * FROM semester""")
    row = db_cursor.fetchall()
    print(row)


# ---Manage course table---
def insert_course(name, code, book, refbook, syll):
    # Search any line which is matched with given all attributes.
    db_cursor.execute("""SELECT rowid FROM course WHERE name=? AND code=? AND book=? AND referenceBook=? AND 
                         syllabusLink =?""", (name, code, book, refbook, syll))
    # Save the information into row
    row = db_cursor.fetchone()
    # If there is match then ignore insert, if not then add new line with given attributes
    if row is None:
        db_cursor.execute("""INSERT INTO course VALUES (?,?,?,?,?,?)""", (None, name, code, book, refbook, syll))
    else:
        print("You have already such a this column.\n")
        select_specific_course(row[0])


# Select all of the information of line which line ID is matched with given ID from course table
def select_specific_course(ID):
    db_cursor.execute("""SELECT * FROM course WHERE ID=?""", str(ID))
    print(db_cursor.fetchone())


# Select all of the line with it's all of the information from course table
def select_all_course():
    db_cursor.execute("""SELECT * FROM course""")
    row = db_cursor.fetchall()
    print(row)


# ---Manage section table---
def insert_section(classroom, hour, day):
    db_cursor.execute("""SELECT rowid FROM section WHERE classroom=? AND hour=? AND day=?""", (classroom, hour, day))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO section VALUES(?,?,?,?)""", (None, classroom, hour, day))
    else:
        print("You have already such a this column.\n")
        select_specific_section(row[0])


def select_specific_section(ID):
    db_cursor.execute("""SELECT * FROM section WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_section():
    db_cursor.execute("""SELECT * FROM section""")
    row = db_cursor.fetchall()
    print(row)


# ---Manage announcement table---
def insert_announcement(date, head, announcement):
    db_cursor.execute("""SELECT rowid FROM announcement WHERE date=? AND head=? AND announcement=?""",
                      (date, head, announcement))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO announcement VALUES(?,?,?,?)""", (None, date, head, announcement))
    else:
        print("You have already such a this column.\n")
        select_specific_announcement(row[0])


def select_specific_announcement(ID):
    db_cursor.execute("""SELECT * FROM announcement WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_announcement():
    db_cursor.execute("""SELECT * FROM announcement""")
    row = db_cursor.fetchall()
    print(row)


# --Manage subject table---
def insert_subject(sub, ref, week):
    db_cursor.execute("""SELECT rowid FROM subject WHERE subject=? AND reference=? AND week=?""", (sub, ref, week))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO subject VALUES(?,?,?,?)""", (None, sub, ref, week))
    else:
        print("You have already such a this column.\n")
        select_specific_subject(row[0])


def select_specific_subject(ID):
    db_cursor.execute("""SELECT * FROM subject WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_subject():
    db_cursor.execute("""SELECT * FROM subject""")
    row = db_cursor.fetchall()
    print(row)


# ---Manage evaluation table---
def insert_evaluation(name, percentage):
    db_cursor.execute("""SELECT rowid FROM evaluation WHERE name=? AND percentage=?""", (name, percentage))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO evaluation VALUES(?,?,?)""", (None, name, percentage))
    else:
        print("You have already such a this column.\n")
        select_specific_evaluation(row[0])


def select_specific_evaluation(ID):
    db_cursor.execute("""SELECT * FROM evaluation WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_evaluation():
    db_cursor.execute("""SELECT * FROM evaluation""")
    row = db_cursor.fetchall()
    print(row)


# ---Manage student table---
def insert_student(ID, name):
    try:
        db_cursor.execute("""INSERT INTO student VALUES(?,?)""", (ID, name))
    except IntegrityError:
        print("You have already such a this column.\n")
        select_specific_student(ID)


def select_specific_student(ID):
    db_cursor.execute("""SELECT * FROM student WHERE ID=?""", (ID,))
    print(db_cursor.fetchone())


def select_all_student():
    db_cursor.execute("""SELECT * FROM student""")
    row = db_cursor.fetchall()
    print(row)


# ---Manage note table---
def insert_note(head, note, date):
    db_cursor.execute("""SELECT rowid FROM note WHERE head=? AND note=? AND date=?""", (head, note, date))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO note VALUES(?,?,?,?)""", (None, head, note, date))
    else:
        print("You have already such a this column.\n")
        select_specific_note(row[0])


def select_specific_note(ID):
    db_cursor.execute("""SELECT * FROM note WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_note():
    db_cursor.execute("""SELECT * FROM note""")
    row = db_cursor.fetchall()
    print(row)


# Starting manage relation tables
def insert_coursein(semID, cID):
    db_cursor.execute("""INSERT INTO courseIn VALUES(?,?)""", (semID, cID))


def insert_sectionin(semID, cID, secID):
    db_cursor.execute("""INSERT INTO sectionIn VALUES(?,?,?)""", (semID, cID, secID))


def insert_announcementin(semID, cID, annID):
    db_cursor.execute("""INSERT INTO announcementIn VALUES(?,?,?)""", (semID, cID, annID))


def insert_evaluationin(semID, cID, evaID):
    db_cursor.execute("""INSERT INTO evaluationIn VALUES(?,?,?)""", (semID, cID, evaID))


def insert_subjectin(semID, cID, subID):
    db_cursor.execute("""INSERT INTO subjectIn VALUES(?,?,?)""", (semID, cID, subID))


def insert_studentin(semID, cID, secID, stuID):
    db_cursor.execute("""INSERT INTO studentIn VALUES(?,?,?,?)""", (semID, cID, secID, stuID))


def insert_student_evaluationin(semID, cID, evaID, stuID, evaluation):
    db_cursor.execute("""INSERT INTO studentEvaluationIn VALUES (?,?,?,?,?)""", (semID, cID, evaID, stuID, evaluation))


def insert_notein(semID, cID, stuID, nID):
    db_cursor.execute("""INSERT INTO noteIn VALUES (?,?,?,?)""", (semID, cID, stuID, nID))
