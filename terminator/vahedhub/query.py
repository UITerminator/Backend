from .models import *

def get_course_section():

    sections = Section.objects.all()
    courses = Course.objects.all()
    
    course_section_list = []
    
    for c in courses:
        course = {"ID": c.ID, "Name" : c.name, "Course ID" : c.ID, "Course Code" : c.code, "Type" : c.type,                  "total_credit" : c.total_credit,"Practical Credit" : c.practical_credit ,"Sections": []}
        for s in sections:
            if s.CourseID_id == c.ID:
                course["Sections"].append({"Section ID" : s.ID, "Section Number" : s.num, "Instructor ID" : s.InstructorID_id})
        course_section_list.append(course)
                                           
    return course_section_list
    
def get_section_timeslots(course_section_list):
    section_timeslots = Section_TimeSlot.objects.all()
    
    for cs in course_section_list:
        for st in section_timeslots:
            for s in cs["Sections"]:
                if s["Section ID"] == st.SectionID_id:
                    s["TimeSlot"] = st.TimeSlotID_id
    
    return course_section_list
    
def get_section_time(course_section_timeslot_list):
    timeslots = TimeSlot.objects.all()
    
    for cst in course_section_timeslot_list:
        for t in timeslots:
            for s in cst["Sections"]:
                if t.ID == s["TimeSlot"]:
                    s["Day"] = t.day
                    s["Start Time"] = t.start_time
                    s["End Time"] = t.end_time
                    
    return course_section_timeslot_list
    
def get_section_instructor(course_section_time_list):
    instructors = Instructor.objects.all()
    
    for cst in course_section_time_list:
        for sec in cst["Sections"]:
            for ins in instructors:
                if ins.ID == sec["Instructor ID"]:
                    sec["Instructor"] = ins.first_name + ' ' + ins.last_name
    
    return course_section_time_list

                

def get_all_courses():
    return get_section_instructor(get_section_time(get_section_timeslots(get_course_section())))
    
def get_non_collision_courses(code, section):
    course_list = get_all_courses()
    
    day = ""
    start_time = ""
    end_time = ""
    
    for course in course_list:
        if course["Course Code"] == code:
            for sec in course["Sections"]:
                if sec["Section Number"] == section:
                    day = sec["Day"]
                    start_time = sec["Start Time"]
                    end_time = sec["End Time"]
                    break
            else:
                continue
            break
        
    print(day)
    print(start_time)
    print(end_time)
    




   