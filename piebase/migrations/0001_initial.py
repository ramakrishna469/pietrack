# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(unique=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('email_verified', models.BooleanField(default=False)),
                ('mobile', models.BigIntegerField(blank=True, default='0')),
                ('api_auth_key', models.CharField(max_length=100, default='')),
                ('api_secret_key', models.CharField(max_length=100, default='')),
                ('country', models.CharField(max_length=100, blank=True, default='')),
                ('state', models.CharField(max_length=100, blank=True, default='')),
                ('city', models.CharField(max_length=100, blank=True, default='')),
                ('pincode', models.IntegerField(blank=True, default='0')),
                ('groups', models.ManyToManyField(related_query_name='user', blank=True, to='auth.Group', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', blank=True, to='auth.Permission', verbose_name='user permissions', help_text='Specific permissions for this user.', related_name='user_set')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
