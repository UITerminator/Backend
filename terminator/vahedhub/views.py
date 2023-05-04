from django.shortcuts import render
from .models import *
from .serializers import CourseSerializer, InstructorSerializer, SectionSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

def get_courses():
    course_list = []
    sections = Section.objects.all()
    courses = Course.objects.all()
    section_timeslots = Section_TimeSlot.objects.all()
    timeslots = TimeSlot.objects.all()
    for c in courses:
        for s in sections:
            for st in section_timeslots:
                for t in timeslots:
                    if (s.CourseID_id == c.ID):
                        if (st.SectionID_id == s.ID):
                            if (t.ID == st.TimeSlotID_id):
                                course_list.append({"Name" : c.name,
                                                    "Course ID" : c.ID,
                                                    "Course Code" : c.code,
                                                    "Section Number" : s.num,
                                                    "Day" : t.day,
                                                    "type" : c.type,
                                                    "Start Time" : t.start_time,
                                                    "End Time" : t.end_time})
    return course_list

def get_ElectiveCourses():
    Ecourses = get_courses()
    dic = {}
    
    i = 0
    while True:    
        if Ecourses[i]['type'] != "اختیاری":
            dic = Ecourses[i]
            Ecourses.remove(dic)
            i = i - 1
        i = i + 1
        if (i ==  len(Ecourses)):
            break
    
    return Ecourses

def get_GeneralEducationCourses():
    Gcourses = get_courses()
    dic = {}
    
    i = 0
    while True:    
        if Gcourses[i]['type'] != "عمومی":
            dic = Gcourses[i]
            Gcourses.remove(dic)
            i = i - 1
        i = i + 1
        if (i ==  len(Gcourses)):
            break
    
    return Gcourses

def get_CoreCourses():
    Ccourses = get_courses()
    dic = {}
    
    i = 0
    while True:    
        if Ccourses[i]['type'] != "تخصصی":
            dic = Ccourses[i]
            Ccourses.remove(dic)
            i = i - 1
        i = i + 1
        if (i ==  len(Ccourses)):
            break
    
    return Ccourses
    
class CourseView(ListAPIView):
    c = Course.objects.all()
    queryset = c
    serializer_class = CourseSerializer

class SectionView(ListAPIView):
    s = Section.objects.all()
    queryset = s
    serializer_class = SectionSerializer
    
class InstructorView(ListAPIView):
   queryset = Instructor.objects.prefetch_related('DepartmentID')
   serializer_class = InstructorSerializer
  
   
@api_view()
def CoursesFullDetailView(request):
    return Response(get_courses())

@api_view()
def electiveCourses(request):
    return Response(get_ElectiveCourses())

@api_view()
def generalEducationCourses(request):
    return Response(get_GeneralEducationCourses())

@api_view()
def coreCourses(request):
    return Response(get_CoreCourses())
  
def indexView(request):
    pass;

def indexView(request):
    pass;

