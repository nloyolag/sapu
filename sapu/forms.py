#coding:utf-8


# Django imports
import django.forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

# SAPU imports
import models
import globals


class FormRedirect(django.forms.Form):
    redirect_url = django.forms.CharField(widget=django.forms.HiddenInput)


class FormSearchProject(django.forms.Form):
    name = django.forms.CharField(
        required=False,
        widget=django.forms.TextInput(
            attrs={
                'placeholder': u"Buscar " + globals.FIELD__PROJECT}
        )
    )


class FormPasswordChange(django.forms.Form):
    password = django.forms.CharField(
        required=False,
        label=globals.FIELD__NEW_PASSWORD,
        widget=django.forms.PasswordInput()
    )

    confirm_password = django.forms.CharField(
        required=False,
        label=globals.FIELD__CONFIRM_PASSWORD,
        widget=django.forms.PasswordInput()
    )


class ModelFormProject(django.forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelFormProject, self).__init__(*args, **kwargs)
        self.fields['institution'].queryset = models.Institution.objects.filter(is_client=True)
        self.fields['deadline'].widget = django.forms.TextInput(attrs={
            'class': 'datetime-field'})

    class Meta:
        model = models.Project
        fields = [
            'name',
            'description',
            'project_id',
            'deadline',
            'folio',
            'photo',
            'institution',
            'project_type',
            'state'
        ]

        error_messages = {
            'name': {
                'required': u"Necesitas asignarle un nombre al proyecto"
            },
            'project_id': {
                'required': u"Necesitas asignarle un identificador al proyecto"
            },
            'deadline': {
                'required': u"Necesitas asignarle una fecha límite al proyecto"
            },
            'state': {
                'required': u"Necesitas asignarle un estado al proyecto"
            }
        }


class ModelFormPermission(django.forms.ModelForm):

    class Meta:
        model = models.Permission
        fields = [
            'title',
            'description',
            'folio',
            'institution',
            'permission_state'
        ]

        error_messages = {
            'title': {
                'required': u"Necesitas asignarle un título al permiso"
            },
            'state': {
                'required': u"Necesitas asignarle un estado al permiso"
            }
        }


class ModelFormStage(django.forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelFormStage, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget = django.forms.TextInput(attrs={
            'class': 'datetime-field'})

    class Meta:
        model = models.Stage
        fields = [
            'name',
            'description',
            'number',
            'deadline',
            'employee',
            'state'
        ]

        error_messages = {
            'name': {
                'required': u"Necesitas asignarle un nombre a la etapa"
            },
            'deadline': {
                'required': u"Necesitas asignarle una fecha límite a la etapa"
            },
            'number': {
                'required': u"Necesitas asignarle un número a la etapa"
            },
            'employee': {
                'required': u"Necesitas asignarle un empleado a la etapa"
            },
            'state': {
                'required': u"Necesitas asignarle un estado a la etapa"
            }
        }


class ModelFormTask(django.forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelFormTask, self).__init__(*args, **kwargs)
        self.fields['deadline'].widget = django.forms.TextInput(attrs={
            'class': 'datetime-field'})

    class Meta:
        model = models.Task
        fields = [
            'title',
            'employee',
            'deadline'
        ]

        error_messages = {
            'title': {
                'required': u"Necesitas asignarle un título a la tarea"
            },
            'deadline': {
                'required': u"Necesitas asignarle una fecha límite a la tarea"
            },
            'employee': {
                'required': u"Necesitas asignarle un encargado a la tarea"
            }
        }


class ModelFormComment(django.forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = [
            'title',
            'description'
        ]

        error_messages = {
            'title': {
                'required': u"Necesitas asignarle un nombre al comentario"
            }
        }


class ModelFormUser(django.forms.ModelForm):

    class Meta:
        model = django.contrib.auth.models.User

        fields = [
            'username',
            'email',
            'first_name',
            'password',
            'groups'
        ]

        labels = {
            'username': globals.FIELD__USERNAME,
            'email': globals.FIELD__EMAIL,
            'first_name': globals.FIELD__NAME,
            'password': globals.FIELD__PASSWORD,
            'groups': globals.FIELD__GROUPS
        }

        error_messages = {
            'username': {
                'required': u"Necesitas escribir un nombre de usuario"
            },
            'first_name': {
                'required': u"Necesitas escribir un nombre(s)"
            },
            'last_name': {
                'required': u"Necesitas escribir un apellido(s)"
            },
            'password': {
                'required': u"Necesitas escribir una contraseña"
            },
            'groups': {
                'required': u"Necesitas seleccionar un puesto"
            }
        }


class ModelFormEditUser(django.forms.ModelForm):

    class Meta:
        model = django.contrib.auth.models.User

        fields = [
            'username',
            'email',
            'first_name',
            'groups'
        ]

        labels = {
            'username': globals.FIELD__USERNAME,
            'email': globals.FIELD__EMAIL,
            'first_name': globals.FIELD__NAME,
            'groups': globals.FIELD__GROUPS
        }

        error_messages = {
            'username': {
                'required': u"Necesitas escribir un nombre de usuario"
            },
            'first_name': {
                'required': u"Necesitas escribir un nombre(s)"
            },
            'last_name': {
                'required': u"Necesitas escribir un apellido(s)"
            },
            'groups': {
                'required': u"Necesitas seleccionar un puesto"
            }
        }


class ModelFormEmployee(django.forms.ModelForm):

    class Meta:
        model = models.Employee
        fields = [
            'photo'
        ]


class ModelFormInstitution(django.forms.ModelForm):

    class Meta:
        model = models.Institution
        fields = [
            'name',
            'phone',
            'address',
            'email',
            'is_client',
            'contact_point'
        ]

        error_messages = {
            'name': {
                'required': u"Necesitas asignarle un nombre a la institución"
            }
        }


class ModelFormProjectType(django.forms.ModelForm):

    class Meta:
        model = models.ProjectType
        fields = [
            'name',
            'description'
        ]

        error_messages = {
            'name': {
                'required': u"Necesitas asignarle un nombre al tipo de proyecto"
            }
        }