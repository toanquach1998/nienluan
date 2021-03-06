from django import forms
import re
from django.contrib.auth import get_user_model

User = get_user_model()
from django.core.exceptions import ObjectDoesNotExist

class RegistrationFrom(forms.Form):
    username = forms.CharField(label='Tài khoản' , max_length= 30)   
    password1 = forms.CharField(label='Mật khẩn', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Số điện thoại', max_length=10)
    citizen_identity_card = forms.CharField(label="Số CMND", max_length=9)

    def clean_password2(self):
        if 'password1'in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")        

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặt biệt")
        try:
                User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],password=self.cleaned_data['password1'],email=self.cleaned_data['email'],
        citizen_identity_card=self.cleaned_data['citizen_identity_card'],phone_number=self.cleaned_data['phone_number'])
