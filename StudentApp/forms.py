from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import FileInput

from StudentApp.models import Login, CollegeAdmin, Student, Marks


class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username',)


class CollegeAdminForm(forms.ModelForm):
    ph_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Must be in the format: '9999999999'")
    phone = forms.CharField(validators=[ph_regex])

    class Meta:
        model = CollegeAdmin
        exclude = ('user',)


class StudentForm(forms.ModelForm):
    dob = forms.DateField(label="Date Of Birth", widget=DateInput)
    ph_regex = RegexValidator(regex=r'^[6-9]\d{9}$', message="Must be in the format: '9999999999'")
    phone = forms.CharField(validators=[ph_regex])
    photo = forms.ImageField(widget=FileInput)

    class Meta:
        model = Student
        exclude = ('user',)

    def check_dob(self):
        date1 = self.cleaned_data['dob']
        age = (date.today() - date1).days / 365
        if age < 18:
            self.add_error('dob', 'Must be at least 18 years old to register!')
        return date1

    # def file_size(value):  # add this to some file where you can import it from
    #     limit = 2 * 1024 * 1024
    #     if value.size > limit:
    #         raise ValidationError('File too large. Size should not exceed 2 MiB.')

    def clean(self):
        cleaned_data = super().clean()
        self.check_dob()
        # self.file_size()


class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields='__all__'

class UpdtMarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields='__all__'

        def __init__(self, *args, **kwargs):
            super(UpdtMarksForm, self).__init__(*args, **kwargs)
            # Make the 'stud_id' field readonly
            self.fields['stud_id'].widget.attrs['readonly'] = True