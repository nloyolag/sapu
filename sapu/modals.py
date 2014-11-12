#coding:utf-8

# Django imports
import django.core.exceptions
from django.contrib import messages

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
    if globals.PREFIX__FORM_EMPLOYEE in modal_forms:
        # Form was passed as a parameter
        employee_form = modal_forms[globals.PREFIX__FORM_EMPLOYEE]

    else:
        # Edit Employee
        if element_index is not None:

            try:
                employee =\
                    models.Employee.objects.get(pk=element_index)

            except models.Employee.DoesNotExist:
                return None

            employee_form = forms.ModelFormEmployee(
                prefix=globals.PREFIX__FORM_EMPLOYEE,
                instance=employee
            )

            action_text = globals.MODAL_ACTION__EDIT
            modal_action = globals.OPTION_NAME__MODAL_FORM_EDIT

        # Create employee
        else:
            employee_form = forms.ModelFormEmployee(prefix=globals.PREFIX__FORM_EMPLOYEE)

    employee_modal_form = globals.ModalForm(
        title=globals.FIELD__EMPLOYEE,
        form=employee_form
    )

    main_forms = [employee_modal_form]

    modal = globals.Modal(
        name=modal_name,
        action=modal_action,
        main_forms=main_forms,
        accept_button_text=action_text
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

def modal_edit_project_handler(request, element_index=None):
    pass


def modal_edit_permission_handler(request, element_index=None):
    pass


def modal_edit_stage_handler(request, element_index=None):
    pass


def modal_edit_task_handler(request, element_index=None):
    pass


def modal_edit_comment_handler(request, element_index=None):
    pass


def modal_edit_employee_handler(request, element_index=None):
    pass


def modal_edit_institution_handler(request, element_index=None):

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

    print "ANtes del valid"

    if form_institution.is_valid():

        print "Despues del valid"

        institution = form_institution.save(commit=False)

        try:
            # Save the new object or update it
            institution.full_clean()
            institution.save()

            print "Se guardo!"

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


def modal_edit_project_type_handler(request, element_index=None):
    pass

################################################################################
#
# Functions and Handlers
#
################################################################################

MODAL__FUNCTIONS = {
    globals.MODAL_EDIT__INSTITUTION: modal_edit_institution,
    globals.MODAL_EDIT__PROJECT: modal_edit_project,
    globals.MODAL_EDIT__PROJECT_TYPE: modal_edit_project_type,
    globals.MODAL_EDIT__STAGE: modal_edit_stage,
    globals.MODAL_EDIT__COMMENT: modal_edit_comment,
    globals.MODAL_EDIT__TASK: modal_edit_task,
    globals.MODAL_EDIT__EMPLOYEE: modal_edit_employee,
    globals.MODAL_EDIT__PERMISSION: modal_edit_permission
}

MODAL__HANDLER_FUNCTIONS = {
    globals.MODAL_EDIT__INSTITUTION: modal_edit_institution_handler,
    globals.MODAL_EDIT__PROJECT: modal_edit_project_handler,
    globals.MODAL_EDIT__PROJECT_TYPE: modal_edit_project_type_handler,
    globals.MODAL_EDIT__STAGE: modal_edit_stage_handler,
    globals.MODAL_EDIT__COMMENT: modal_edit_comment_handler,
    globals.MODAL_EDIT__TASK: modal_edit_task_handler,
    globals.MODAL_EDIT__EMPLOYEE: modal_edit_employee_handler,
    globals.MODAL_EDIT__PERMISSION: modal_edit_permission_handler
}