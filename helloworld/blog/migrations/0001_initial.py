# Generated by Django 2.2.2 on 2019-09-02 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'blog',
                'ordering': ['-modified_time'],
                'get_latest_by': ['-modified_time', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_follow_friend', models.BooleanField(default=False)),
                ('friend_follow_user', models.BooleanField(default=False)),
                ('communication_times', models.IntegerField(default=0, null=True)),
                ('follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('comment_at', models.DateTimeField(auto_now=True)),
                ('belong_to_blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment', to='blog.Blog')),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'blog_comments',
                'ordering': ['-comment_at'],
                'get_latest_by': ['comment_at'],
            },
        ),
    ]
