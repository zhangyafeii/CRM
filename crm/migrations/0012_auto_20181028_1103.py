# Generated by Django 2.0.5 on 2018-10-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20181027_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentenrollment',
            name='eamil_address',
            field=models.EmailField(default=False, max_length=254),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='emergence_contact',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='现有联系方式'),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='id_num',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='身份证号'),
        ),
        migrations.AlterField(
            model_name='customerinfo',
            name='sex',
            field=models.PositiveIntegerField(blank=True, choices=[(0, '男'), (1, '女')], null=True, verbose_name='性别'),
        ),
    ]