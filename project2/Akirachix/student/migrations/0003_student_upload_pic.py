# Generated by Django 2.2.1 on 2019-06-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='upload_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]