"""project URL Configuration

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
from Vet.views import index, about,  AnimalList, AnimalMineList, AnimalUpdate, AnimalDelete, AnimalCreate, Login, Logout, SignUp, ProfileCreate, ProfileUpdate, AnimalDetail, MensajeCreate, MensajeDelete, MensajeList
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views as auth_views
#from Vet import views
#from .view import profile_view
#from django.contrib.auth.views import LoginView
#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', about),
    path('animal/list', AnimalList.as_view(), name="animal-list"),
    path('animal/list/mine', AnimalMineList.as_view(), name="animal-mine"),
    path('animal/<pk>/update', AnimalUpdate.as_view(), name="animal-update"),
    path('post/<pk>/detail', AnimalDetail.as_view(), name="animal-detail"),
    path('animal/<pk>/delete', AnimalDelete.as_view(), name="animal-delete"),
    path('animal/create', AnimalCreate.as_view(), name="animal-create"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list" ),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create" ),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    #path('', include('project.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/profile/', profile_view, name='profile'),
    #path('', views.home, name='home'),
    #path('profile/', views.profile, name='profile'),
    #path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),