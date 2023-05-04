from django.urls import path
from . import views
app_name = 'vahedhub'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('courses/', views.CourseView.as_view(), name='course-list'),
    path('instructors/', views.InstructorView.as_view(), name = 'instructor-list'),
    path('sections/', views.SectionView.as_view(), name='section-list'),
    path('coursesfulldetail/', views.CoursesFullDetailView, name='course-full-detail-list'),
]