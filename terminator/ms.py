from vahedhub.models import Course, Section, Section_TimeSlot, TimeSlot
sections = Section.objects.all()
courses = Course.objects.all()
section_timeslots = Section_TimeSlot.objects.all()
timeslots = TimeSlot.objects.all()

count = 0

for c in courses:
    for s in sections:
        for st in section_timeslots:
            for t in timeslots:
                if (s.CourseID_id == c.ID):
                    if (st.SectionID_id == s.ID):
                        if (t.ID == st.TimeSlotID_id):
                            print(c.ID, end='')
                            print(' ', end='')
                            print(s.ID, end='')
                            print(' ', end='')
                            print(t.day, end='')
                            print()
                            count = count + 1                            
print(count)