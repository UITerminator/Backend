from django.contrib import admin
from .models import Course, Section, Building,TimeSlot , Section_TimeSlot,Exam , Instructor

# Register your models here.

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Building)
admin.site.register(TimeSlot)
admin.site.register(Section_TimeSlot)
admin.site.register(Exam)
admin.site.register(Instructor)



