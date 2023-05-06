from django.urls import path
from . import views

app_name = 'vahedhub'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('courses/', views.CourseView.as_view(), name='course-list'),
    path('instructors/', views.InstructorView.as_view(), name='instructor-list'),
    path('sections/', views.SectionView.as_view(), name='section-list'),
    path('coursesfulldetail/', views.CoursesFullDetailView, name='course-full-detail-list'),
    path('electiveCourses/', views.electiveCourses, name='electiveCourses'),
    path('electiveCourses/', views.electiveCourses, name='electiveCourses'),
    path('generalEducationCourses/', views.generalEducationCourses, name='generalEducationCourses'),
    path('coreCourses/', views.coreCourses, name='coreCourses'),
    path('selectCourseAndGetCollisions/', views.SelectCourseAndGetCollisionsView),
    path('showComment/', views.showComment.as_view(), name='showComment'),
    path('showQuestion/', views.showQuestion.as_view(), name='showQuestion'),
    path('questions/', views.questions, name='questions'),
    path('users/', views.UserList.as_view()),
    path('studentSelectedCourses/<int:studentID>', views.StudentSelectedCourses),
    path('formattedJson/', views.formattedJson, name='formattedJson'),
]
