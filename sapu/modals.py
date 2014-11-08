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
    pass


def modal_edit_permission(
        modal_name,
        element_index=None,
        modal_forms=None
):
    pass


def modal_edit_stage(
        modal_name,
        element_index=None,
        modal_forms=None
):
    pass


def modal_edit_task(
        modal_name,
        element_index=None,
        modal_forms=None
):
    pass


def modal_edit_comment(
        modal_name,
        element_index=None,
        modal_forms=None
):
    pass


def modal_edit_employee(
        modal_name,
        element_index=None,
        modal_forms=None
):
    pass


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
        title=u"Institución",
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
    pass


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