from db_tables import *
from db_fonk import *

create_entity_tables()
create_relation_tables()

# Samples
insert_course("Bilgisayar Bilimleri","CE201","Database in First Course,3e,Abraham Silverster","Lecterur slayts",
              "www.ieusyllabus.com")
insert_announcement("12.12.2017","Quizes","There will be a quizz in the next class")
insert_evaluation("quiz","5")
insert_note("Missing quiz","Student umut will be taken again quiz 1","12.12.2017")
insert_section("M103","13.00-15.00","Monday")
insert_subject("Bla bla bla","Our textbook","1")
insert_semester("201602","14")
insert_student("20140602036","Umut Yilmaz")
save_changes()

print("\n\n")
