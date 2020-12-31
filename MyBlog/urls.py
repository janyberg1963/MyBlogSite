"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView as auth_views
from django.contrib.auth.views import LogoutView as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),

    #login
    path('accounts/login/', auth_views.as_view(template_name='registration/login.html'), name='login'),

    #logout

    path('accounts/logout/', auth_view.as_view(template_name='Mysite/post_draft_list.html'), name='logout' ),

    

    path('', include('Mysite.urls'))
]
