# -*- coding:utf-8 -*- 

from django.forms import ModelForm
from .models import Blog, Comments

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {                     # 之前form的中'widget'之类的属性，现在写在这里。
            'blogger':'blog owner'
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
