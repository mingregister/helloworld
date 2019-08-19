# -*- coding:utf-8 -*- 

from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Blog, Comments

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # exclude = ['blogger']
        labels = {                     # 之前form的中'widget'之类的属性，现在写在这里。
            'blogger':'blog owner'
        }
    def __init__(self, *args, **kwargs):
        try:
            userid = kwargs.pop('userid')
        except: 
            pass
        super(BlogForm, self).__init__(*args, **kwargs)
        try:
            self.fields['blogger'].queryset = User.objects.filter(id=userid)
        except: 
            pass
    
    # def limit_queryset_userid(self):
    #     try:
    #         self.userid = kwargs.pop('userid')
    #     except: 
    #         pass
        


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
