# Generated by Django 2.0.5 on 2018-11-01 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0020_auto_20181101_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.Student'),
        ),
    ]
