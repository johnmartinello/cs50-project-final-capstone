# Generated by Django 4.1.5 on 2023-06-06 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0016_rename_members_course_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='description',
        ),
    ]
