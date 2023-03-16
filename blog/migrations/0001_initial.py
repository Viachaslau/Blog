# Generated by Django 4.1.5 on 2023-02-21 19:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('excerpt', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='static/images/')),
                ('data', models.DateField(default=datetime.datetime.now)),
                ('slug', models.SlugField(blank=True, default='')),
                ('content', models.CharField(max_length=300)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('tag', models.ManyToManyField(to='blog.tag')),
            ],
        ),
    ]
