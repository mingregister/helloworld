from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User

# Create your models here.

class Blog(models.Model):
    # blogger = models.CharField(max_length=50)
    # # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.related_name
    blogger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    title = models.TextField(max_length=200, blank=False, null=False)
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    body = models.TextField()

    def __str__(self):
        # return ": ".join([self.blogger, self.title])
        return self.title

    class Meta:
        db_table = 'blog'
        ordering = ['-modified_time']
        get_latest_by =  ['-modified_time', '-create_time']


class Comments(models.Model):
    content = models.TextField()
    comment_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    belong_to_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment', null=True)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')

    def __str__(self):
        return self.content

    # SAVE METHOD
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        # do_something_else()

    # # ABSOLUTE URL METHOD
    # def get_absolute_url(self):
    #     return reverse('blog-index', kwargs={'pk': self.id})

    class Meta:
        db_table = 'blog_comments'
        ordering = ['-comment_at']
        get_latest_by = ['comment_at'] 


# https://blog.csdn.net/Curry_chicken/article/details/79809078
# 关注是针对于User模型的，一个用户可以关注多个用户，一个用户也可以被多个用户关注，属于多对多关系。
# 而且这个关系的两边是同一个模型,都是User。所以采用一个中间表来实现。
class Follow(models.Model):
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follow_user")
    # user为用户主体，即关注人本身。
	# 查询用户关注了那些人时: select follow_id where user_id='当前登录用户id';
	# 查询用户有那些粉丝时: select user_id where follow_id='被查询用户id';
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_user")

    user_follow_friend = models.BooleanField(default=False)
    friend_follow_user = models.BooleanField(default=False)
    communication_times = models.IntegerField(default=0,null=True)

    # SAVE METHOD
    def save(self, *args, **kwargs):
        print('i rewrite the save function to print this: before save follow')
        super().save(*args, **kwargs)  # Call the "real" save() method.
        print('i rewrite the save function to print this: after save follow')
        # do_something_else()
    
    def __str__(self):
        # return "follow:{},current_user:{}".format(self.follow, self.user)
        # return self.user.username + self.follow.username + communication_times
        # return self.user.username + self.follow.username
        return ': '.join([self.user.username, self.follow.username])

    @staticmethod
    def get_follow_friends(user):
        return Follow.objects.filter(user=user).filter(user_follow_friend=True)


