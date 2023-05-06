from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Building)
admin.site.register(TimeSlot)
admin.site.register(Section_TimeSlot)
admin.site.register(Exam)
admin.site.register(Instructor)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(SelectedCourses)
admin.site.register(Student)
