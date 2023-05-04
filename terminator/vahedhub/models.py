from django.db import models


class Student(models.Model):
    ID = models.IntegerField(primary_key=True)
    DepartmentID = models.ForeignKey('Department', on_delete=models.CASCADE)
    entry_year = models.IntegerField()
    passed_credit = models.IntegerField()
    GPA = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    gender = models.BooleanField()
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    


class Takes(models.Model):
    ID = models.IntegerField(primary_key=True)
    StudentID = models.ForeignKey('Student', on_delete=models.CASCADE)
    SectionID = models.ForeignKey('Section', on_delete=models.CASCADE)
    grade = models.IntegerField()
    
    def __str__(self):
        return self.ID


class Department(models.Model):
    ID = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Instructor(models.Model):
    ID = models.IntegerField(primary_key=True)
    DepartmentID = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='ins_dept')
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Section(models.Model):
    ID = models.IntegerField(primary_key=True)
    InstructorID = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    CourseID = models.ForeignKey('Course', on_delete=models.CASCADE)
    TermID = models.ForeignKey('Term', on_delete=models.CASCADE)
    BuildingID = models.ForeignKey('Building', on_delete=models.CASCADE)
    ExamID = models.ForeignKey('Exam', on_delete=models.CASCADE)
    num = models.IntegerField()
    capacity = models.IntegerField()
    gender = models.IntegerField()
    
    def __str__(self):
        return self.ID



class Section_TimeSlot(models.Model):
    ID = models.IntegerField(primary_key=True)
    SectionID = models.ForeignKey('Section', on_delete=models.CASCADE)
    TimeSlotID = models.ForeignKey('TimeSlot', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ID

class TimeSlot(models.Model):
    ID = models.IntegerField(primary_key=True)
    day = models.CharField(max_length = 50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return self.ID


class Exam(models.Model):
    ID = models.IntegerField(primary_key=True)
    date_time = models.DateField()
    building_id = models.ForeignKey('Building', on_delete=models.CASCADE)
    # ?????
    room_number = models.IntegerField()
    
    def __str__(self):
        return self.ID


class Course(models.Model):
    ID = models.IntegerField(primary_key=True)
    code = models.IntegerField()
    total_credit = models.IntegerField()
    practical_credit = models.IntegerField()
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Term(models.Model):
    ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()
    
    def __str(self):
        return self.name


class Building(models.Model):
    ID = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Comment(models.Model):
    pass


class Vote(models.Model):
    pass


class Choice(models.Model):
    pass


class Question(models.Model):
    pass
