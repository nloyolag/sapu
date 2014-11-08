# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\xbfEst\xe1 activo?')),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('description', models.TextField(verbose_name='Descripci\xf3n')),
                ('date', models.DateTimeField(verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'photos/users', verbose_name='Foto')),
                ('user', models.OneToOneField(related_name='employee', on_delete=django.db.models.deletion.PROTECT, verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=255, verbose_name='Tel\xe9fono')),
                ('address', models.CharField(max_length=255, verbose_name='Direcci\xf3n')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('is_client', models.BooleanField(default=None, verbose_name='\xbfEs cliente?')),
                ('contact_point', models.CharField(max_length=255, verbose_name='Punto de Contacto')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('is_active', models.BooleanField(default=True, verbose_name='\xbfEst\xe1 activo?')),
            ],
            options={
                'verbose_name': 'Instituci\xf3n',
                'verbose_name_plural': 'Instituciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripci\xf3n')),
                ('folio', models.CharField(max_length=255, verbose_name='Folio')),
                ('is_active', models.BooleanField(default=True, verbose_name='\xbfEst\xe1 activo?')),
                ('institution', models.ForeignKey(related_name='permission_institution', on_delete=django.db.models.deletion.PROTECT, verbose_name='Instituci\xf3n', to='sapu.Institution')),
            ],
            options={
                'verbose_name': 'Permiso',
                'verbose_name_plural': 'Permisos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_id', models.CharField(max_length=255, verbose_name='ID de Proyecto')),
                ('creation_date', models.DateTimeField(verbose_name='Fecha de creaci\xf3n')),
                ('deadline', models.DateTimeField(verbose_name='Fecha l\xedmite')),
                ('is_active', models.BooleanField(default=True, verbose_name='\xbfEst\xe1 activo?')),
                ('name', models.CharField(max_length=150, verbose_name='Proyecto')),
                ('photo', models.ImageField(upload_to=b'photos/projects', verbose_name='Foto')),
                ('description', models.CharField(max_length=255, verbose_name=b'Descripci\xc3\xb3n')),
                ('folio', models.CharField(max_length=255, verbose_name='Folio de oficio de solicitud')),
                ('institution', models.ForeignKey(related_name='project_institution', on_delete=django.db.models.deletion.PROTECT, verbose_name='Instituci\xf3n', to='sapu.Institution')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripci\xf3n')),
                ('is_active', models.BooleanField(default=True, verbose_name='\xbfEst\xe1 activo?')),
            ],
            options={
                'verbose_name': 'Tipo de Proyecto',
                'verbose_name_plural': 'Tipos de Proyecto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, verbose_name=b'Descripci\xc3\xb3n')),
                ('number', models.IntegerField(verbose_name=b'N\xc3\xbamero')),
                ('is_active', models.BooleanField(default=True, verbose_name='\xbfEst\xe1 activo?')),
                ('deadline', models.DateTimeField(verbose_name='Fecha L\xedmite')),
                ('employee', models.ManyToManyField(related_name='stage_employees', verbose_name='Empleados', to='sapu.Employee', blank=True)),
                ('project', models.ForeignKey(related_name='stage_project', on_delete=django.db.models.deletion.PROTECT, verbose_name='Proyecto', to='sapu.Project')),
            ],
            options={
                'verbose_name': 'Etapa',
                'verbose_name_plural': 'Etapas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255, verbose_name=b'Descripci\xc3\xb3n')),
                ('color', models.CharField(max_length=7)),
                ('is_active', models.BooleanField(default=True, verbose_name='\xbfEst\xe1 activo?')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='\xbfEst\xe1 activo?')),
                ('title', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('deadline', models.DateTimeField(verbose_name='Fecha L\xedmite')),
                ('finished_date', models.DateTimeField(verbose_name='Fecha de Completitud')),
                ('is_complete', models.BooleanField(default=None, verbose_name='\xbfEst\xe1 completada?')),
                ('employee', models.ForeignKey(related_name='task_employee', on_delete=django.db.models.deletion.PROTECT, verbose_name='Empleado', to='sapu.Employee')),
                ('stage', models.ForeignKey(related_name='task_stage', on_delete=django.db.models.deletion.PROTECT, verbose_name='Etapa', to='sapu.Stage')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stage',
            name='state',
            field=models.ForeignKey(related_name='stage_state', on_delete=django.db.models.deletion.PROTECT, verbose_name='Estado', to='sapu.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(related_name='project_project_type', on_delete=django.db.models.deletion.PROTECT, verbose_name='Tipo de Proyecto', to='sapu.ProjectType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='state',
            field=models.ForeignKey(related_name='project_state', on_delete=django.db.models.deletion.PROTECT, verbose_name='Estado', to='sapu.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='permission',
            name='project',
            field=models.ForeignKey(related_name='permission_project', on_delete=django.db.models.deletion.PROTECT, verbose_name='Proyecto', to='sapu.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='employee',
            field=models.ForeignKey(related_name='comment_employee', on_delete=django.db.models.deletion.PROTECT, verbose_name='Empleado', to='sapu.Employee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='stage',
            field=models.ForeignKey(related_name='comment_stage', on_delete=django.db.models.deletion.PROTECT, verbose_name='Etapa', to='sapu.Stage'),
            preserve_default=True,
        ),
    ]
