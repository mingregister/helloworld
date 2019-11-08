
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='tools-index'), # it can not be write as '/'
    # path('f1', views.function1, name='tools-f1'), 
    path('f1', views.uploadFile, name='tools-f1'), 
    path('uploadFile', views.FileFieldView.as_view(), name='tools-uploadFile'), 
    path('f2', views.function2, name='tools-f2'), 
    path('f3', views.function3, name='tools-f3'), 
]
