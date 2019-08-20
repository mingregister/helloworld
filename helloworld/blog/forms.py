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

    # def __init__(self, *args, userid=None, **kwargs):
    def __init__(self, *args, **kwargs):
        # try:
        #     userid = kwargs.pop('userid')
        # except: 
        #     pass

        userid = kwargs.get('userid', None)
        if userid is not None:
            # 如果‘userid’不为None，说明userid已经存在了，把userid给pop出来.
            _x = kwargs.pop('userid')

        super(BlogForm, self).__init__(*args, **kwargs)

        if userid is not None:
            self.fields['blogger'].queryset = User.objects.filter(id=userid)
        # try:
        #     self.fields['blogger'].queryset = User.objects.filter(id=userid)
        # except: 
        #     pass
    

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'

