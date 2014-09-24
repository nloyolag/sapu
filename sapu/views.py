#coding:utf-8

# Python imports
import os
import datetime

# Django imports
import django.core.exceptions
import django.core.servers.basehttp
import django.core.urlresolvers
import django.core.paginator
import django.contrib.auth
import django.contrib.auth.decorators
import django.contrib.auth.forms
import django.core.mail
import django.http
import django.shortcuts
import django.utils.encoding
import django.template.context
import django.contrib.auth.models
from django.contrib.auth.models import User

# SAPU imports
import settings
import forms
import models


# Functions that render the views of the application

def action_login(request):
    pass


def action_logout(request):
    pass


def login_render_view(request):
    pass


@django.contrib.auth.decorators.login_required
def users_render_view(request):
    pass


@django.contrib.auth.decorators.login_required
def institutions_render_view(request):
    pass


@django.contrib.auth.decorators.login_required
def project_type_render_view(request):
    pass


@django.contrib.auth.decorators.login_required
def stages_render_view(request):
    pass


@django.contrib.auth.decorators.login_required
def stage_detail_render_view(request):
    pass