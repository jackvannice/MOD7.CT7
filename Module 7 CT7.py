def course_info(student_input):
    room_num = {"CSC101":3004,
               "CSC102":4501,
               "CSC103":6755,
               "NET110":1244,
               "COM241":1411}
    instructors = {"CSC101":"Haynes",
               "CSC102":"Alvarado",
               "CSC103":"Rich",
               "NET110":"Burke",
               "COM241":"Lee"}
    meeting_time = {"CSC101":"8:00 am",
               "CSC102":"9:00 am",
               "CSC103":"10:00 am",
               "NET110":"11:00 am",
               "COM241":"1:00 pm"}
    if student_input in room_num:
        return room_num[student_input], instructors[student_input], meeting_time[student_input]
    else:
        return "", "", ""

student_input = input("Please input your course number (options: CSC101, CSC102, CSC103, NET110, COM241): ")
course_info = course_info(student_input)

if course_info[0] != "":
    print(f"Room Number: {course_info[0]}")
    print(f"Instructor: {course_info[1]}")
    print(f"Meeting Time: {course_info[2]}")
else:
    print("Room Number not found")