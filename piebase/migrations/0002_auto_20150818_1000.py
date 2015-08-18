# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import piebase.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('piebase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('attached_file', models.FileField(max_length=500, upload_to=piebase.models.url, null=True, verbose_name='attached file', blank=True)),
                ('order', models.IntegerField(default=0, verbose_name='order')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('attachments', models.ManyToManyField(to='piebase.Attachment', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='name', db_index=True)),
                ('slug', models.SlugField(max_length=250, verbose_name='slug', blank=True)),
                ('estimated_start', models.DateField(verbose_name='estimated start date')),
                ('estimated_finish', models.DateField(verbose_name='estimated finish date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date')),
                ('status', models.CharField(default=b'planned', max_length=200, choices=[(b'planned', b'Planned'), (b'started', b'Started'), (b'finished', b'Finished')])),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug', blank=True)),
                ('color', models.CharField(default=b'#999999', max_length=20, verbose_name='color')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(unique=True, max_length=250, verbose_name='slug', blank=True)),
                ('description', models.TextField(verbose_name='description')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date')),
                ('logo', models.ImageField(null=True, upload_to=piebase.models.url, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(max_length=250, verbose_name='slug', blank=True)),
                ('description', models.TextField(verbose_name='description')),
                ('milestone', models.ForeignKey(related_name='requirements', to='piebase.Milestone', null=True)),
                ('project', models.ForeignKey(related_name='requirements', verbose_name='project', to='piebase.Project', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(max_length=250, verbose_name='slug', blank=True)),
                ('project', models.ForeignKey(related_name='roles', verbose_name='project', to='piebase.Project', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Severity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug', blank=True)),
                ('color', models.CharField(default=b'#999999', max_length=20, verbose_name='color')),
                ('project', models.ForeignKey(related_name='severities', verbose_name='project', to='piebase.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('slug', models.SlugField(max_length=250, verbose_name='slug', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('modified_date', models.DateTimeField(verbose_name='modified date')),
                ('finished_date', models.DateTimeField(null=True, verbose_name='finished date', blank=True)),
                ('order', models.IntegerField(default=1)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('ticket_type', models.CharField(max_length=50)),
                ('target_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug', blank=True)),
                ('color', models.CharField(default=b'#999999', max_length=20, verbose_name='color')),
                ('project', models.ForeignKey(related_name='task_statuses', verbose_name='project', to='piebase.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('namespace', models.CharField(default=b'default', max_length=250, db_index=True)),
                ('event_type', models.CharField(max_length=250, db_index=True)),
                ('data', models.TextField(verbose_name='data', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(related_name='content_type_timelines', to='contenttypes.ContentType')),
                ('data_content_type', models.ForeignKey(related_name='data_timelines', to='contenttypes.ContentType')),
                ('project', models.ForeignKey(to='piebase.Project', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='api_auth_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='api_secret_key',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='attachments',
            field=models.ManyToManyField(to='piebase.Attachment', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='milestone',
            field=models.ForeignKey(related_name='tasks', default=None, blank=True, to='piebase.Milestone', null=True, verbose_name='milestone'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='priority',
            field=models.ForeignKey(related_name='priority_tickets', verbose_name='priority', blank=True, to='piebase.Priority', null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='project',
            field=models.ForeignKey(related_name='project_tickets', verbose_name='project', to='piebase.Project'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='reference',
            field=models.ManyToManyField(related_name='reference_rel_+', null=True, to='piebase.Ticket', blank=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='requirement',
            field=models.ForeignKey(related_name='tasks', default=None, blank=True, to='piebase.Requirement', null=True, verbose_name='milestone'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='severity',
            field=models.ForeignKey(related_name='severity_tickets', verbose_name='severity', blank=True, to='piebase.Severity', null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.ForeignKey(related_name='tickets', verbose_name='status', blank=True, to='piebase.TicketStatus', null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='users',
            field=models.ManyToManyField(related_name='user_roles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='priority',
            name='project',
            field=models.ForeignKey(related_name='priorities', verbose_name='project', to='piebase.Project'),
        ),
        migrations.AddField(
            model_name='milestone',
            name='project',
            field=models.ForeignKey(related_name='milestones', verbose_name='project', to='piebase.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commented_by',
            field=models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(related_name='ticket_comments', to='piebase.Ticket'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='project',
            field=models.ForeignKey(to='piebase.Project'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterIndexTogether(
            name='timeline',
            index_together=set([('content_type', 'object_id', 'namespace')]),
        ),
        migrations.AlterUniqueTogether(
            name='ticketstatus',
            unique_together=set([('project', 'slug'), ('project', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='severity',
            unique_together=set([('project', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=set([('slug', 'project')]),
        ),
        migrations.AlterUniqueTogether(
            name='priority',
            unique_together=set([('project', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='milestone',
            unique_together=set([('slug', 'project'), ('name', 'project')]),
        ),
    ]
