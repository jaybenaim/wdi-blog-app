"""blog_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog_app.views import *

urlpatterns = [
    path('', root), 
    path('admin/', admin.site.urls),
    path('home/', home),
    path('home/<int:id>', post_show, name='post_details'), 
    path('accounts/signup', signup, name='signup'), 
    path('accounts/signup_create', signup_create, name='signup_create'), 
    path('accounts/profile/', include('django.contrib.auth.urls')), 
    path('article/new', new_article, name='new_article'), 
    path('article/create', create_article, name='create_article'),
    path('article/<int:id>/edit', edit_article, name='edit_article'),
    path('article/<int:id>/delete', delete_article, name='delete_article'), 
    path('comments/new', create_comment, name='create_comment'), 
    path('comments/<int:id>/edit', edit_comment, name='edit_comment'), 
    path('comments/<int:id>/delete', delete_comment, name='delete_comment'),
   
]
