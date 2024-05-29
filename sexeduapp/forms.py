from django import forms
from django.contrib.auth.models import User
from sexeduapp.models import UserProfileInfo, Laporan

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg bg-light fs-6',
        'placeholder': 'Buat Password'
    }))

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg bg-light fs-6',
                'placeholder': 'Masukkan Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg bg-light fs-6',
                'placeholder': 'Masukkan Email'
            }),
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ()  




class LaporanForm(forms.ModelForm):
    class Meta:
        model = Laporan
        fields = ['nama', 'email', 'deskripsi']
