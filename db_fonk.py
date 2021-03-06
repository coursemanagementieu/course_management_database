from sqlite3 import *
# connection supplied
connectDatabase = connect("cms.db")
connectDatabase.execute('pragma foreign_keys=ON')
db_cursor = connectDatabase.cursor()


# All changes will be saved into the database
def save_changes():
    connectDatabase.commit()


# Manage semester table
def insert_semester(name, week="Empty"):
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


def edit_semester(name, week):
    db_cursor.execute("""SELECT week FROM semester WHERE name=?""", (name,))
    row = db_cursor.fetchone()

    if row is not row[0]:
        db_cursor.execute("""UPDATE semester SET week=? WHERE name=?""", (week, name))


def delete_semester(name):
    db_cursor.execute("""DELETE FROM semester WHERE name=?""", (name,))


# ---Manage course table---
# Add new course in course table and return with it's rowid
def insert_course(name="Empty", code="Empty", book="Empty", refbook="Empty", syll="Empty"):
    # If there is match then ignore insert, if not then add new line with given attributes
    row = find_course_rowid(name, code, book, refbook, syll)
    if row is None:
        db_cursor.execute("""INSERT INTO course VALUES (?,?,?,?,?,?)""", (None, name, code, book, refbook, syll))
        row = find_course_rowid(name, code, book, refbook, syll)
        return row[0]
    else:
        print("You have already such a this column.\n")
        select_specific_course(row[0])
        return row[0]


# attached rowid with given attributes
def find_course_rowid(name="Empty", code="Empty", book="Empty", refbook="Empty", syll="Empty"):
    # Search any line which is matched with given all attributes.
    db_cursor.execute("""SELECT rowid FROM course WHERE name=? AND code=? AND book=? AND referenceBook=? AND 
                             syllabusLink =?""", (name, code, book, refbook, syll))
    # Save the information into row
    row = db_cursor.fetchone()
    return row


# Select rowid
def select_course_rowid(semID, code):
    db_cursor.execute("""SELECT ID FROM course WHERE code=? AND ID IN (SELECT courseID
                                                                       FROM courseIn
                                                                       WHERE semesterID=?)""", (code, semID))
    row = db_cursor.fetchone()
    return row[0]


def edit_course(ID, name="Empty", code="Empty", book="Empty", refbook="Empty", syll="Empty"):
    db_cursor.execute("""SELECT name, code, book, referenceBook, syllabusLink FROM course WHERE rowid=?""", str(ID))
    row = db_cursor.fetchone()

    if name is not row[0]:
        db_cursor.execute("""UPDATE course SET name=? WHERE rowid=?""", (name, ID))

    if code is not row[1]:
        db_cursor.execute("""UPDATE course SET code=? WHERE rowid=?""", (code, ID))

    if book is not row[2]:
        db_cursor.execute("""UPDATE course SET book=? WHERE rowid=?""", (book, ID))

    if refbook is not row[3]:
        db_cursor.execute("""UPDATE course SET referenceBook=? WHERE rowid=?""", (refbook, ID))

    if syll is not row[4]:
        db_cursor.execute("""UPDATE course SET syllabusLink=? WHERE rowid=?""", (syll, ID))


# Select all of the information of line which line ID is matched with given ID from course table
def select_specific_course(ID):
    db_cursor.execute("""SELECT * FROM course WHERE ID=?""", str(ID))
    print(db_cursor.fetchone())


# Select all of the line with it's all of the information from course table
def select_all_course():
    db_cursor.execute("""SELECT * FROM course""")
    row = db_cursor.fetchall()
    print(row)


def delete_course(ID):
    db_cursor.execute("""DELETE FROM course WHERE rowid=?""", str(ID))


# ---Manage section table---
def insert_section(name="Empty", classroom="Empty", hour="Empty", day="Empty"):
    # db_cursor.execute("""SELECT * FROM section WHERE name=?""", (name,))
    # duplicateName = db_cursor.fetchone()
    # if duplicateName is not None:
    #     print("Can not created! You have already this name.")
    #     return 0
    row = find_section_rowid(name, classroom, hour, day)
    if row is None:
        db_cursor.execute("""INSERT INTO section VALUES(?,?,?,?,?)""", (None, name, classroom, hour, day))
        row = find_section_rowid(name, classroom, hour, day)
        return row[0]
    else:
        print("You have already such a this column.\n")
        select_specific_section(row[0])
        return row[0]


def find_section_rowid(name="Empty", classroom="Empty", hour="Empty", day="Empty"):
    db_cursor.execute("""SELECT rowid FROM section WHERE name=? AND classroom=? AND hour=? AND day=?""",
                      (name, classroom, hour, day))
    row = db_cursor.fetchone()
    return row


def select_section_rowid(semID, cID, name):
    db_cursor.execute("""SELECT ID FROM section WHERE name=? AND ID IN (SELECT sectionID
                                                                     FROM sectionIn
                                                                     WHERE semesterID=? AND courseID=?)""",
                      (name, semID, cID))

    row = db_cursor.fetchone()
    return row[0]


def edit_section(ID, name="Empty", classroom="Empty", hour="Empty", day="Empty"):
    db_cursor.execute("""SELECT name, classroom, hour, day FROM section WHERE rowid=?""", str(ID))
    row = db_cursor.fetchone()

    if name is not row[0]:
        db_cursor.execute("""UPDATE section SET name=? WHERE rowid=?""", (name, ID))

    if classroom is not row[1]:
        db_cursor.execute("""UPDATE section SET classroom=? WHERE rowid=?""", (classroom, ID))

    if hour is not row[2]:
        db_cursor.execute("""UPDATE section SET hour=? WHERE rowid=?""", (hour, ID))

    if day is not row[3]:
        db_cursor.execute("""UPDATE section SET day=? WHERE rowid=?""", (day, ID))


def select_specific_section(ID):
    db_cursor.execute("""SELECT * FROM section WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_section():
    db_cursor.execute("""SELECT * FROM section""")
    row = db_cursor.fetchall()
    print(row)


def delete_section(ID):
    db_cursor.execute("""DELETE FROM section WHERE rowid=?""", str(ID))


# ---Manage announcement table---
def insert_announcement(date="Empty", head="Empty", announcement="Empty"):
    # # Since we will find announcement rowid thanks to semesterID, courseID and head of it, one tuple should be unique.
    # # Since semesterID and courseID can be same, if semesterID and courseID is same then head shall be different
    # db_cursor.execute("""SELECT * FROM announcement WHERE head=?""", (head,))
    # duplicateHead = db_cursor.fetchone()
    # if duplicateHead is not None:
    #     print("You cannot create this announcement, because you had already using same head.")
    #     return 0
    row = find_announcement_rowid(date, head, announcement)
    if row is None:
        db_cursor.execute("""INSERT INTO announcement VALUES(?,?,?,?)""", (None, date, head, announcement))
        row = find_announcement_rowid(date,head,announcement)
        return row[0]
    else:
        print("You have already such a this column.\n")
        select_specific_announcement(row[0])
        return row[0]


def find_announcement_rowid(date="Empty", head="Empty", announcement="Empty"):
    db_cursor.execute("""SELECT rowid FROM announcement WHERE date=? AND head=? AND announcement=?""",
                      (date, head, announcement))
    row = db_cursor.fetchone()
    return row


def select_announcement_rowid(semID, cID, head):
    db_cursor.execute("""SELECT ID FROM announcement WHERE head=? AND ID IN (SELECT announcementID FROM announcementIn 
                                                                          WHERE semesterID=? AND courseID=?)""",

                      (head, semID, cID))
    row = db_cursor.fetchone()
    return row[0]


def edit_announcement(ID, date="Empty", head="Empty", announcement="Empty"):
    db_cursor.execute("""SELECT date, head, announcement FROM announcement WHERE rowid=?""", str(ID))
    row = db_cursor.fetchone()

    if date is not row[0]:
        db_cursor.execute("""UPDATE announcement SET date=? WHERE rowid=?""", (date, ID))

    if head is not row[1]:
        db_cursor.execute("""UPDATE announcement SET head=? WHERE rowid=?""", (head, ID))

    if announcement is not row[2]:
        db_cursor.execute("""UPDATE announcement SET announcement=? WHERE rowid=?""", (announcement, ID))


def select_specific_announcement(ID):
    db_cursor.execute("""SELECT * FROM announcement WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_announcement():
    db_cursor.execute("""SELECT * FROM announcement""")
    row = db_cursor.fetchall()
    print(row)


def delete_announcement(ID):
    db_cursor.execute("""DELETE FROM announcement WHERE rowid=?""", str(ID))


# --Manage subject table---
def insert_subject(sub="Empty", ref="Empty", week="Empty"):
    row = find_subject_rowid(sub,ref,week)
    if row is None:
        db_cursor.execute("""INSERT INTO subject VALUES(?,?,?,?)""", (None, sub, ref, week))
        row = find_subject_rowid(sub, ref, week)
        return row[0]
    else:
        print("You have already such a this column.\n")
        select_specific_subject(row[0])
        return row[0]


def find_subject_rowid(sub="Empty", ref="Empty", week="Empty"):
    db_cursor.execute("""SELECT rowid FROM subject WHERE subject=? AND reference=? AND week=?""", (sub, ref, week))
    row = db_cursor.fetchone()
    return row


def select_subject_rowid(semID, cID, week):
    db_cursor.execute("""SELECT ID FROM subject WHERE week=? AND ID IN (SELECT subjectID 
                                                                        FROM subjectIn 
                                                                        WHERE semesterID=? AND courseID=?)""",
                      (week, semID, cID))
    row = db_cursor.fetchone()
    return row[0]


def edit_subject(ID, sub="Empty", ref="Empty", week="Empty"):
    db_cursor.execute("""SELECT subject, reference, week FROM subject WHERE rowid=?""", str(ID))
    row = db_cursor.fetchone()

    if sub is not row[0]:
        db_cursor.execute("""UPDATE subject SET subject=? WHERE rowid=?""", (sub, ID))

    if ref is not row[1]:
        db_cursor.execute("""UPDATE subject SET reference=? WHERE rowid=?""", (ref, ID))

    if week is not row[2]:
        db_cursor.execute("""UPDATE subject SET week=? WHERE rowid=?""", (week, ID))


def select_specific_subject(ID):
    db_cursor.execute("""SELECT * FROM subject WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_subject():
    db_cursor.execute("""SELECT * FROM subject""")
    row = db_cursor.fetchall()
    print(row)


def delete_subject(ID):
    db_cursor.execute("""DELETE FROM subject WHERE rowid=?""", str(ID))


# ---Manage evaluation table---
def insert_evaluation(name="Empty", percentage="Empty"):
    row = find_evaluation_rowid(name, percentage)
    if row is None:
        db_cursor.execute("""INSERT INTO evaluation VALUES(?,?,?)""", (None, name, percentage))
        row = find_evaluation_rowid(name, percentage)
        return row[0]
    else:
        print("You have already such a this column.\n")
        select_specific_evaluation(row[0])
        return row[0]


def find_evaluation_rowid(name="Empty", percentage="Empty"):
    db_cursor.execute("""SELECT rowid FROM evaluation WHERE name=? AND percentage=?""", (name, percentage))
    row = db_cursor.fetchone()
    return row


def select_evaluiaton_rowid(semID, cID, name):
    db_cursor.execute("""SELECT ID FROM evaluation WHERE name=? AND ID IN (SELECT evaluationID 
                                                                           FROM evaluationIn 
                                                                           WHERE semesterID=? AND courseID=?)""",
                      (name, semID, cID))
    row = db_cursor.fetchone()
    return row[0]


def edit_evaluation(ID, name="Empty", percentage="Empty"):
    db_cursor.execute("""SELECT name, percentage FROM evaluation WHERE rowid=?""", str(ID))
    row = db_cursor.fetchone()

    if name is not row[0]:
        db_cursor.execute("""UPDATE evaluation SET name=? WHERE rowid=?""", (name, ID))

    if percentage is not row[1]:
        db_cursor.execute("""UPDATE evaluation SET percentage=? WHERE rowid=?""", (percentage, ID))


def select_specific_evaluation(ID):
    db_cursor.execute("""SELECT * FROM evaluation WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_evaluation():
    db_cursor.execute("""SELECT * FROM evaluation""")
    row = db_cursor.fetchall()
    print(row)


def delete_evaluation(ID):
    db_cursor.execute("""DELETE FROM evaluation WHERE rowid=?""", str(ID))

# ---Manage student table---
def insert_student(ID, name="Empty"):
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


def edit_student(ID, name="Empty"):
    db_cursor.execute("""SELECT name FROM student WHERE ID=?""", (ID,))
    row = db_cursor.fetchone()

    if name is not row[0]:
        db_cursor.execute("""UPDATE student SET name=? WHERE ID=?""", (name, ID))


def delete_student(ID):
    db_cursor.execute("""DELETE FROM student WHERE ID=?""", (ID,))


# ---Manage note table---
def insert_note(head="Empty", note="Empty", date="Empty"):
    row = find_note_rowid(head,note,date)
    if row is None:
        db_cursor.execute("""INSERT INTO note VALUES(?,?,?,?)""", (None, head, note, date))
        row = find_note_rowid(head, note, date)
        return row[0]
    else:
        print("You have already such a this column.\n")
        select_specific_note(row[0])
        return row[0]


def find_note_rowid(head="Empty", note="Empty", date="Empty"):
    db_cursor.execute("""SELECT rowid FROM note WHERE head=? AND note=? AND date=?""", (head, note, date))
    row = db_cursor.fetchone()
    return row


def select_note_rowid(semID, cID, stuID, head):
    db_cursor.execute("""SELECT ID FROM note WHERE head=? AND ID IN (SELECT noteID 
                                                                     FROM noteIn 
                                                                     WHERE semesterID=? AND courseID=? 
                                                                     AND studentID=?)""", (head, semID, cID, stuID))
    row = db_cursor.fetchone()
    return row[0]


def edit_note(ID, head="Empty", note="Empty", date="Empty"):
    db_cursor.execute("""SELECT head, note, date FROM note WHERE rowid=?""", str(ID))
    row = db_cursor.fetchone()

    if head is not row[0]:
        db_cursor.execute("""UPDATE note SET head=? WHERE rowid=?""", (head, ID))

    if note is not row[1]:
        db_cursor.execute("""UPDATE note SET note=? WHERE rowid=?""", (note, ID))

    if date is not row[2]:
        db_cursor.execute("""UPDATE note SET date=? WHERE rowid=?""", (date, ID))


def select_specific_note(ID):
    db_cursor.execute("""SELECT * FROM note WHERE rowid=?""", str(ID))
    print(db_cursor.fetchone())


def select_all_note():
    db_cursor.execute("""SELECT * FROM note""")
    row = db_cursor.fetchall()
    print(row)


def delete_note(ID):
    db_cursor.execute("""DELETE FROM note WHERE rowid=?""", str(ID))


# Starting manage relation tables

# Define the course in given semester.
def insert_coursein(semID, cID):  # This function will be called after courseID known.
    db_cursor.execute("""SELECT * FROM courseIn WHERE semesterID=? AND courseID=?""", (semID, str(cID)))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO courseIn VALUES(?,?)""", (semID, str(cID)))


# Select all course which are in given semester
def select_all_course_in_semester(semID):
    db_cursor.execute("""SELECT courseID FROM courseIn WHERE semesterID=?""", (semID,))
    row = db_cursor.fetchall()
    for id in row:
        db_cursor.execute("""SELECT name, code FROM course WHERE ID=?""", (str(id[0])))
        course = db_cursor.fetchone()
        print(course)


# Define section where it is
def insert_sectionin(semID, cID, secID):
    db_cursor.execute("""SELECT * FROM sectionIn WHERE semesterID=? AND courseID=? AND sectionID=?""", (semID, cID, secID))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO sectionIn VALUES(?,?,?)""", (semID, cID, secID))


def select_all_section_in(semID, cID):
    db_cursor.execute("""SELECT sectionID FROM sectionIn WHERE semesterID=? AND courseID=?""", (semID, cID))
    row = db_cursor.fetchall()
    for code in row:
        db_cursor.execute("""SELECT name FROM section WHERE ID=?""", str(code[0]))
        section = db_cursor.fetchone()
        print(section)


# Define announcement where it is
def insert_announcementin(semID, cID, annID):
    db_cursor.execute("""SELECT * FROM announcementIn WHERE semesterID=? AND courseID=? AND announcementID=?""",
                      (semID, cID, annID))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO announcementIn VALUES(?,?,?)""", (semID, cID, annID))


def select_all_announcement_in(semID, cID):
    db_cursor.execute("""SELECT announcementID FROM announcementIn WHERE semesterID=? AND courseID=?""", (semID, cID))
    row = db_cursor.fetchall()
    for id in row:
        db_cursor.execute("""SELECT head FROM announcement WHERE ID=?""", str(id[0]))
        announcement = db_cursor.fetchone()
        print(announcement)


# Define evaluation where it is
def insert_evaluationin(semID, cID, evaID):
    db_cursor.execute("""SELECT * FROM evaluationIn WHERE semesterID=? AND courseID=? AND evaluationID=?""",
                      (semID, cID, evaID))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO evaluationIn VALUES(?,?,?)""", (semID, cID, evaID))


def select_all_evaluation_in(semID, cID):
    db_cursor.execute("""SELECT evaluationID FROM evaluationIn WHERE semesterID=? AND courseID=?""",
                      (semID, cID))
    row = db_cursor.fetchall()
    for id in row:
        db_cursor.execute("""SELECT name, percentage FROM evaluation WHERE ID=?""", str(id[0]))
        evaluation = db_cursor.fetchone()
        print(evaluation)


# Define subject where it is
def insert_subjectin(semID, cID, subID):
    db_cursor.execute("""SELECT * FROM subjectIn WHERE semesterID=? AND courseID=? AND subjectID=?""",
                      (semID, cID, subID))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO subjectIn VALUES(?,?,?)""", (semID, cID, subID))


def select_all_subject_in(semID, cID):
    db_cursor.execute("""SELECT subjectID FROM subjectIn WHERE semesterID=? AND courseID=?""",
                      (semID, cID))
    row = db_cursor.fetchall()
    for id in row:
        db_cursor.execute("""SELECT subject, reference, week FROM subject WHERE ID=?""", str(id[0]))
        subject = db_cursor.fetchone()
        print(subject)


# Define student where it is
def insert_studentin(semID, cID, secID, stuID):
    db_cursor.execute("""SELECT * FROM studentIn WHERE semesterID=? AND courseID=? AND sectionID=? AND studentID=?""",
                      (semID, cID, secID, stuID))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO studentIn VALUES(?,?,?,?)""", (semID, cID, secID, stuID))
        print("OK")


def select_all_student_in(semID, cID, secID):
    db_cursor.execute("""SELECT studentID FROM studentIn WHERE semesterID=? AND courseID=? AND sectionID=?""",
                      (semID, cID, secID))
    row = db_cursor.fetchall()
    for id in row:
        db_cursor.execute("""SELECT name, ID FROM student WHERE ID=?""", id)
        student = db_cursor.fetchone()
        print(student)


# Define evaluation of student where it is
def insert_student_evaluationin(semID, cID, evaID, stuID, evaluation):
    db_cursor.execute("""SELECT * FROM studentEvaluationIn WHERE semesterID=? AND courseID=? AND evaluationID=? AND
                        studentID=?""", (semID, cID, evaID, stuID))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO studentEvaluationIn VALUES (?,?,?,?,?)""",
                          (semID, cID, evaID, stuID, evaluation))
    else:
        print("Evaluation have already be given")


def edit_studentEvaluation_in(semID, cID, evaID, stuID, evaluation):
    db_cursor.execute("""SELECT evaluation FROM studentEvaluationIn WHERE semesterID=? AND courseID=? AND
                         evaluationID=? AND studentID=?""", (semID, cID, evaID, stuID))
    row = db_cursor.fetchone()

    if evaluation is not row[0]:
        db_cursor.execute("""UPDATE studentEvaluationIn SET evaluation=? WHERE semesterID=? AND courseID=? AND
                         evaluationID=? AND studentID=?""", (evaluation, semID, cID, evaID, stuID))


def select_studentEvaluation_in(semID, cID, evaID, stuID):
    db_cursor.execute("""SELECT evaluation FROM studentEvaluationIn WHERE semesterID=? AND courseID=? AND
                         evaluationID=? AND studentID=?""", (semID, cID, evaID, stuID))
    row = db_cursor.fetchall()
    for id in row:
        print(id[0])


def select_all_studentEvaluation_in(semID, cID, stuID):
    db_cursor.execute("""SELECT evaluation FROM studentEvaluationIn WHERE semesterID=? AND courseID=? AND
                         studentID=?""", (semID, cID, stuID))
    row = db_cursor.fetchall()
    for id in row:
        print(id[0])


# Define note where it is
def insert_notein(semID, cID, stuID, nID):
    db_cursor.execute("""SELECT * FROM noteIn WHERE semesterID=? AND courseID=? AND studentID=? AND noteID=?""",
                      (semID, cID, stuID, nID))
    row = db_cursor.fetchone()
    if row is None:
        db_cursor.execute("""INSERT INTO noteIn VALUES (?,?,?,?)""", (semID, cID, stuID, nID))


def select_all_note_in(semID, cID, stuID):
    db_cursor.execute("""SELECT noteID FROM noteIn WHERE semesterID=? AND courseID=? AND studentID=?""",
                      (semID, cID, stuID,))
    row = db_cursor.fetchall()
    for id in row:
        db_cursor.execute("""SELECT head FROM note WHERE ID=?""", str(id[0]))
        note = db_cursor.fetchone()
        print(note)
