"""
URL configuration for YHH47 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.urls import path, include
from django.conf.urls.i18n import urlpatterns
from django.contrib import admin
from django.urls import path

from YHH47.settings import MEDIA_URL

from movie.views import signup
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),#搜索电影
    path("signup/",signup,name='signup'),#注册账号
    path("",include('movie.urls')),#主页面
    path('movie/', include('movie.urls')),
    path('book/', include('book.urls')),
    path('accounts/',include('accounts.urls'),name='accounts')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

