# Generated by Django 4.1.5 on 2023-03-21 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_delete_enter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]