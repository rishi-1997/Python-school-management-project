"""SMP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_SMP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('our_institutions/', views.our_institutions),
    path('our_pillars/', views.our_pillars),
    path('advisory_panel/', views.advisory_panel),
    path('about_us/', views.about_us),
    path('select_profile/', views.select_profile),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/student/', views.student_signup_view, name='student_signup'),
    path('accounts/signup/teacher/', views.teacher_signup_view, name='teacher_signup'),
    path('accounts/signup/principal/', views.principal_signup_view, name='teacher_signup'),
    path('principal_home/', views.principal_view),
    path('add_teacher/', views.add_teacher),
    path('add_student/', views.add_student),
    path('result_list/', views.result_view),
    path('add_student_results/', views.student_result_input),
    path('view_result/', views.view_result),
    path('teacher_home/', views.teacher_view),
    path('student_home/', views.student_view),
    path('principal_profile/', views.principal_profile),
    path('teacher_profile/', views.teacher_profile),
    path('student_profile/', views.student_profile),
    path('teacher/', views.teacher_view),
    path('student/', views.student_view),
    path('logout/', views.logout),
    path('delete_result_record/<username>', views.delete_result_view),
    path('update_result_record/<username>', views.update_result),
    path('student_list/', views.student_list),
    path('teacher_list/', views.teacher_list),
    path('teacher_delete/<username>', views.delete_teacher_view),
    path('student_delete/<username>', views.delete_student_view),
    path('update_teacher_record/<username>', views.update_teacher),
    path('add_student_attendance/', views.student_attendance),

]
