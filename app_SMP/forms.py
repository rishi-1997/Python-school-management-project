from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Teacher_List, Student_List, Student_Result, students_attendance


class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class PrincipalSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_principal = True
        if commit:
            user.save()
        return user


class TeacherAddForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'Second Name'}))
    last_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    Username = forms.CharField(min_length=6, label="", max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    Joining_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Joining Date'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label="")
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone'}), label="")
    address = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Teacher_List
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        email_value = cleaned_data['email']
        if email_value[len(email_value) - 9:] != 'gmail.com':
            raise forms.ValidationError('wrong mail id')

        input_phone = cleaned_data['phone']
        if input_phone < 1000000000 or input_phone > 10000000000:
            raise forms.ValidationError('Please input the correct mobile number')

        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value) != 0:
            raise forms.ValidationError("You are not allowed to signup")


class StudentAddForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    middle_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'Second Name'}))
    last_name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    Username = forms.CharField(min_length=6, label="", max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    Joining_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Joining Date'}), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label="")
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone'}), label="")
    address = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Student_List
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        email_value = cleaned_data['email']
        if email_value[len(email_value) - 9:] != 'gmail.com':
            raise forms.ValidationError('wrong mail id')

        input_phone = cleaned_data['phone']
        if input_phone < 1000000000 or input_phone > 10000000000:
            raise forms.ValidationError('Please input the correct mobile number')

        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value) != 0:
            raise forms.ValidationError("You are not allowed to signup")


class StudentResultForm(forms.ModelForm):
    Username = forms.CharField(min_length=6, label="", max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    physics = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '/100'}), label="Physics")
    chemistry = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '/100'}), label="Chemistry")
    maths = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '/100'}), label="Maths")
    social_studies = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '/100'}), label="Social studies")
    english = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '/100'}), label="English")
    hindi = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '/100'}), label="Hindi")

    class Meta:
        model = Student_Result
        fields = '__all__'

    def clean(self):
        cleaned_data = super(StudentResultForm, self).clean()

        input_physics = cleaned_data['physics']
        if input_physics > 100:
            raise forms.ValidationError("Marks must be less than or equal to 100")
        input_chemistry = cleaned_data['chemistry']
        if input_chemistry > 100:
            raise forms.ValidationError("Marks must be less than or equal to 100")
        input_maths = cleaned_data['maths']
        if input_maths > 100:
            raise forms.ValidationError("Marks must be less than or equal to 100")
        input_ssc = cleaned_data['social_studies']
        if input_ssc > 100:
            raise forms.ValidationError("Marks must be less than or equal to 100")
        input_english = cleaned_data['english']
        if input_english > 100:
            raise forms.ValidationError("Marks must be less than or equal to 100")
        input_hindi = cleaned_data['hindi']
        if input_hindi > 100:
            raise forms.ValidationError("Marks must be less than or equal to 100")


class student_attendance_form(forms.ModelForm):
    # Username = forms.CharField(min_length=6, label="", max_length=30,
    #                            widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    # ATTENDANCE_CHOICE = (
    #     ('P', 'Present'),
    #     ('A', 'Absent'),
    # )
    # Attendance_status = forms.ChoiceField(choices=ATTENDANCE_CHOICE)
    # Reason = forms.CharField(max_length=50, required=False, label="",
    #                          widget=forms.TextInput(attrs={'placeholder': 'Reason'}))
    # attendance_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Attendance Date'}), label='')"""

    class Meta:
        model = students_attendance
        fields = '__all__'
