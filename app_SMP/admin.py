from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.conf import settings
from .models import User, Teacher_List, Student_List, Student_Result, students_attendance

# User Register your models here.
admin.site.register(User)


# Add teacher Model admin Registration
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'Username', 'Joining_date', 'email', 'phone', 'address']


admin.site.register(Teacher_List, TeacherAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'Username', 'Joining_date', 'email', 'phone', 'address']


admin.site.register(Student_List, StudentAdmin)


class StudentResultAdmin(admin.ModelAdmin):
    list_display = ['Username', 'physics', 'chemistry', 'maths', 'social_studies', 'english', 'hindi']


admin.site.register(Student_Result, StudentResultAdmin)


class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ['Attendance_status', 'Reason','attendance_date']


admin.site.register(students_attendance, StudentAttendanceAdmin)
