from rest_framework import serializers
from .models import Course, Instructor, Section

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'
    #search_url = serializers.SerializerMethodField('get_search_url') 
    #def get_search_url(self, obj):
        #return "http://www.isbnsearch.org/isbn/{}"
        
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__' 
        
