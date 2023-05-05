from django.shortcuts import render
from .models import *
from .serializers import CourseSerializer, InstructorSerializer, SectionSerializer,CommentSerializer,QuestionSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes

import copy
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
   
@api_view(['POST'])
@parser_classes([JSONParser])
def SelectCourseAndGetCollisionsView(request):   
    return Response(get_non_collision_courses(request.data["Code"], request.data["SectionNumber"]))


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