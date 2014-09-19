#coding:utf-8

# Django imports
import django.contrib.auth.models
import django.db.models
import datetime

class Institution (django.db.models.Model):

    #phone, address, email, contact_point, name

class Proyect_Type (django.db.models.Model):

    #name, description

class Permission (django.db.models.Model):

    #title, folio, decription

    #folio = django.db.models.CharField(unique=True, max_length=255, verbose_name=u"Folio")
