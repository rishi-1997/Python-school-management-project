from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import student_required, teacher_required, principal_required
from . models import Teacher_List,Student_List,Student_Result,students_attendance
from django.shortcuts import redirect
from . import forms
from .forms import StudentResultForm

# Create your views here.


def home(request):
    return render(request, 'SMP_home/home.html')


def our_institutions(request):
    return render(request, 'SMP_home/our_institution.html')


def our_pillars(request):
    return render(request, 'SMP_home/our_pillars.html')


def advisory_panel(request):
    return render(request, 'SMP_home/advisory_panel.html')


def about_us(request):
    return render(request, 'SMP_home/about_us.html')


def select_profile(request):
    return render(request, 'profile_app/select_profile.html')


def principal_signup_view(request):
    character = "Principal"
    form = forms.PrincipalSignUpForm()
    if request.method == 'POST':
        form = forms.PrincipalSignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/principal_home/')
    my_dict = {'profile_character': character, 'form': form}
    return render(request, 'registration/principal_signup_form.html', context=my_dict)


def teacher_signup_view(request):
    character = "teacher"
    form = forms.TeacherSignUpForm()
    if request.method == 'POST':
        form = forms.TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/teacher_home/')
    my_dict = {'profile_character': character, 'form': form}
    return render(request, 'registration/teacher_signup_form.html', context=my_dict)


def student_signup_view(request):
    character = "student"
    form = forms.StudentSignUpForm()
    if request.method == 'POST':
        form = forms.StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/student_home/')
    my_dict = {'profile_character': character, 'form': form}
    return render(request, 'registration/student_signup_form.html', context=my_dict)
# Result views goes here------------------------------------#

def result_view(request):
    if request.user.is_authenticated:
        result_list = Student_Result.objects.all()
    my_dict = {'result_list':result_list}
    return render(request,'selected/principal_pages/view_results_list.html',context=my_dict)


def delete_result_view(request, username):
    record_result = Student_Result.objects.get(Username=username)
    record_result.delete()
    return redirect('/result_list/')


def update_result(request, username):
    record_result = Student_Result.objects.get(Username=username)
    form = StudentResultForm()
    if request.method == 'POST':
        form = forms.StudentResultForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return request('/result_list/')
    return render(request,'selected/principal_pages/update_result.html',{'record_result':record_result})
# principal pages goes below-----------------------#
@login_required()
@principal_required()
def principal_view(request):
    character = "principal"
    my_dict = {'profile_character': character}
    return render(request, 'selected/principal_pages/principal_home.html', context=my_dict)


@login_required()
@principal_required()
def principal_profile(request):
    character = "principal"
    my_dict = {'profile_character': character}
    return render(request, 'selected/principal_pages/principal_profile.html', context=my_dict)


def add_teacher(request):
    form = forms.TeacherAddForm()
    if request.method == 'POST':
        form = forms.TeacherAddForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'registration/thank.html')
    return render(request, 'selected/principal_pages/add_teachers.html', {'form': form})


def add_student(request):
    form = forms.StudentAddForm()
    if request.method == 'POST':
        form = forms.StudentAddForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'registration/thank.html')
    return render(request, 'selected/principal_pages/add_students.html', {'form': form})


# Teacher pages goes below---------------------------#

@login_required()
@teacher_required()
def teacher_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        teacher_detail = Teacher_List.objects.get(Username=username)
    my_dict = {'teacher_detail': teacher_detail}
    return render(request, 'selected/teacher_pages/teacher_home.html', context=my_dict)

@login_required()
@teacher_required()
def teacher_profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        teacher_detail = Teacher_List.objects.get(Username=username)
    my_dict = {'teacher_detail': teacher_detail}
    return render(request, 'selected/teacher_pages/teacher_profile.html', context=my_dict)


def teacher_list(request):
    teachers_list = Teacher_List.objects.all()
    return render(request,'selected/teacher_pages/teachers_list.html', {'teachers_list':teachers_list})


def delete_teacher_view(request, username):
    record_teacher = Teacher_List.objects.get(Username=username)
    record_teacher.delete()
    return redirect('/teacher_list/')


def update_teacher(request, username):
    record_teacher = Teacher_List.objects.get(Username=username)
    form = forms.TeacherAddForm()
    if request.method == 'POST':
        form = forms.TeacherAddForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return request('/teacher_list/')
    return render(request,'selected/teacher_pages/update_teacher.html',{'record_teacher':record_teacher})

# Student pages goes below --------------------------#
@login_required()
@student_required()
def student_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        student_detail = Student_List.objects.get(Username=username)
    my_dict = {'student_detail': student_detail}
    return render(request, 'selected/student_pages/student_home.html', context=my_dict)


@login_required()
@student_required()
def student_profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        student_detail = Student_List.objects.get(Username=username)
    my_dict = {'student_detail': student_detail}
    return render(request, 'selected/student_pages/student_profile.html', context=my_dict)


@login_required()
@student_required()
def view_result(request):
    if request.user.is_authenticated:
        username = request.user.username
        student_result = Student_Result.objects.get(Username=username)
    my_dict = {'student_result' : student_result}
    return render(request,'selected/student_pages/view_result.html', context=my_dict)


def student_list(request):
    Student_list = Student_List.objects.all()
    return render(request,'selected/student_pages/students_list.html', {'Student_list':Student_list})


def delete_student_view(request, username):
    record_student = Student_List.objects.get(Username=username)
    record_student.delete()
    return redirect('/student_list/')




# Result_add_View -----------------------------------------#

@ login_required()
def student_result_input(request):
    form = forms.StudentResultForm()
    if request.method == 'POST':
        form = forms.StudentResultForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/result_list/')
    return render(request, 'selected/principal_pages/add_student_results.html', {'form': form})


# logout view ------------------------------------------#
def logout(request):
    return render(request,'registration/logout.html')


# add attendance ---------------------------------------#

def student_attendance(request):
    Student_list = Student_List.objects.all()
    form = forms.student_attendance_form()
    if request.method == 'POST':
        import pdb; pdb.set_trace()
        form = forms.student_attendance_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'registration/thank.html')
    my_dict = {'form':form, 'Student_list':Student_list}
    return render(request, 'selected/teacher_pages/add_student_attendance.html',context=my_dict)