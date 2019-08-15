# Generated by Django 2.2.2 on 2019-08-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blogger', models.CharField(max_length=50)),
                ('title', models.TextField(max_length=200)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('modified_time', models.DateField(auto_now=True)),
                ('body', models.TextField()),
            ],
            options={
                'db_table': 'blog',
                'ordering': ['modified_time'],
                'get_latest_by': ['modified_time', 'create_time'],
            },
        ),
    ]
