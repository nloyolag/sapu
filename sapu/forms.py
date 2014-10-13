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

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass


class ModelFormPermission(django.forms.ModelForm):

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass


class ModelFormStage(django.forms.ModelForm):

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass


class ModelFormTask(django.forms.ModelForm):

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass


class ModelFormComment(django.forms.ModelForm):

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass


class ModelFormUser(django.forms.ModelForm):

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass


class ModelFormInstitution(django.forms.ModelForm):

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass


class ModelFormProjectType(django.forms.ModelForm):

    #def __init__(self, *args, **kwargs):

    #class Meta:
    pass