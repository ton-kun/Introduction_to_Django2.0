"""djangoApp URL Configuration

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
# 管理者用の画面呼び出しモジュール
from django.contrib import admin
# 特定のパス以下をアプリケーションに関連付ける
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('hoge/', include('hoge.urls')),
    # パスの引数をviewに投げる
    path('fuga/<foo>', views.fuga),
    path('search', views.search),
    # POST用 path('form', views.render_form),
    path('form', views.form),
    path('login', views.login),
    path('upload', views.upload),
    path('admin/', admin.site.urls)
]
