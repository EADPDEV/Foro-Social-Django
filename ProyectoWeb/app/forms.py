from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Image, Perfiles

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:None for k in fields}


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué estas pensando?'}))
    class Meta:
        model = Post
        fields = ['content']

class ImagePost(forms.ModelForm):
    image = forms.ImageField(label='', widget=forms.ClearableFileInput(attrs={"multiple":True}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Qué recuerdo tienes para mostrar?'}))
    class Meta:
        model = Image
        fields = ['image','content']
        help_texts = {k:None for k in fields}

class UserInformationForm(forms.ModelForm):
    bio = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'¿Hablanos de ti?'}))
    class Meta:
        model = Perfiles
        fields = ['bio']
        help_texts = {k:None for k in fields}
    