from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegisterForm, PostForm, ImagePost, UserInformationForm
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'ProyectoWebApp/inicio.html')

@login_required
def miPerfil(request, username= None):
    current_user = request.user
    if username and username != current_user:
        user = User.objects.get(username=username)
        posts = user.posts.all()
        images = user.images.all()
        
    else:
        user = current_user
        posts = current_user.posts.all()
        images = current_user.images.all()

    current_user = get_object_or_404(User, pk=request.user.pk)

    if request.method=='POST':
        userinfo = UserInformationForm(request.POST,instance=request.user.perfiles)
        if userinfo.is_valid:
            userinfo.save()
            return redirect('mi_perfil')
    else:
        userinfo = UserInformationForm(instance=request.user)
    return render(request,'ProyectoWebApp/mi_perfil.html', {'user':user, 'posts':posts, 'images':images,
                                                             'user_info': userinfo})

@login_required
class UpdatePerfiles(UpdateView):
    model = Perfiles
    userinfo = UserInformationForm
    fields = ['bio']
    template_name = ('ProyectoWebApp/mi_perfil.html')

@login_required
def contacto(request, username= None):
    current_user = request.user
    if username and username != current_user:
        user = User.objects.get(username=username)
        posts = user.posts.all()
        images = user.images.all()
    else:
        images = current_user.images.all()
        posts = current_user.posts.all()
        user = current_user

    if not request.user.is_authenticated:
        return render(request, 'ProyectoWebApp/login.html')
        
    if request.GET['buscar']:
        busqueda=request.GET['buscar']
        if busqueda:
            usuario=Perfiles.objects.filter(user__username__icontains=busqueda)
            posts = Post.objects.filter(user__username__icontains=busqueda)
            images = Image.objects.filter(user__username__icontains=busqueda)
        else:
            return render(request,'ProyectoWebApp/contacto.html',{'usuario':usuario, 'query': busqueda, 'user':user, 'posts':posts, 'images':images})
    return render(request,'ProyectoWebApp/contacto.html',{'usuario':usuario, 'query': busqueda, 'user':user, 'posts':posts, 'images':images})

def sobreNosotros(request):
    return render(request, 'ProyectoWebApp/sobre_nosotros.html')

def registro(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('Home')
    else:
        form = UserRegisterForm()
    return render(request, 'ProyectoWebApp/crear-usuario.html',{'formu':form})

def comunidad(request):
    posts = Post.objects.all()
    images = Image.objects.all()
    return render(request,'ProyectoWebApp/comunidad.html', {'posts': posts, 'images':images})

@login_required
def publicar(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = PostForm(request.POST, prefix='postform')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('comunidad')
    else:
        form = PostForm(prefix='postform')

    if request.method == "POST" and not form.is_valid():
        imageform = ImagePost(request.POST,request.FILES, prefix='postimg')
        form = PostForm(prefix='postform')
        if imageform.is_valid():
            postIMG = imageform.save(commit=False)
            postIMG.user = current_user
            postIMG.save()
            return redirect('comunidad')
    else:
        imageform = ImagePost(prefix='postimg')
    return render(request, 'ProyectoWebApp/publicar.html', {'form': form,'imageform': imageform})

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationships(from_user=current_user, to_user=to_user_id)
    rel.save()
    return redirect('comunidad')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationships.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    return redirect('comunidad')

def error_404(request, exception):
    return render(request,"not_found.html")