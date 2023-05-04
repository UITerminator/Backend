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
  
def indexView(request):
    pass;

