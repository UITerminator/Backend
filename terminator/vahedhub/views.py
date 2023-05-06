from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes

from rest_framework.permissions import IsAdminUser
from .permissions import *

import copy
import json
from .query import *

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


@api_view(['GET'])
def CoursesFullDetailView(request):
    return Response(get_all_courses())

@api_view(['GET'])
def electiveCourses(request):
    return Response(get_ElectiveCourses())

@api_view(['GET'])
def generalEducationCourses(request):
    return Response(get_GeneralEducationCourses())

@api_view(['GET'])
def coreCourses(request):
    return Response(get_CoreCourses())
    
@api_view(['GET'])
def StudentSelectedCourses(request, studentID):
    student = Student.objects.get(student_id = studentID)
    selected_course = SelectedCourses.objects.get(StudentID = student.ID)
    return Response(selected_course.selected_sections)
   
@api_view(['POST'])
@parser_classes([JSONParser])
def SelectCourseAndGetCollisionsView(request):
    student = Student.objects.get(student_id = request.data["StudentID"])
       
    selected_course = SelectedCourses.objects.get(StudentID = student.ID)
    
    selected_course.selected_sections = request.data["Sections"]
   
    selected_course.save()
 
    collision_courses = []
    for section in request.data["Sections"]:
        collision_courses.extend(get_collision_courses(section["CourseCode"], section["SectionNumber"]))
    return Response(collision_courses)
    

def indexView(request):
    pass;

def indexView(request):
    pass;
    
    
class showComment(ListAPIView):
    c = Comment.objects.all()
    queryset = c
    serializer_class = CommentSerializer

class showQuestion(ListAPIView):
    q = Question.objects.all()
    queryset = q
    serializer_class = QuestionSerializer

# @api_view()
# def comments(request):
#     return Response(get_ElectiveCourses())

@api_view(['GET'])
def questions(request):
    return Response(get_question_answer())
    
                       
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)