from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import RequestsClient
from django.test import Client
from rest_framework import status
from django.urls import reverse
from .query import *
from .models import *

class VahedhubTestCases(APITestCase):

    def test_instructorId_should_response_failed_when_id_is_not_valid(self):
        client = RequestsClient()
        response = client.get('http://localhost:8000/vahedhub/instructorComments/99999999')
        status_code = response.status_code
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    def test_studentSelectedCourses_should_response_failed_when_student_is_empty(self):
        client = RequestsClient()
        response = client.get('http://localhost:8000/vahedhub/studentSelectedCourses/99999999')
        status_code = response.status_code
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    def test_comment_should_response_ok_when_data_is_not_empty(self):
        url = 'http://localhost:8000/vahedhub/comment/'
        data = {
                  "InstructorID": 29,
                  "Comment": "he is a bad teacher",
                  "display_stu" : 0,
                  "display_avg" : 0
                }
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_200_OK
        
        
    def test_comment_should_response_400_when_instructor_is_not_exist(self):
        url = 'http://localhost:8000/vahedhub/comment/'
        data = {
                  "InstructorID": -1,
                  "Comment": "he is a bad teacher",
                  "display_stu" : 0,
                  "display_avg" : 0
                }
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        
    def test_comment_should_response_400_when_comment_is_empty(self):
        url = 'http://localhost:8000/vahedhub/comment/'
        data = {
                  "InstructorID": 5,
                  "Comment": "",
                  "display_stu" : 0,
                  "display_avg" : 0
                }
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    def test_comment_should_response_400_when_data_is_empty(self):
        url = 'http://localhost:8000/vahedhub/comment/'
        data = {}
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
    def test_selectCourseAndGetCollision_should_response_400_when_data_is_empty(self):
        url = 'http://localhost:8000/vahedhub/selectCourseAndGetCollisions/'
        data = {}
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        
        
    def test_likeComment_should_response_ok_when_like_is_one(self):
        url = 'http://localhost:8000/vahedhub/likeComments/'
        data = {
                  "CommentID": 29,
                  "Like": 1,
                }
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_200_OK
        
        
    def test_likeComment_should_response_ok_when_like_is_zero(self):
        url = 'http://localhost:8000/vahedhub/likeComments/'
        data = {
                  "CommentID": 29,
                  "Like": 0,
                }
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_200_OK
        
        
    def test_likeComment_should_response_400_when_comment_is_not_exist(self):
        url = 'http://localhost:8000/vahedhub/likeComments/'
        data = {
                  "CommentID": 01,
                  "Like": 0,
                }
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        
    def test_likeComment_should_response_400_when_like_is_not_zero_or_one(self):
        url = 'http://localhost:8000/vahedhub/likeComments/'
        data = {
                  "CommentID": 01,
                  "Like": -1,
                }
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
            
        
        
    def test_likeComment_should_response_400_when_data_is_empty(self):
        url = 'http://localhost:8000/vahedhub/likeComments/'
        data = {}
        response = self.client.post(url, data, format='json')
        status_code = response.status_code
        print(response.content)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        
class GetCollisionTestCases(APITestCase):
    fixtures = ['student', 'section', 'course', 'timeslot', 'sec_timeslot']
    
    def test_getallcourses_should_not_empty_if_database_is_not_empty(self):
        courses = get_all_courses()
        assert len(courses) > 0
        
    def test_getCoreCourses_should_not_empty_when_getAllCourses_is_not_empty():
        courses = get_all_courses()
        core_courses = get_CoreCourses()
        
        if len(courses) > 0:
            assert len(core_courses) > 0
        else:
            assert len(courses) == 0
            
            
    def test_getElectiveCourses_should_not_empty_when_getAllCourses_is_not_empty():
        courses = get_all_courses()
        elective_courses = get_ElectiveCourses()
        
        if len(courses) > 0:
            assert len(elective_courses) > 0
        else:
            assert len(courses) == 0
            
    def test_getGeneralEducationCourses_should_not_empty_when_getAllCourses_is_not_empty():
        courses = get_all_courses()
        general_courses = get_GeneralEducationCourses()
        
        if len(courses) > 0:
            assert len(general_courses) > 0
        else:
            assert len(courses) == 0
            
    def test_getCoreCourses_should_return_corecourses():
        core_courses = get_CoreCourses()
        
        flag = True
        for course in core_courses:
            if course["Type"] != 'تخصصی':
                flag = false
                break
       assert flag == True
       
    def test_getElectiveCourses_should_return_electivecourses():
        elective_courses = get_ElectiveCourses()
        
        flag = True
        for course in elective_courses:
            if course["Type"] != 'اختیاری':
                flag = false
                break
       assert flag == True
       
       
    def test_getGeneralEducationCourses_should_return_generalcourses():
        general_courses = get_GeneralEducationCourses()
        
        flag = True
        for course in general_courses:
            if course["Type"] != 'عمومی':
                flag = false
                break
       assert flag == True
       
    def test_get_collision_courses_should_return_emptylist_when_code_is_not_valid():
        courses = get_collsion_courses(-1, 1)
        assert len(courses) == 0
        
    


    
    
        

        
        
        
    
   




