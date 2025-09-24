def courseInfo():
    roomNum = {"CSC101":3004,
               "CSC102":4501,
               "CSC103":6755,
               "NET110":1244,
               "COM241":1411}
    instructors = {"CSC101":"Haynes",
               "CSC102":"Alvarado",
               "CSC103":"Rich",
               "NET110":"Burke",
               "COM241":"Lee"}
    meetingTime = {"CSC101":"8:00 am",
               "CSC102":"9:00 am",
               "CSC103":"10:00 am",
               "NET110":"11:00 am",
               "COM241":"1:00 pm"}
    return roomNum, instructors, meetingTime

student_input = ("Please input your course number: ")
course_info = courseInfo(student_input)