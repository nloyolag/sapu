#coding:utf-8

# Django imports
import django.contrib.admin

# SAPU imports
import models


django.contrib.admin.site.register(models.Project)
django.contrib.admin.site.register(models.ProjectType)
django.contrib.admin.site.register(models.Institution)
django.contrib.admin.site.register(models.Stage)
django.contrib.admin.site.register(models.State)
django.contrib.admin.site.register(models.Permission)
django.contrib.admin.site.register(models.Employee)
django.contrib.admin.site.register(models.Comment)
django.contrib.admin.site.register(models.Task)

