# Generated by Django 2.0.5 on 2018-10-28 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_userprofile_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlist',
            name='day_nums',
            field=models.PositiveIntegerField(default=10, verbose_name='课程总节次'),
        ),
    ]