# -*- coding:utf-8 -*- 

from django.forms import ModelForm
# from django.contrib.auth.models import User
from accounts.models import User

from .models import Blog, Comments, Follow
# from .views import FollowView
# from .views import myView 

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

class FollowForm(ModelForm):

    class Meta:
        model = Follow
        # # 这个fields在某种程度上会决定self.fields有什么内容
        # # 在这里，user对应的是django.forms.models.ModelChoiceField，所以它也有queryset属性
        # # https://docs.djangoproject.com/en/2.2/ref/forms/fields/#modelchoicefield
        # fields = ['user']
        fields = '__all__'

    # # just as a example
    # # https://github.com/jumpserver/jumpserver/blob/master/apps/assets/forms/asset.py
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # 重写其他字段为不再required
    #     for name, field in self.fields.items():
    #         if name != 'assets':
    #             field.required = False

    def is_valid(self):
        """Return True if the form has no errors, or False otherwise."""
        return self.is_bound and not self.errors and not self.is_follow()

    def is_follow(self):
        user = self.fields['user']
        print('#################')
        print(type(self.fields))
        print('###################')
        print(self.fields)
        # return False
        return FollowView.is_follow()


