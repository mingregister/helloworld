from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Version(models.Model):
    version = models.CharField(max_length=20)
    delivery_time = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        db_table = 'demoaversion'

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.ForeignKey.related_name
    # 一对多关系[一个Board对应0-*个Topic]，外键定义在*多(Topic)*的一方。
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

class Post(models.Model):
    message = models.TextField(max_length=4000)
    # 一对多关系[一个Topic对应1-*个Post]，外键定在*多(Post)*的一方
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')



