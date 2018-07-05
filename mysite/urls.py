"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import main.views as main_views
import user.views as user_views
import guestbook.views as guestbook_list
import board.views as board_view

urlpatterns = [
    path('', main_views.index),
    path('user/joinform', user_views.joinform),
    path('user/join', user_views.join),
    path('user/joinsuccess',user_views.joinsuccess),
    path('guestbook/',guestbook_list.index),
    path('guestbook/add', guestbook_list.add),
    path('board/list', board_view.list),
    path('board/add',board_view.add),
    path('board/write',board_view.write),
    path('board/view',board_view.view),
    path('board/modify',board_view.modify),



    path('admin/', admin.site.urls)


]
