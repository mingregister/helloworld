# Generated by Django 2.2.2 on 2019-08-29 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190829_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='communication_times',
            field=models.IntegerField(default=0, null=True),
        ),
    ]