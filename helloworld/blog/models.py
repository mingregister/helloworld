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

    class Meta:
        db_table = 'blog_comments'
        ordering = ['-comment_at']
        get_latest_by = ['comment_at'] 
