# Generated by Django 4.0.3 on 2022-03-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_mr_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dr_user',
            name='profile_pic',
            field=models.CharField(default='', max_length=255),
        ),
    ]