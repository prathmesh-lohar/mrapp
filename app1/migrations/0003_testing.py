# Generated by Django 4.0.2 on 2022-03-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220222_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rollno', models.IntegerField()),
            ],
        ),
    ]