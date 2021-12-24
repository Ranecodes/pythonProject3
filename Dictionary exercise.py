course_room = {"CS101": 3004, "CS102": 4501, "CS103": 6755, "NT110": 1244, "CM241": 1411}
course_instructor = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241":"Lee"}
course_meeting = {"CS101": "8:00 a.m.", "CS102": "9:00 a.m.", "CS103":"10:00 a.m.", "NT110": "11:00 a.m.", "CM241": "1:00 p.m."}

print()
print("Course Information")
print("-----------------------")

user_entry = input("Course code: ")
if user_entry == "CS101":
    print("Room number", course_room["CS101"])
    print("Instructor: ", course_instructor["CS101"])
    print("Meeting time: ", course_meeting["CS101"])

elif user_entry == "CS102":
    print("Room number: ", course_room["CS102"])
    print("Instructor: ", course_instructor["CS102"])
    print("Meeting time: ", course_meeting["CS102"])

elif user_entry == "CS103":
    print("Room number: ", course_room["CS103"])
    print("Instructor: ", course_instructor["CS103"])
    print("Meeting time: ", course_meeting["CS103"])

else:
    print("Entry not valid.")