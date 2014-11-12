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
import django.contrib.auth.forms
import django.core.mail
import django.http
import django.shortcuts
import django.utils.encoding
import django.template.context
import django.contrib.auth.models
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib import messages

# SAPU imports
import settings
import globals
import forms
import models
import modals


# TODO Create modal edit
# TODO Create modal add
# TODO Apply client corrections
# TODO Fix Create/Update/Delete buttons styles
# TODO Show Create/Edit/Delete buttons only to appropriate groups

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


@login_required
def projects_render_view(request):

    project_query = ''

    if request.method == "POST":

        form_search_project = forms.FormSearchProject(request.POST)
        if form_search_project.is_valid():

            project_query = form_search_project.cleaned_data['name']

    template_variables = {}

    # TODO Order Projects By States, not deadlines
    # TODO Add logic to change project state to delayed (Beware of it overriding finished or cancelled states)
    # TODO Create projects
    # TODO Edit projects
    # TODO Delete projects

    if project_query:

        projects = models.Project.objects\
            .filter(name__icontains=project_query, is_active=True)\
            .order_by('-creation_date')

        template_variables['projects'] = projects
        template_variables['pagination'] = False

    else:

        projects = models.Project.objects\
            .filter(is_active=True)\
            .order_by('-creation_date')

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


@login_required
def users_render_view(request):
    template_variables = {}

    # TODO Check if user logged in at least once
    # TODO Add option (in edit form or separately) to change user permissions
    # TODO Create users
    # TODO Edit users
    # TODO Delete users

    try:
        employees = models.Employee.objects.filter(user__is_active=True)
        template_variables = {
            'employees': employees
        }

    except models.ProjectType.DoesNotExist as e:
        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__USERS,
        template_context
    )


@login_required
def institutions_render_view(request):

    # TODO Refactor template interface
    # TODO Create institutions
    # TODO Edit institutions

    institution_query = ''

    if request.method == "POST":

        form_search_institution = forms.FormSearchProject(request.POST)
        if form_search_institution.is_valid():

            institution_query = form_search_institution.cleaned_data['name']

    template_variables = {}

    if institution_query:

        institutions = models.Institution.objects\
            .filter(name__icontains=institution_query, is_active=True)\
            .order_by('-name')

        template_variables['institutions'] = institutions
        template_variables['pagination'] = False

    else:

        institutions = models.Institution.objects\
            .filter(is_active=True)\
            .order_by('-name')

        paginator = django.core.paginator.Paginator(institutions, 15)
        page = request.GET.get('page')

        try:
            requests_page = paginator.page(page)

        except django.core.paginator.PageNotAnInteger:
            requests_page = paginator.page(1)

        except django.core.paginator.EmptyPage:
            requests_page = paginator.page(paginator.num_pages)

        template_variables['institutions'] = requests_page
        template_variables['pagination'] = True

    template_variables['form_search_institution'] = forms.FormSearchProject()

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__INSTITUTIONS,
        template_context
    )


@login_required
def project_type_render_view(request):

    # TODO Create project_types
    # TODO Edit project_types
    # TODO Delete project_types

    template_variables = {}

    try:
        project_types = models.ProjectType.objects.filter(is_active=True)
        template_variables = {
            'project_types': project_types
        }

    except models.ProjectType.DoesNotExist as e:
        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__PROJECT_TYPES,
        template_context
    )


@login_required
def stages_render_view(request, project_id):

    # TODO Add logic to change project state to delayed (Beware of it overriding finished or cancelled states)
    # TODO Add logic to change stage state to delayed (Beware of it overriding finished or cancelled states)
    # TODO Code button to declare project as complete
    # TODO Code button to cancel project
    # TODO Create stages
    # TODO Edit stages
    # TODO Delete stages
    # TODO Create permissions
    # TODO Edit permissions
    # TODO Delete permissions

    template_variables = {}

    try:
        project = models.Project.objects.get(pk=project_id)
        stages = models.Stage.objects.filter(project=project, is_active=True)
        permissions = models.Permission.objects.filter(project=project, is_active=True)
        template_variables = {
            'stages': stages,
            'project': project,
            'permissions': permissions
        }

    except models.Stage.DoesNotExist as e:
        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__STAGES,
        template_context
    )


@login_required
def stage_detail_render_view(request, project_id, stage_id):

    # TODO Add option to assign or unassign employees to stage
    # TODO Code checkbox to modify is_complete value
    # TODO Separate Tasks from Comments
    # TODO Code buttons for assignees to declare stage as finished
    # TODO Create tasks
    # TODO Edit tasks
    # TODO Delete tasks
    # TODO Create comments
    # TODO Edit comments
    # TODO Delete comments

    template_variables = {}

    try:
        project = models.Project.objects.get(pk=project_id)
        stage = models.Stage.objects.get(pk=stage_id)
        comments = models.Comment.objects.filter(stage=stage, is_active=True)
        tasks = models.Task.objects.filter(stage=stage, is_active=True)
        employees = stage.employee.all()
        template_variables = {
            'comments': comments,
            'tasks': tasks,
            'stage': stage,
            'project': project,
            'employees': employees
        }

    except models.Stage.DoesNotExist as e:
        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__STAGE_DETAIL,
        template_context
    )


@login_required
def generic_modal(request, modal_action, modal_element, element_index=None):

    modal_forms = {}
    template_variables = {}

    if request.method == "POST":

        # Modal Handlers
        handler =\
            modals.MODAL__HANDLER_FUNCTIONS[modal_element]
        if handler is None:
            messages.error(request, globals.ERROR__SERVER_ERROR)
        else:
            modal_forms = handler(
                request=request,
                element_index=element_index
            )

    modal_function =\
        modals.MODAL__FUNCTIONS[modal_element]
    if modal_function is None:
        raise django.http.Http404

    modal = modal_function(modal_name=modal_element,
                           element_index=element_index,
                           modal_forms=modal_forms)

    template_variables['modal'] = modal
    template_variables['element_index'] = element_index

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__MODAL,
        template_context
    )


@login_required
@permission_required('sapu.delete_institution')
def delete_institution_view(request, institution_id):

    # TODO Fix redirection bug on delete functions

    template_variables = {}

    try:

        institution = models.Institution.objects.get(pk=institution_id)
        institution.is_active = False
        institution.save()
        messages.success(request,
                         u"La institución " +
                         unicode(institution.name) +
                         u" ha sido eliminada")

    except models.Institution.DoesNotExist as e:

        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__INSTITUTIONS,
        template_context
    )


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_projecttype')
def delete_project_type_view(request, project_type_id):

    template_variables = {}

    try:

        project_type = models.ProjectType.objects.get(pk=project_type_id)
        project_type.is_active = False
        project_type.save()
        messages.success(request,
                         u"El tipo de proyecto " +
                         unicode(project_type.name) +
                         u" ha sido eliminado.")

    except models.ProjectType.DoesNotExist as e:

        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__PROJECT_TYPES,
        template_context
    )

    pass


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_project')
def delete_project_view(request, project_id):

    template_variables = {}

    try:

        project = models.Project.objects.get(pk=project_id)
        project.is_active = False
        project.save()
        messages.success(request,
                         u"El proyecto " +
                         unicode(project.name) +
                         u" ha sido eliminado.")

    except models.Project.DoesNotExist as e:

        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__PROJECTS,
        template_context
    )

    pass


@django.contrib.auth.decorators.login_required
def delete_permission_view(request, permission_id):

    template_variables = {}

    try:

        permission = models.Permission.objects.get(pk=permission_id)
        permission.is_active = False
        permission.save()
        messages.success(request,
                         u"El permiso " +
                         unicode(permission.title) +
                         u" ha sido eliminado.")

    except models.Permission.DoesNotExist as e:

        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__STAGES,
        template_context
    )

    pass

@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_employee')
def delete_employee_view(request, employee_id):

    template_variables = {}

    try:

        employee = models.Employee.objects.get(pk=employee_id)
        employee.is_active = False
        employee.save()
        messages.success(request,
                         u"El usuario " +
                         unicode(employee.user) +
                         u" ha sido eliminado.")

    except models.Employee.DoesNotExist as e:

        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__USERS,
        template_context
    )

    pass



@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_stage')
def delete_stage_view(request, stage_id):

    template_variables = {}

    try:

        stage = models.Stage.objects.get(pk=stage_id)
        stage.is_active = False
        stage.save()
        messages.success(request,
                         u"La etapa " +
                         unicode(stage.name) +
                         u" ha sido eliminada.")

    except models.Stage.DoesNotExist as e:

        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__STAGES,
        template_context
    )

    pass


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_task')
def delete_task_view(request, task_id):

    template_variables = {}

    try:

        task = models.Task.objects.get(pk=task_id)
        task.is_active = False
        task.save()
        messages.success(request,
                         u"La tarea " +
                         unicode(task.title) +
                         u" ha sido eliminada.")

    except models.Task.DoesNotExist as e:

        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__STAGE_DETAIL,
        template_context
    )

    pass


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_comment')
def delete_comment_view(request, comment_id):

    template_variables = {}

    try:

        comment = models.Comment.objects.get(pk=comment_id)
        comment.is_active = False
        comment.save()
        messages.success(request,
                         u"La tarea " +
                         unicode(comment.title) +
                         u" ha sido eliminada.")

    except models.Task.DoesNotExist as e:

        messages.error(request, e.messages)

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__STAGE_DETAIL,
        template_context
    )

    pass