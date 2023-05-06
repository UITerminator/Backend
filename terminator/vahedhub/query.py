from .models import *
import copy
import datetime


def get_ElectiveCourses():
    Ecourses = get_all_courses()
    dic = {}

    i = 0
    while True:
        if Ecourses[i]['Type'] != "اختیاری":
            dic = Ecourses[i]
            Ecourses.remove(dic)
            i = i - 1
        i = i + 1
        if (i == len(Ecourses)):
            break

    return Ecourses


def get_GeneralEducationCourses():
    Gcourses = get_all_courses()
    dic = {}

    i = 0
    while True:
        if Gcourses[i]['Type'] != "عمومی":
            dic = Gcourses[i]
            Gcourses.remove(dic)
            i = i - 1
        i = i + 1
        if (i == len(Gcourses)):
            break

    return Gcourses


def get_CoreCourses():
    Ccourses = get_all_courses()
    dic = {}

    i = 0
    while True:
        if Ccourses[i]['Type'] != "تخصصی":
            dic = Ccourses[i]
            Ccourses.remove(dic)
            i = i - 1
        i = i + 1
        if (i == len(Ccourses)):
            break

    return Ccourses


def get_course_section():
    sections = Section.objects.all()
    courses = Course.objects.all()

    course_section_list = []

    for c in courses:
        course = {"ID": c.ID, "Name": c.name,
                  "Course ID": c.ID,
                  "Course Code": c.code,
                  "Type": c.type,
                  "total_credit": c.total_credit,
                  "Practical Credit": c.practical_credit,
                  "Sections": []}
        for s in sections:
            if s.CourseID_id == c.ID:
                course["Sections"].append({"Section ID": s.ID,
                                           "Section Number": s.num,
                                           "Instructor ID": s.InstructorID_id,
                                           "Instructor Name": "",
                                           "TimeSlots": []})

        course_section_list.append(course)

    return course_section_list


def get_section_timeslots(course_section_list):
    section_timeslots = Section_TimeSlot.objects.all()

    for cs in course_section_list:
        for s in cs["Sections"]:
            for st in section_timeslots:
                if st.SectionID_id == s["Section ID"]:
                    s["TimeSlots"].append({"TimeSlotID": st.TimeSlotID_id})

    return course_section_list


def get_section_time(course_section_timeslot_list):
    timeslots = TimeSlot.objects.all()

    for cst in course_section_timeslot_list:
        for s in cst["Sections"]:
            for st in s["TimeSlots"]:
                for t in timeslots:
                    if st["TimeSlotID"] == t.ID:
                        st["Day"] = t.day
                        st["StartTime"] = t.start_time
                        st["EndTime"] = t.end_time

    return course_section_timeslot_list


def get_section_instructor(course_section_time_list):
    instructors = Instructor.objects.all()

    for cst in course_section_time_list:
        for sec in cst["Sections"]:
            for ins in instructors:
                if ins.ID == sec["Instructor ID"]:
                    sec["Instructor Name"] = ins.first_name + \
                        ' ' + ins.last_name

    return course_section_time_list


def get_all_courses():
    return get_section_time(get_section_timeslots(get_section_instructor(get_course_section())))


def get_collision_courses(code, section):
    course_list = get_all_courses()

    day = ""
    start_time = ""
    end_time = ""

    for course in course_list:
        if course["Course Code"] == code:
            for sec in course["Sections"]:
                if sec["Section Number"] == section:
                    for ts in sec["TimeSlots"]:
                        day = ts["Day"]
                        start_time = ts["StartTime"]
                        end_time = ts["EndTime"]
                    break
            else:
                continue
            break

    tcourses = []
    for course in course_list:
        check = False
        for sections in course["Sections"]:
            for ts in sections["TimeSlots"]:
                if ts["Day"] == day:
                    if ts["StartTime"] == start_time or ts["EndTime"] == end_time:
                        if check == False:
                            tmpc = copy.deepcopy(course)
                            tcourses.append(tmpc)
                            tcourses[-1]["Sections"].clear()
                            check = True
                        tcourses[-1]["Sections"].append(sections)

    return tcourses


def get_question_answer():
    question = Question.objects.all()
    answer = Answer.objects.all()

    question_answer_list = []

    for q in question:
        question = {"ID": q.ID, "Student ID": q.StudentID_id, "Instructor ID": q.InstructorID_id,
                    "Like Number": q.like_number, "Dislike Number": q.dislike_number,
                    "Question Text": q.Question_text, "Answers": []}
        for a in answer:
            if q.ID == a.QuestionID_id:
                question["Answers"].append(
                    {"Answer ID": a.ID, "Answer StudentID": a.StudentID_id, "Answer Like Number": a.like_number,
                     "Answer Dislike Number": a.dislike_number, "Answer Text ": a.answer_text})
        question_answer_list.append(question)

    return question_answer_list


def newJsonForFront():
    courselist = get_all_courses()
    days = {
        0: "saturday",
        1: "sunday",
        2: "monday",
        3: "tuesday",
        4: "wednesday",
    }
    rev_days = {
        "saturday": 0,
        "sunday": 1,
        "monday": 2,
        "tuesday": 3,
        "wednesday": 4,
    }
    hours = {
        0: "08:00:00",
        1: "09:00:00",
        2: "10:00:00",
        3: "11:00:00",
        4: "12:00:00",
        5: "13:00:00",
        6: "14:00:00",
        7: "15:00:00",
        8: "16:00:00",
        9: "17:00:00",
        10: "18:00:00",
    }
    rev_hours = {
        "08:00:00": 0,
        "09:00:00": 1,
        "10:00:00": 2,
        "11:00:00": 3,
        "12:00:00": 4,
        "13:00:00": 5,
        "14:00:00": 6,
        "15:00:00": 7,
        "16:00:00": 8,
        "17:00:00": 9,
        "18:00:00": 10,
    }
    newJson = []

    for i in range(5):
        temp = {"Day": days[i], "Times": []}
        for j in range(10):
            time = {"Start Time": hours[j],
                    "End Time": hours[j+1], "Sections": []}
            temp["Times"].append(time)
        newJson.append(temp)

    for course in courselist:
        for section in course["Sections"]:

            for ts in section["TimeSlots"]:
                temp_section = {
                    "Name": course["Name"], "Course ID": course["Course ID"], "Course Code": course["Course Code"], "Type": course["Type"], "total_credit": course["total_credit"], "Practical Credit": course["Practical Credit"],
                    "Instructor Name": section["Instructor Name"], "Section ID": section["Section ID"], "Section Number": section["Section Number"], "Instructor ID": section["Instructor ID"], "TimeSlotID": ts["TimeSlotID"], "Day": ts["Day"], "StartTime": ts["StartTime"], "EndTime": ts["EndTime"]}
                if int(str(temp_section["EndTime"])[:2]) - int(str(temp_section["StartTime"])[:2]) == 1:
                    newJson[rev_days[ts["Day"]]
                            ]["Times"][rev_hours[str(ts["StartTime"])]]["Sections"].append(temp_section)

                else:
                    endtime = datetime.time(
                        int(str(temp_section["EndTime"])[:2]) - 1, 0)
                    temp_section["EndTime"] = endtime

                    newsection=copy.deepcopy(temp_section)
                    del newsection["Day"]
                    del newsection["StartTime"]
                    del newsection["EndTime"]
                    newJson[rev_days[temp_section["Day"]]]["Times"][rev_hours[str(
                        temp_section["StartTime"])]]["Sections"].append(copy.deepcopy(newsection))

                    starttime = datetime.time(
                        int(str(temp_section["StartTime"])[:2])+1, 0)
                    temp_section["StartTime"] = starttime

                    endtime = datetime.time(
                        int(str(temp_section["EndTime"])[:2])+1, 0)
                    temp_section["EndTime"] = endtime

                    newsection=copy.deepcopy(temp_section)
                    del newsection["Day"]
                    del newsection["StartTime"]
                    del newsection["EndTime"]
                    newJson[rev_days[temp_section["Day"]]
                            ]["Times"][rev_hours[str(temp_section["StartTime"])]]["Sections"].append(copy.deepcopy(newsection))

    return newJson
