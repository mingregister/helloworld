# Generated by Django 2.2.2 on 2019-08-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=20)),
                ('delivery_time', models.DateField()),
            ],
            options={
                'db_table': 'demoaversion',
            },
        ),
    ]
