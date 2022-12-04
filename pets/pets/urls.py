"""pets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from display import views 
from display.views import hi 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.welcome), 
    path('hello/', hi), 
    path('', views.get_title), 
    path('show_pets/', views.get_pets),
    path('add_pets/', views.add_pet),
    path('delete_pets/', views.delete_pet),
    path('edit_pet/', views.edit_pet),
]
