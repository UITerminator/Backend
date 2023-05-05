from django.shortcuts import render
from .models import *
from .serializers import CourseSerializer, InstructorSerializer, SectionSerializer,CommentSerializer,QuestionSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import copy
from .query import *

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
        if (i ==  len(Ecourses)):
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
        if (i ==  len(Gcourses)):
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
    # t=get_non_collision_courses(3620313, 1)
    return Response(get_all_courses())

@api_view()
def electiveCourses(request):
    return Response(get_ElectiveCourses())

@api_view()
def generalEducationCourses(request):
    return Response(get_GeneralEducationCourses())

@api_view()
def coreCourses(request):
    return Response(get_CoreCourses())

@api_view()
def showTadakhol(request):
    return Response(get_non_collision_courses(2822065,1))


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

@api_view()
def questions(request):
    return Response(get_question_answer())