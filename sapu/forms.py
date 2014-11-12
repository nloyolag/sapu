#coding:utf-8


# Django imports
import django.forms
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


class ModelFormProject(django.forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelFormProject, self).__init__(*args, **kwargs)
        self.fields['institution'].queryset = models.Institution.objects.filter(is_client=True)

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
            'project_type'
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
            }
        }


class ModelFormPermission(django.forms.ModelForm):

    class Meta:
        model = models.Permission
        fields = [
            'title',
            'description',
            'folio',
            'institution'
        ]

        error_messages = {
            'title': {
                'required': u"Necesitas asignarle un título al permiso"
            }
        }


class ModelFormStage(django.forms.ModelForm):

    class Meta:
        model = models.Stage
        fields = [
            'name',
            'description',
            'number',
            'deadline',
            'employee'
        ]

        error_messages = {
            'title': {
                'required': u"Necesitas asignarle un título a la etapa"
            },
            'deadline': {
                'required': u"Necesitas asignarle una fecha límite a la etapa"
            },
            'number': {
                'required': u"Necesitas asignarle un número a la etapa"
            }
        }


class ModelFormTask(django.forms.ModelForm):

    class Meta:
        model = models.Task
        fields = [
            'title',
            'employee',
            'deadline',
            'employee'
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


class ModelFormEmployee(django.forms.ModelForm):

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass


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