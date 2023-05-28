from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import ListCreateAPIView
from django.core.serializers import serialize
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework import status

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
def formattedJson(request):
    return Response(newJsonForFront())


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
    student = Student.objects.get(student_id=studentID)

    if student.UserID_id != request.user.id:
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    selected_course = SelectedCourses.objects.get(StudentID=student.ID)
    return Response(selected_course.selected_sections)


@api_view(['POST'])
@parser_classes([JSONParser])
def SelectCourseAndGetCollisionsView(request):
    # student = Student.objects.get(student_id = request.data["StudentID"])
    student = Student.objects.get(UserID_id=request.user.id)

    selected_course = SelectedCourses.objects.get(StudentID=student.ID)

    selected_course.selected_sections = request.data["Sections"]

    selected_course.save()

    collision_courses = []
    for section in request.data["Sections"]:
        collision_courses.extend(get_collision_courses(
            section["CourseCode"], section["SectionNumber"]))
    return Response(collision_courses)


@api_view(['POST'])
@parser_classes([JSONParser])
def createQuestion(request):
    # student = Student.objects.get(student_id = request.data["StudentID"])
    try:
        student = Student.objects.get(UserID_id=request.user.id)
        queText = request.data["Question"]
        InsID = request.data["InstructorID"]
        question = Question(like_number=0, dislike_number=0, Question_text=queText,
                            InstructorID_id=InsID, StudentID_id=student.ID)
        question.save()
        return Response("Success")
    except:
        return Response("Failed", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@parser_classes([JSONParser])
def likeQuestions(request):
    # student = Student.objects.get(student_id = request.data["StudentID"])
    try:
        question = Question.objects.get(ID=request.data["QuestionID"])
        if request.data["Like"]:
            question.like_number += 1
        else:
            question.dislike_number += 1

        question.save()
        return Response("Success")
    except:
        return Response("Failed", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@parser_classes([JSONParser])
def comment(request):
    try:
        student = Student.objects.get(UserID_id=request.user.id)
        InsID = request.data["InstructorID"]
        instructor = Instructor.objects.get(ID=InsID)
        comment_text = request.data["Comment"]
        stuBool = request.data["display_stu"]
        avgBool = request.data["display_avg"]
        comment = Comment(display_stu=stuBool, display_avg=avgBool, like_number=0, dislike_number=0,
                          comment_text=comment_text, InstructorID_id=instructor.ID, StudentID_id=student.ID)
        comment.save()
        return Response("Success")
    except:
        return Response("Failed", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def instructorComments(request, instructorID):
    try:
        instructor = Instructor.objects.get(ID=instructorID)
        if Comment.objects.filter(InstructorID_id=instructor.ID).exists():
            queryset = Comment.objects.filter(InstructorID_id=instructor.ID)
            data = list(queryset.values())
            return Response(data)
        else:
            raise Exception
    except:
        return Response("Failed", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@parser_classes([JSONParser])
def likeComments(request):
    try:
        comment = Comment.objects.get(ID=request.data["CommentID"])
        if request.data["Like"]:
            comment.like_number += 1
        else:
            comment.dislike_number += 1

        comment.save()
        return Response("Success")
    except:
        return Response("Failed", status=status.HTTP_400_BAD_REQUEST)


def indexView(request):
    pass


def indexView(request):
    pass


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


@ api_view(['GET'])
def questions(request):
    return Response(get_question_answer())


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
