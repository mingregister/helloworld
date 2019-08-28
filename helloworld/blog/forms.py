# -*- coding:utf-8 -*- 

from django.forms import ModelForm
# from django.contrib.auth.models import User
from accounts.models import User
from django.db.models import Q

from .models import Blog, Comments, Follow
# # 不能再从views中导入了，会导致交叉引用问题.
# from .views import FollowView

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
        # user = self.fields['user'].queryset.filter(username='zmhuang')
        # # 这里现在只能返回一个用户，因为views.FollowView.get_form()限制了queryset的值
        # user = self.fields['user'].queryset.all()

        # 从FollowView.get_form()中获取到此属性
        current_user = self.current_user

        the_users_id_i_have_follow = Follow.objects.filter(user_id=current_user.id)

        the_user_id_i_will_follow = None

        # isFollow = Follow.objects.filter(user_id=current_user.id).get(id=the_user_id_i_will_follow)

        if the_user_id_i_will_follow in the_users_id_i_have_follow:
        # if isFollow is not None:
            # 你已经关注过这个用户了,不需要再关注了。
            return True
        return False



