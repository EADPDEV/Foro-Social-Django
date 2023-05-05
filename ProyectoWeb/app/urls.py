from django.urls import re_path as url
from django.conf import settings
from django.views.static import serve

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('', LoginView.as_view(template_name='ProyectoWebApp/login.html'), name='autenticacion'),
    path('inicio/',views.inicio, name='Home'),
    path('mi_perfil/',views.miPerfil, name='mi_perfil'),
    path('mi_perfil/<int:pk>/',views.UpdatePerfiles, name='setting_profile'),
    path('perfil/<str:username>/', views.miPerfil, name = 'otro_usuario'),
    path('publicar/', views.publicar, name='publicar'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('comunidad/', views.comunidad, name='comunidad'),
    path('logout/', LogoutView.as_view(template_name='ProyectoWebApp/logout.html'), name='Logout'),
    path('contacto/',views.contacto, name='Contacto'),
    path('sobre_nosotros/', views.sobreNosotros, name='SobreNosotros'),
    path('crear-usuario/', views.registro, name='CrearUsuario'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
