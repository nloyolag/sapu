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
from django.http import HttpResponse
from django.utils import timezone

# SAPU imports
import settings
import globals
import forms
import models
import modals

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
                    employee = models.Employee.objects.get(user=user)
                    employee.logged = True
                    employee.save()

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

    template_variables = {}
    delayed = False

    projects = models.Project.objects\
        .filter(is_active=True)\
        .order_by('state__number')

    template_variables['projects'] = projects

    for project in projects:

        stages = models.Stage.objects.filter(project=project)

        for stage in stages:

            if stage.state.number == 1:
                delayed = True
                break

        if delayed and project.state.number == 2:
            project.state = models.State.objects.get(number=1)
            project.save()

        elif not delayed and project.state.number == 1:
            project.state = models.State.objects.get(number=2)
            project.save()

        delayed = False

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__PROJECTS,
        template_context
    )


@login_required
def users_render_view(request):
    template_variables = {}

    employees = None

    try:
        employees = models.Employee.objects.filter(user__is_active=True)
        template_variables = {
            'employees': employees
        }

    except models.ProjectType.DoesNotExist as e:
        messages.error(request, e.messages)

    if request.method == "POST":
        for employee in employees:
            employee.logged = False
            employee.save()

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__USERS,
        template_context
    )


@login_required
def institutions_render_view(request):

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

    template_variables = {}
    stages = None
    delayed = False
    can_complete = True
    project = None

    try:
        project = models.Project.objects.get(pk=project_id)
        stages = models.Stage.objects\
            .filter(project=project, is_active=True)\
            .order_by('-creation_date')
        permissions = models.Permission.objects.filter(project=project, is_active=True)
        template_variables = {
            'stages': stages,
            'project': project,
            'permissions': permissions
        }

    except models.Stage.DoesNotExist as e:
        messages.error(request, e.messages)

    # Validate project state change form submission

    if request.method == "POST":
        form_state_project = forms.ModelFormStateProject(request.POST)

        if form_state_project.is_valid():
            state = form_state_project.cleaned_data['state']

            if state.number == 5:  # Completed

                for stage in stages:
                    if stage.state.number != 5:
                        can_complete = False
                        break

                if can_complete:
                    project.state = models.State.objects.get(number=5)
                    project.save()

                else:
                    messages.error(request, globals.ERROR__STAGES_ARE_NOT_COMPLETE)

            else:
                project.state = models.State.objects.get(number=state.number)
                project.save()

    else:
        form_state_project = forms.ModelFormStateProject()

    # Check datetimes to set projects and stages to delayed or on time

    for stage in stages:

        if stage.state.number == 1:
            delayed = True

        if stage.deadline < timezone.now() and stage.state.number == 2:
            stage.state = models.State.objects.get(number=1)
            stage.save()

        elif stage.deadline > timezone.now() and stage.state.number == 1:
            stage.state = models.State.objects.get(number=2)
            stage.save()

    if delayed and project.state.number == 2:
        project.state = models.State.objects.get(number=1)
        project.save()

    elif not delayed and project.state.number == 1:
        project.state = models.State.objects.get(number=2)
        project.save()

    template_variables['form_state_project'] = form_state_project

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__STAGES,
        template_context
    )


@login_required
def stage_detail_render_view(request, project_id, stage_id):

    template_variables = {}
    current_user_in_stage = False
    employees = None
    stage = None
    stage_completed = True

    try:
        project = models.Project.objects.get(pk=project_id)
        stage = models.Stage.objects.get(pk=stage_id)
        comments = models.Comment.objects.filter(stage=stage, is_active=True)
        tasks = models.Task.objects.filter(stage=stage, is_active=True)
        employees = stage.employee.all()
        assignments = models.Assignment.objects.filter(stage=stage)

        template_variables = {
            'comments': comments,
            'tasks': tasks,
            'stage': stage,
            'project': project,
            'employees': employees,
            'assignments': assignments
        }

    except models.Stage.DoesNotExist as e:
        messages.error(request, e.messages)

    for employee in employees:
        if employee.user.id == request.user.id:
            current_user_in_stage = True
            break

    template_variables['current_user_in_stage'] = current_user_in_stage

    # Check state form submission

    if request.method == "POST":
        form_state_stage = forms.ModelFormStateStage(request.POST)

        if form_state_stage.is_valid():
            state = form_state_stage.cleaned_data['state']

            if state.number == 5:  # Completed

                submit_employee = models.Employee.objects.get(user=request.user)
                assignment = models.Assignment.objects.get(employee=submit_employee, stage=stage)
                assignment.completed = True
                assignment.save()

                for employee in employees:
                    assignment = models.Assignment.objects.get(employee=employee, stage=stage)

                    if not assignment.completed:
                        stage_completed = False
                        break

                if stage_completed:  # All employees set stage as finished, stage is completed
                    stage.state = models.State.objects.get(number=state.number)
                    stage.save()

            elif stage.state.number == 5 and state.number != 5:  # Quitting completed status

                submit_employee = models.Employee.objects.get(user=request.user)
                assignment = models.Assignment.objects.get(employee=submit_employee, stage=stage)
                assignment.completed = False
                assignment.save()
                stage.state = models.State.objects.get(number=state.number)
                stage.save()

            else:
                stage.state = models.State.objects.get(number=state.number)
                stage.save()

    else:
        form_state_stage = forms.ModelFormStateStage()

    template_variables['form_state_stage'] = form_state_stage

    # Check current state with datetime

    if stage.deadline < timezone.now() and stage.state.number == 2:
        stage.state = models.State.objects.get(number=1)
        stage.save()

    elif stage.deadline > timezone.now() and stage.state.number == 1:
        stage.state = models.State.objects.get(number=2)
        stage.save()

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    return django.shortcuts.render_to_response(
        globals.TEMPLATE__STAGE_DETAIL,
        template_context
    )


@login_required
def check_task_view(
        request,
        task_id
):
    task = models.Task.objects.get(pk=task_id)

    if task.is_complete:
        task.is_complete = False
    else:
        task.is_complete = True
        task.finished_date = timezone.now()

    task.save()

    return HttpResponse('')


@login_required
def generic_modal(
        request,
        modal_action,
        modal_element,
        element_index=None,
        project_id=None,
        stage_id=None
):

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
                element_index=element_index,
                project_id=project_id,
                stage_id=stage_id
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
    template_variables['project_id'] = project_id
    template_variables['stage_id'] = stage_id

    template_context =\
        django.template.context.RequestContext(request, template_variables)

    if modal_element == globals.PREFIX__FORM_PROJECT_PHOTO and request.method == "POST":
        return projects_render_view(request)

    elif modal_element == globals.PREFIX__FORM_EMPLOYEE_PHOTO and request.method == "POST":
        return users_render_view(request)

    else:
        return django.shortcuts.render_to_response(
            globals.TEMPLATE__MODAL,
            template_context
        )


@login_required
@permission_required('sapu.delete_institution')
def delete_institution_view(request, institution_id):

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

    return HttpResponse('')


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_projecttype')
def delete_project_type_view(request, project_type_id):

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

    return HttpResponse('')


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_project')
def delete_project_view(request, project_id):

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

    return HttpResponse('')


@django.contrib.auth.decorators.login_required
def delete_permission_view(request, permission_id):

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

    return HttpResponse('')


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_employee')
def delete_employee_view(request, employee_id):

    try:

        employee = models.Employee.objects.get(pk=employee_id)
        employee.user.is_active = False
        employee.user.save()
        messages.success(request,
                         u"El usuario " +
                         unicode(employee.user) +
                         u" ha sido eliminado.")

    except models.Employee.DoesNotExist as e:

        messages.error(request, e.messages)

    return HttpResponse('')


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_stage')
def delete_stage_view(request, stage_id):

    stage = models.Stage.objects.get(pk=stage_id)
    deleted_stage_number = stage.number
    project = stage.project

    count = models.Stage.objects.filter(project=project, is_active=True).count()
    stage.is_active = False
    stage.save()

    for i in range(deleted_stage_number + 1, count + 1):
        current_stage = models.Stage.objects.get(project=project, number=i, is_active=True)
        if current_stage is not None:
            current_stage.number = i - 1
            current_stage.save()

    messages.success(request,
                     u"La etapa " +
                     unicode(stage.name) +
                     u" ha sido eliminada.")

    return HttpResponse('')


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_task')
def delete_task_view(request, task_id):

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

    return HttpResponse('')


@django.contrib.auth.decorators.login_required
@permission_required('sapu.delete_comment')
def delete_comment_view(request, comment_id):

    try:

        comment = models.Comment.objects.get(pk=comment_id)
        comment.is_active = False
        comment.save()
        messages.success(request,
                         u"La tarea " +
                         unicode(comment.title) +
                         u" ha sido eliminada.")

    except models.Comment.DoesNotExist as e:

        messages.error(request, e.messages)

    return HttpResponse('')


@django.contrib.auth.decorators.login_required
def delete_assignment_view(request, assignment_id):

    try:

        assignment = models.Assignment.objects.get(pk=assignment_id)
        assignment.delete()

        messages.success(request,
                         u"La asignación ha sido eliminada.")

    except models.Assignment.DoesNotExist as e:

        messages.error(request, e.messages)

    return HttpResponse('')