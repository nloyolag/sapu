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
from django.contrib import messages

# SAPU imports
import settings
import globals
import forms
import models


# Functions that render the views of the application

def action_login(request):

    if request.method == "POST":

        # Get and validate the login form
        form_login =\
            django.contrib.auth.forms.AuthenticationForm(data=request.POST)

        if form_login.is_valid():

            #Authenticate the user
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']

            user =\
                django.contrib.auth.authenticate(
                    username=username,
                    password=password
                )

            if user is not None:

                # Verify if the user is active
                if user.is_active:

                    # Login and redirect to projects view
                    django.contrib.auth.login(request, user)

                    redirect_url =\
                        request.POST.get('redirect_url',
                                         settings.LOGIN_REDIRECT_URL)

                    return django.shortcuts.redirect(redirect_url)

                else:
                    messages.error(request, globals.ERROR__USER_NOT_ACTIVE)

            else:
                messages.error(request, globals.ERROR__INVALID_USER_OR_PASSWORD)

        else:

            if 'This account inactive' in unicode(form_login.errors):
                messages.error(request, globals.ERROR__USER_NOT_ACTIVE)

            else:
                messages.error(request, globals.ERROR__INVALID_USER_OR_PASSWORD)

    else:
        messages.error(request, globals.ERROR__NO_POST_DATA)

    # If some step in the authentication process is invalid, redirect to the
    # login page and show the errors.
    return login_render_view(request=request)


def action_logout(request):
    django.contrib.auth.logout(request)
    redirect_url = settings.LOGIN_URL
    return django.http.HttpResponseRedirect(redirect_url)


def login_render_view(request):

    if request.user.is_authenticated():
        return django.http.HttpResponseRedirect(
            django.core.urlresolvers.reverse('projects'))

    template_variables = {}

    redirect_url = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
    form_redirect =\
        forms.FormRedirect(
            initial={'redirect_url': redirect_url})

    template_variables['form_redirect'] = form_redirect

    # Create an empty login form
    form_login = django.contrib.auth.forms.AuthenticationForm()
    form_login.fields['username'].widget.attrs['placeholder'] =\
        globals.FIELD__USERNAME

    form_login.fields['password'].widget.attrs['placeholder'] =\
        globals.FIELD__PASSWORD

    template_variables['form_login'] = form_login
    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__LOGIN,
        template_context
    )


@django.contrib.auth.decorators.login_required
def projects_render_view(request):

    project_query = ''

    if request.method == "POST":

        form_search_project = forms.FormSearchProject(request.POST)
        if form_search_project .is_valid():

            project_query = form_search_project.cleaned_data['name']

    template_variables = {}
    employee = models.Employee.objects.get(user=request.user)

    #TODO Order Projects By States, not deadlines

    if project_query:

        projects = models.Project.objects\
            .filter(name__contains=project_query)\
            .order_by('-deadline')

        template_variables['projects'] = projects
        template_variables['pagination'] = False

    else:

        projects = models.Project.objects\
            .order_by('-deadline')

        paginator = django.core.paginator.Paginator(projects, 10)
        page = request.GET.get('page')

        try:
            requests_page = paginator.page(page)

        except django.core.paginator.PageNotAnInteger:
            requests_page = paginator.page(1)

        except django.core.paginator.EmptyPage:
            requests_page = paginator.page(paginator.num_pages)

        template_variables['projects'] = requests_page
        template_variables['pagination'] = True

    template_variables['form_search_project'] = forms.FormSearchProject()

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__PROJECTS,
        template_context
    )


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