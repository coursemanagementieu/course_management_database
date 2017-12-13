from db_tables import *
from db_fonk import *

create_entity_tables()
create_relation_tables()


# ---Samples---
# Semester
insert_semester("201701","14")
insert_semester("201702","14")

select_specific_semester("201701")
select_all_semester()

semester = "201701"

# Course
print("\n\nCourse Samples")
course = insert_course("Bilgisayar", "CE221", "ABC", "Lecturer")
insert_coursein(semester, course)

course = insert_course("Bilgisayar", "CE221", "ABC", "Lecturer")
insert_coursein(semester, course)

course = insert_course("Bilgisayarlar", "CE222", "ABC", "Lecturer")
insert_coursein(semester, course)

print("All course in semester: ")
select_all_course_in_semester(semester)

courseCode = "CE221"
print("Specific course with", courseCode)
course = select_course_rowid(semester, courseCode)
select_specific_course(course)

# Edit course
name = "Network"
code = "CE340"
book = "ABC"
refbook = "Lecturer"
syll = "www."
edit_course(course, name, code, book, refbook, syll)
# After edit
select_specific_course(course)

# Section
print("\n\nSection Samples")
section = insert_section("Section1", "M102", "15:00-17:00", "Friday")
insert_sectionin(semester, course, section)

section = insert_section("Section1", "M102", "15:00-17:00", "Friday")
insert_sectionin(semester, course, section)

section = insert_section("Section2", "M103", "15:00-17:00", "Thursday")
insert_sectionin(semester, course, section)

print("Select all section in:")
select_all_section_in(semester, course)

sectionName = "Section1"
print("Specific section with ", sectionName)
section = select_section_rowid(semester, course, sectionName)
select_specific_section(section)

# Edit section
sectionName = "Section1"
classroom = "M105"
hour = "15:00-16:50"
day = "Thursday"
# After edit
edit_section(section, sectionName, classroom, hour, day)
select_specific_section(section)

# Announcement
print("\n\nAnnouncement Samples")
announcement = insert_announcement("12.12.2017", "Midterm", "There will be a midterm")
insert_announcementin(semester, course, announcement)

announcement = insert_announcement("12.12.2017", "Midterm", "There will be a midterm")
insert_announcementin(semester, course, announcement)

# announcement = insert_announcement("13.12.2017", "Midterm", "There will be a midterm")
# insert_announcementin(semester, course, announcement)


announcement = insert_announcement("15.12.2017", "Midterm Result", "There will be a midterm")
insert_announcementin(semester, course, announcement)

select_all_announcement_in(semester, course)

head = "Midterm"
print("Specific announcement with ", head)
announcement = select_announcement_rowid(semester, course, head)
select_specific_announcement(announcement)

# Edit announcement
date = "12.13.2017"
head = "Midterm"
ann = "There will be a midterm on 15.12.2017"
edit_announcement(announcement, date, head, ann)
# After edit
select_specific_announcement(announcement)

# Subject
print("\n\n Subject Samples")
subject = insert_subject("BLA BA BLA", "Lecturer","1")
insert_subjectin(semester, course, subject)

subject = insert_subject("BLA BA BLA", "Lecturer","1")
insert_subjectin(semester, course, subject)

subject = insert_subject("BLA BA BLA", "Lecturer","2")
insert_subjectin(semester, course, subject)

select_all_subject_in(semester, course)

week = "1"
print("Specific subject with week =", week)
subject = select_subject_rowid(semester, course, week)
select_specific_subject(subject)

# Edit subject
sub = "BLA BLA BLA BLA"
ref = "Lecturer notes"
subjectweek = "2"
edit_subject(subject,sub, ref, subjectweek)
# After edit
select_specific_subject(subject)

# Evaluation
print("\n\n Evaluation Samples")
evaluation = insert_evaluation("Quiz", "10")
insert_evaluationin(semester, course, evaluation)

evaluation = insert_evaluation("Midterm", "25")
insert_evaluationin(semester, course, evaluation)

evaluation = insert_evaluation("Midterm", "25")
insert_evaluationin(semester, course, evaluation)

evaluation = insert_evaluation("Final", "60")
insert_evaluationin(semester, course, evaluation)

select_all_evaluation_in(semester, course)

evaluationName = "Midterm"
print("Specific evaluation with name = ", evaluationName)
evaluation = select_evaluiaton_rowid(semester, course, evaluationName)
select_specific_evaluation(evaluation)

# Edit evaluation
evaluationName = "Final"
percentage = "40"
edit_evaluation(evaluation,evaluationName, percentage)
# After edit
select_specific_evaluation(evaluation)

# Student
print("\n\nStudent Samples")
insert_student("20140602036", "Umut Yilmaz")
insert_studentin(semester, course, section, "20140602036")

insert_student("20140602036", "Umut Yilmaz")
insert_studentin(semester, course, section,"20140602036")

insert_student("20140602037", "Umut Yilmaz")
insert_studentin(semester, course, section, "20140602037")

insert_student("20140602038", "Umut Duymaz")
insert_studentin(semester, course, section, "20140602038")

select_all_student_in(semester, course, section)

student = "20140602036"
print("Specific student with ID = ", student)
select_specific_student(student)

# Edit student
stuName = "Elif Duymaz"
edit_student(student, stuName)
# After edit
select_specific_student(student)

# Note
print("\n\nNote Samples")
note = insert_note("Attandance","Student will fail with attendance","12.12.2017")
insert_notein(semester, course, student, note)

note = insert_note("Attandance","Student will fail with attendance","12.12.2017")
insert_notein(semester, course, student, note)

note = insert_note("Grade","BLA BLA","12.12.2017")
insert_notein(semester, course, student, note)

# note = insert_note("Attandance","Stu..","12.12.2017")
# insert_notein(semester, course, student, note)

select_all_note_in(semester, course, student)

noteHead = "Grade"
print("Specific note with head =", noteHead)
note = select_note_rowid(semester, course, student, noteHead)
select_specific_note(note)

# Edit note
nNote = "Student will not pass"
date = "12.15.2017"
edit_note(note, noteHead, nNote, date)
# After edit
select_specific_note(note)

# Student Evaluaton
print("\n\nStudent Evaluation Sample")
insert_student_evaluationin(semester, course, evaluation, student, 70)
insert_student_evaluationin(semester, course, evaluation, student, 80)

print("Student evaluation given evaluation name: ")
select_studentEvaluation_in(semester, course, evaluation, student)

print("All of the evaluation of a student: ")
select_all_studentEvaluation_in(semester, course, student)

# Edit evaluation
stuEvaluation = "100"
edit_studentEvaluation_in(semester, course, evaluation, student, stuEvaluation)
# After edit
select_studentEvaluation_in(semester, course, evaluation, student)

print("\n\nHERE IS SPECİAL\n\n")
select_all_student_in(semester,course, section)
delete_student(student)
select_all_student_in(semester, course, section)



print("\n\n")
