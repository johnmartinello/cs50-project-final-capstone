# Generated by Django 4.1.5 on 2023-05-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0008_post_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='filec',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
