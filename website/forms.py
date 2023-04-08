from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from django.core.validators import RegexValidator

class Sign_Up_Form(UserCreationForm):
    first_Name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}))
    ID_Number = forms.DecimalField(label="", max_digits=5, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ID Number'}))
    email = forms.EmailField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email address'}))
    
    class Meta:
        model = User
        fields = ("username", "first_Name", "ID_Number", "email", "password1", "password2")

        def __init__(self, *args, **kwargs):
            super(Sign_Up_Form, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label =''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li> \
                                                <li>Your password must contain at least 8 characters.</li> \
                                                <li>Your password can\'t be a commonly used password.</li> \
                                                <li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

 # add record form   
class Add_Record_Form(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First_Name", 'class': "form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last_Name", 'class': "form-control"}), label="")
    KRA_PIN = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "KRA PIN", 'class': "form-control"}), label="")
    Account_Number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Account Number", 'class': "form-control"}), label="")
    Phone_Number = forms.CharField(max_length=10, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone Number", 'class': "form-control"}), 
                                                                                validators=[RegexValidator(
                                                                                           regex=r"^0\d{9}$", 
                                                                                           message='Phone number should have 10 digits and start with 0 e.g. 0xxxxxxxxx', 
                                                                                           code='invalid_phone_number'
                                                                                        )], label="" )
    # image = forms.ImageField()

    class Meta:
            model = Record
            exclude = ('user',)
            # fields = "__all__" # this attribute will show all fields without the need to specify them again in class above
            





