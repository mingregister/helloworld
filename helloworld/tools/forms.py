# -*- coding:utf-8 -*- 

from django import forms
from django.forms import ModelForm, widgets
# from django.contrib.auth.models import User
from accounts.models import User
from django.db.models import Q

# # 不能再从views中导入了，会导致交叉引用问题.
# from .views import FollowView


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
