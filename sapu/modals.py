#coding:utf-8

# Python imports
import datetime

# Django imports
import django.core.exceptions
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# SAPU imports
import forms
import models
import globals


################################################################################
#
# Modal Functions
#
################################################################################

# Functions that help render the modal


def modal_edit_project(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Project was already added/edited
    if globals.PREFIX__FORM_PROJECT in modal_forms:
        # Form was passed as a parameter
        project_form = modal_forms[globals.PREFIX__FORM_PROJECT]

    else:
        # Edit Project
        if element_index is not None:

            try:
                project =\
                    models.Project.objects.get(pk=element_index)

            except models.Project.DoesNotExist:
                return None

            project_form = forms.ModelFormProject(
                prefix=globals.PREFIX__FORM_PROJECT,
                instance=project
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create project
        else:
            project_form = forms.ModelFormProject(prefix=globals.PREFIX__FORM_PROJECT)

    project_modal_form = globals.ModalForm(
        title=globals.FIELD__PROJECT,
        form=project_form
    )

    main_forms = [project_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
    )

    return modal


def modal_edit_project_photo(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Project was already added/edited
    if globals.PREFIX__FORM_PROJECT_PHOTO in modal_forms:
        # Form was passed as a parameter
        project_photo_form = modal_forms[globals.PREFIX__FORM_PROJECT_PHOTO]

    else:
        # Edit Project
        if element_index is not None:

            try:
                project =\
                    models.Project.objects.get(pk=element_index)

            except models.Project.DoesNotExist:
                return None

            project_photo_form = forms.ModelFormProjectPhoto(
                prefix=globals.PREFIX__FORM_PROJECT_PHOTO,
                instance=project
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create project
        else:
            project_photo_form = forms.ModelFormProjectPhoto(prefix=globals.PREFIX__FORM_PROJECT_PHOTO)

    project_modal_form = globals.ModalForm(
        title=globals.FIELD__PHOTO,
        form=project_photo_form
    )

    main_forms = [project_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text,
        accept_button_link="/modal/edit/project_photo/" + element_index
    )

    return modal


def modal_edit_permission(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Permission was already added/edited
    if globals.PREFIX__FORM_PERMISSION in modal_forms:
        # Form was passed as a parameter
        permission_form = modal_forms[globals.PREFIX__FORM_PERMISSION]

    else:
        # Edit Permission
        if element_index is not None:

            try:
                permission =\
                    models.Permission.objects.get(pk=element_index)

            except models.Permission.DoesNotExist:
                return None

            permission_form = forms.ModelFormPermission(
                prefix=globals.PREFIX__FORM_PERMISSION,
                instance=permission
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create permission
        else:
            permission_form = forms.ModelFormPermission(prefix=globals.PREFIX__FORM_PERMISSION)

    permission_modal_form = globals.ModalForm(
        title=globals.FIELD__PERMISSION,
        form=permission_form
    )

    main_forms = [permission_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
    )

    return modal


def modal_edit_stage(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Stage was already added/edited
    if globals.PREFIX__FORM_STAGE in modal_forms:
        # Form was passed as a parameter
        stage_form = modal_forms[globals.PREFIX__FORM_STAGE]

    else:
        # Edit Stage
        if element_index is not None:

            try:
                stage =\
                    models.Stage.objects.get(pk=element_index)

            except models.Stage.DoesNotExist:
                return None

            stage_form = forms.ModelFormStage(
                prefix=globals.PREFIX__FORM_STAGE,
                instance=stage
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create stage
        else:
            stage_form = forms.ModelFormStage(prefix=globals.PREFIX__FORM_STAGE)

    stage_modal_form = globals.ModalForm(
        title=globals.FIELD__STAGE,
        form=stage_form
    )

    main_forms = [stage_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
    )

    return modal


def modal_edit_task(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Task was already added/edited
    if globals.PREFIX__FORM_TASK in modal_forms:
        # Form was passed as a parameter
        task_form = modal_forms[globals.PREFIX__FORM_TASK]

    else:
        # Edit Task
        if element_index is not None:

            try:
                task =\
                    models.Task.objects.get(pk=element_index)

            except models.Task.DoesNotExist:
                return None

            task_form = forms.ModelFormTask(
                prefix=globals.PREFIX__FORM_TASK,
                instance=task
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create task
        else:
            task_form = forms.ModelFormTask(prefix=globals.PREFIX__FORM_TASK)

    task_modal_form = globals.ModalForm(
        title=globals.FIELD__TASK,
        form=task_form
    )

    main_forms = [task_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
    )

    return modal


def modal_edit_comment(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Comment was already added/edited
    if globals.PREFIX__FORM_COMMENT in modal_forms:
        # Form was passed as a parameter
        comment_form = modal_forms[globals.PREFIX__FORM_COMMENT]

    else:
        # Edit Comment
        if element_index is not None:

            try:
                comment =\
                    models.Comment.objects.get(pk=element_index)

            except models.Comment.DoesNotExist:
                return None

            comment_form = forms.ModelFormComment(
                prefix=globals.PREFIX__FORM_COMMENT,
                instance=comment
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create comment
        else:
            comment_form = forms.ModelFormComment(prefix=globals.PREFIX__FORM_COMMENT)

    comment_modal_form = globals.ModalForm(
        title=globals.FIELD__COMMENT,
        form=comment_form
    )

    main_forms = [comment_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
    )

    return modal


def modal_edit_employee(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Employee was already added/edited
    if globals.PREFIX__FORM_USER in modal_forms:
        # Form was passed as a parameter
        user_form = modal_forms[globals.PREFIX__FORM_USER]
        password_form = modal_forms[globals.PREFIX__FORM_PASSWORD_CHANGE]

    else:
        # Edit Employee
        if element_index is not None:

            try:
                employee =\
                    models.Employee.objects.get(pk=element_index)
                user =\
                    employee.user

            except models.Employee.DoesNotExist:
                return None

            except User.DoesNotExist:
                return None

            user_form = forms.ModelFormEditUser(
                prefix=globals.PREFIX__FORM_USER,
                instance=user
            )

            password_form = forms.FormPasswordChange(
                prefix=globals.PREFIX__FORM_PASSWORD_CHANGE
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create employee
        else:
            user_form = forms.ModelFormUser(prefix=globals.PREFIX__FORM_USER)
            password_form = None

    user_modal_form = globals.ModalForm(
        form=user_form
    )

    password_modal_form = globals.ModalForm(
        form=password_form
    )

    main_forms = [user_modal_form, password_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
    )

    return modal


def modal_edit_employee_photo(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Employee was already added/edited
    if globals.PREFIX__FORM_EMPLOYEE_PHOTO in modal_forms:
        # Form was passed as a parameter
        employee_form = modal_forms[globals.PREFIX__FORM_EMPLOYEE_PHOTO]

    else:
        # Edit Employee
        if element_index is not None:

            try:
                employee =\
                    models.Employee.objects.get(pk=element_index)

            except models.Employee.DoesNotExist:
                return None

            employee_form = forms.ModelFormEmployee(
                prefix=globals.PREFIX__FORM_EMPLOYEE_PHOTO,
                instance=employee
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create project
        else:
            employee_form = forms.ModelFormEmployee(prefix=globals.PREFIX__FORM_EMPLOYEE_PHOTO)

    employee_modal_form = globals.ModalForm(
        title=globals.FIELD__PHOTO,
        form=employee_form
    )

    main_forms = [employee_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text,
        accept_button_link="/modal/edit/employee_photo/" + element_index
    )

    return modal


def modal_edit_institution(
        modal_name,
        element_index=None,
        modal_forms=None
):

    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Institution was already added/edited
    if globals.PREFIX__FORM_INSTITUTION in modal_forms:
        # Form was passed as a parameter
        institution_form = modal_forms[globals.PREFIX__FORM_INSTITUTION]

    else:
        # Edit Institution
        if element_index is not None:

            try:
                institution =\
                    models.Institution.objects.get(pk=element_index)

            except models.Institution.DoesNotExist:
                return None

            institution_form = forms.ModelFormInstitution(
                prefix=globals.PREFIX__FORM_INSTITUTION,
                instance=institution
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create institution
        else:
            institution_form = forms.ModelFormInstitution(prefix=globals.PREFIX__FORM_INSTITUTION)

    institution_modal_form = globals.ModalForm(
        title=globals.FIELD__INSTITUTION,
        form=institution_form
    )

    main_forms = [institution_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
    )

    return modal


def modal_edit_project_type(
        modal_name,
        element_index=None,
        modal_forms=None
):
    # Construct the modal
    action_text = globals.MODAL_ACTION__CREATE
    modal_action = globals.OPTION_NAME__MODAL_FORM_ADD

    # Project Type was already added/edited
    if globals.PREFIX__FORM_PROJECT_TYPE in modal_forms:
        # Form was passed as a parameter
        project_type_form = modal_forms[globals.PREFIX__FORM_PROJECT_TYPE]

    else:
        # Edit Project Type
        if element_index is not None:
            try:
                project_type =\
                    models.ProjectType.objects.get(pk=element_index)

            except models.ProjectType.DoesNotExist:
                return None

            project_type_form = forms.ModelFormProjectType(
                prefix=globals.PREFIX__FORM_PROJECT_TYPE,
                instance=project_type
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create project type
        else:
            project_type_form = forms.ModelFormProjectType(prefix=globals.PREFIX__FORM_PROJECT_TYPE)

    project_type_modal_form = globals.ModalForm(
        title=globals.FIELD__PROJECT_TYPE,
        form=project_type_form
    )

    main_forms = [project_type_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
    )

    return modal


################################################################################
#
# Modal Handlers
#
################################################################################

# Functions that handle database modifications made with modals

def modal_edit_project_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_project = None

    if element_index:

        try:
            old_project = models.Project.objects.get(pk=element_index)
        except models.Project.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_project = forms.ModelFormProject(
            request.POST,
            prefix=globals.PREFIX__FORM_PROJECT,
            instance=old_project
        )

    else:
        # Get the form for new element
        form_project = forms.ModelFormProject(
            request.POST,
            prefix=globals.PREFIX__FORM_PROJECT
        )

    if form_project.is_valid():

        project = form_project.save(commit=False)

        try:
            # Save the new object or update it

            if not element_index:
                project.creation_date = datetime.datetime.now()

            project.full_clean()
            project.save()

            if not old_project:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__PROJECT,
                    item_name=project.name
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__PROJECT,
                    item_name=project.name
                ))

        except models.Project.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_PROJECT: form_project
    }

    return forms_handler


def modal_edit_project_photo_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_project = None

    if element_index:

        try:
            old_project = models.Project.objects.get(pk=element_index)
        except models.Project.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_project_photo = forms.ModelFormProjectPhoto(
            request.POST,
            request.FILES,
            prefix=globals.PREFIX__FORM_PROJECT_PHOTO,
            instance=old_project
        )

    else:
        # Get the form for new element
        form_project_photo = forms.ModelFormProjectPhoto(
            request.POST,
            request.FILES,
            prefix=globals.PREFIX__FORM_PROJECT
        )

    if form_project_photo.is_valid():

        project_photo = form_project_photo.save(commit=False)

        try:
            # Save the new object or update it

            if 'project_photo-photo' in request.FILES:
                project_photo.full_clean()
                old_project.photo = request.FILES['project_photo-photo']
                old_project.save()

            if not old_project:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__PROJECT,
                    item_name=old_project.name
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__PROJECT,
                    item_name=old_project.name
                ))

        except models.Project.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_PROJECT_PHOTO: form_project_photo
    }

    return forms_handler


def modal_edit_permission_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_permission = None

    if element_index:

        try:
            old_permission = models.Permission.objects.get(pk=element_index)
        except models.Permission.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_permission = forms.ModelFormPermission(
            request.POST,
            prefix=globals.PREFIX__FORM_PERMISSION,
            instance=old_permission
        )

    else:
        # Get the form for new element
        form_permission = forms.ModelFormPermission(
            request.POST,
            prefix=globals.PREFIX__FORM_PERMISSION
        )

    if form_permission.is_valid():

        permission = form_permission.save(commit=False)

        try:

            # Save the new object or update it

            permission.project = models.Project.objects.get(pk=project_id)
            permission.full_clean()
            permission.save()

            if not old_permission:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__PERMISSION,
                    item_name=permission.title
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__PERMISSION,
                    item_name=permission.title
                ))

        except models.Permission.DoesNotExist as e:
            messages.error(request, e.messages)

        except models.Project.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_PERMISSION: form_permission
    }

    return forms_handler


def modal_edit_stage_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_stage = None

    if element_index:

        try:
            old_stage = models.Stage.objects.get(pk=element_index)
        except models.Stage.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_stage = forms.ModelFormStage(
            request.POST,
            prefix=globals.PREFIX__FORM_STAGE,
            instance=old_stage
        )

    else:
        # Get the form for new element
        form_stage = forms.ModelFormStage(
            request.POST,
            prefix=globals.PREFIX__FORM_STAGE
        )

    if form_stage.is_valid():

        stage = form_stage.save(commit=False)

        try:
            # Save the new object or update it
            # auto fill project.
            stage.project = models.Project.objects.get(pk=project_id)
            stage.full_clean()
            stage.save()

            if not old_stage:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_F.format(
                    model_name=globals.MODEL_NAME__STAGE,
                    item_name=stage.name
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_F.format(
                    model_name=globals.MODEL_NAME__STAGE,
                    item_name=stage.name
                ))

        except models.Stage.DoesNotExist as e:
            messages.error(request, e.messages)

        except models.Project.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_STAGE: form_stage
    }

    return forms_handler


def modal_edit_task_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_task = None

    if element_index:

        try:
            old_task = models.Task.objects.get(pk=element_index)
        except models.Task.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_task = forms.ModelFormTask(
            request.POST,
            prefix=globals.PREFIX__FORM_TASK,
            instance=old_task
        )

    else:
        # Get the form for new element
        form_task = forms.ModelFormTask(
            request.POST,
            prefix=globals.PREFIX__FORM_TASK
        )

    if form_task.is_valid():

        task = form_task.save(commit=False)

        try:
            # Save the new object or update it
            stage = models.Stage.objects.get(pk=stage_id)
            task.stage = stage
            task.finished_date = datetime.datetime.now()
            task.full_clean()
            task.save()

            if not old_task:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_F.format(
                    model_name=globals.MODEL_NAME__TASK,
                    item_name=task.title
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_F.format(
                    model_name=globals.MODEL_NAME__TASK,
                    item_name=task.title
                ))

        except models.Task.DoesNotExist as e:
            messages.error(request, e.messages)

        except models.Stage.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_TASK: form_task
    }

    return forms_handler


def modal_edit_comment_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_comment = None

    if element_index:

        try:
            old_comment = models.Comment.objects.get(pk=element_index)
        except models.Comment.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_comment = forms.ModelFormComment(
            request.POST,
            prefix=globals.PREFIX__FORM_COMMENT,
            instance=old_comment
        )

    else:
        # Get the form for new element
        form_comment = forms.ModelFormComment(
            request.POST,
            prefix=globals.PREFIX__FORM_COMMENT
        )

    if form_comment.is_valid():

        comment = form_comment.save(commit=False)

        try:
            # Save the new object or update it
            # auto fill stage and employee
            comment.stage = models.Stage.objects.get(pk=stage_id)
            user = request.user
            employee = models.Employee.objects.get(user=user)
            comment.employee = employee
            comment.date = datetime.datetime.now()
            comment.full_clean()
            comment.save()

            if not old_comment:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__COMMENT,
                    item_name=comment.title
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__COMMENT,
                    item_name=comment.title
                ))

        except models.Comment.DoesNotExist as e:
            messages.error(request, e.messages)

        except models.Stage.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_COMMENT: form_comment
    }

    return forms_handler


def modal_edit_employee_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_employee = None
    employee = None
    old_user = None
    form_password = None

    if element_index:

        try:
            old_employee = models.Employee.objects.get(pk=element_index)
            old_user = old_employee.user

        except models.Employee.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        except User.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_user = forms.ModelFormEditUser(
            request.POST,
            prefix=globals.PREFIX__FORM_USER,
            instance=old_user
        )

        form_password = forms.FormPasswordChange(
            request.POST,
            prefix=globals.PREFIX__FORM_PASSWORD_CHANGE
        )

    else:
        # Get the form for new element
        form_user = forms.ModelFormUser(
            request.POST,
            prefix=globals.PREFIX__FORM_USER
        )

    if form_user.is_valid():

        user = form_user.save(commit=False)

        try:
            # Save the new object or update it
            user.full_clean()

            if element_index:

                user.groups.clear()

                if form_password and form_password.is_valid():
                    password = form_password.cleaned_data['password']
                    confirm_password = form_password.cleaned_data['confirm_password']

                    if password != "" and confirm_password != "":

                        if password == confirm_password:
                            user.set_password(password)

                        else:
                            messages.error(request, globals.ERROR__PASSWORDS_DONT_MATCH)

            user.save()
            groups = request.POST.getlist('user-groups')

            for group in groups:
                group_id = int(group)
                user.groups.add(group_id)

            user.save()

            if old_employee:

                old_employee.user = user
                old_employee.save()

            else:
                employee = models.Employee.objects.get_or_create(user=user)[0]

            if not old_employee:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__EMPLOYEE,
                    item_name=employee.user.first_name
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__EMPLOYEE,
                    item_name=old_employee.user.first_name
                ))

        except models.Employee.DoesNotExist as e:
            messages.error(request, e.messages)

        except User.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_USER: form_user,
        globals.PREFIX__FORM_PASSWORD_CHANGE: form_password
    }

    return forms_handler


def modal_edit_employee_photo_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_employee = None

    if element_index:

        try:
            old_employee = models.Employee.objects.get(pk=element_index)
        except models.Employee.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_employee = forms.ModelFormEmployee(
            request.POST,
            request.FILES,
            prefix=globals.PREFIX__FORM_EMPLOYEE_PHOTO,
            instance=old_employee
        )

    else:
        # Get the form for new element
        form_employee = forms.ModelFormEmployee(
            request.POST,
            request.FILES,
            prefix=globals.PREFIX__FORM_EMPLOYEE_PHOTO
        )

    if form_employee.is_valid():

        employee_photo = form_employee.save(commit=False)

        try:
            # Save the new object or update it

            if 'employee_photo-photo' in request.FILES:
                employee_photo.full_clean()
                old_employee.photo = request.FILES['employee_photo-photo']
                old_employee.save()

            if not old_employee:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__EMPLOYEE,
                    item_name=old_employee.user.first_name
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__EMPLOYEE,
                    item_name=old_employee.user.first_name
                ))

        except models.Project.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_PROJECT_PHOTO: form_employee
    }

    return forms_handler


def modal_edit_institution_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_institution = None

    if element_index:

        try:
            old_institution = models.Institution.objects.get(pk=element_index)
        except models.Institution.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_institution = forms.ModelFormInstitution(
            request.POST,
            prefix=globals.PREFIX__FORM_INSTITUTION,
            instance=old_institution
        )

    else:
        # Get the form for new element
        form_institution = forms.ModelFormInstitution(
            request.POST,
            prefix=globals.PREFIX__FORM_INSTITUTION
        )

    if form_institution.is_valid():

        institution = form_institution.save(commit=False)

        try:
            # Save the new object or update it
            institution.full_clean()
            institution.save()

            if not old_institution:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_F.format(
                    model_name=globals.MODEL_NAME__INSTITUTION,
                    item_name=institution.name
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_F.format(
                    model_name=globals.MODEL_NAME__INSTITUTION,
                    item_name=institution.name
                ))

        except models.Institution.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_INSTITUTION: form_institution
    }

    return forms_handler


def modal_edit_project_type_handler(
        request,
        element_index=None,
        project_id=None,
        stage_id=None
):

    old_project_type = None

    if element_index:

        try:
            old_project_type = models.ProjectType.objects.get(pk=element_index)
        except models.ProjectType.DoesNotExist:
            messages.error(request, globals.ERROR__FORBIDDEN)
            return None

        # Get the form for instance element
        form_project_type = forms.ModelFormProjectType(
            request.POST,
            prefix=globals.PREFIX__FORM_PROJECT_TYPE,
            instance=old_project_type
        )

    else:
        # Get the form for new element
        form_project_type = forms.ModelFormProjectType(
            request.POST,
            prefix=globals.PREFIX__FORM_PROJECT_TYPE
        )

    if form_project_type.is_valid():

        project_type = form_project_type.save(commit=False)

        try:
            # Save the new object or update it
            project_type.full_clean()
            project_type.save()

            if not old_project_type:

                messages.success(request, globals.MESSAGE__CREATION_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__PROJECT_TYPE,
                    item_name=project_type.name
                ))

            else:

                messages.success(request, globals.MESSAGE__EDIT_SUCCESS_M.format(
                    model_name=globals.MODEL_NAME__PROJECT_TYPE,
                    item_name=project_type.name
                ))

        except models.ProjectType.DoesNotExist as e:
            messages.error(request, e.messages)

        except django.core.exceptions.ValidationError as e:
            messages.error(request, e.messages)

    forms_handler = {
        globals.PREFIX__FORM_PROJECT_TYPE: form_project_type
    }

    return forms_handler

################################################################################
#
# Functions and Handlers
#
################################################################################

MODAL__FUNCTIONS = {
    globals.MODAL_EDIT__INSTITUTION: modal_edit_institution,
    globals.MODAL_EDIT__PROJECT: modal_edit_project,
    globals.MODAL_EDIT__PROJECT_PHOTO: modal_edit_project_photo,
    globals.MODAL_EDIT__PROJECT_TYPE: modal_edit_project_type,
    globals.MODAL_EDIT__STAGE: modal_edit_stage,
    globals.MODAL_EDIT__COMMENT: modal_edit_comment,
    globals.MODAL_EDIT__TASK: modal_edit_task,
    globals.MODAL_EDIT__EMPLOYEE: modal_edit_employee,
    globals.MODAL_EDIT__EMPLOYEE_PHOTO: modal_edit_employee_photo,
    globals.MODAL_EDIT__PERMISSION: modal_edit_permission
}

MODAL__HANDLER_FUNCTIONS = {
    globals.MODAL_EDIT__INSTITUTION: modal_edit_institution_handler,
    globals.MODAL_EDIT__PROJECT: modal_edit_project_handler,
    globals.MODAL_EDIT__PROJECT_PHOTO: modal_edit_project_photo_handler,
    globals.MODAL_EDIT__PROJECT_TYPE: modal_edit_project_type_handler,
    globals.MODAL_EDIT__STAGE: modal_edit_stage_handler,
    globals.MODAL_EDIT__COMMENT: modal_edit_comment_handler,
    globals.MODAL_EDIT__TASK: modal_edit_task_handler,
    globals.MODAL_EDIT__EMPLOYEE: modal_edit_employee_handler,
    globals.MODAL_EDIT__EMPLOYEE_PHOTO: modal_edit_employee_photo_handler,
    globals.MODAL_EDIT__PERMISSION: modal_edit_permission_handler
}