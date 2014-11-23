# Python imports
import os

# Django imports

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# SAPU imports

import sapu.models


def create_permissions():

    # Institutions

    permission_add_inst = Permission.objects.get(codename='add_institution')
    permission_change_inst = Permission.objects.get(codename='change_institution')
    permission_delete_inst = Permission.objects.get(codename='delete_institution')

    # Project Types

    permission_add_ptype = Permission.objects.get(codename='add_projecttype')
    permission_change_ptype = Permission.objects.get(codename='change_projecttype')
    permission_delete_ptype = Permission.objects.get(codename='delete_projecttype')

    # Project

    permission_add_project = Permission.objects.get(codename='add_project')
    permission_change_project = Permission.objects.get(codename='change_project')
    permission_delete_project = Permission.objects.get(codename='delete_project')

    # Permission

    content_type = ContentType.objects.get_for_model(Permission)
    permission_add_permission = Permission.objects.get(codename='add_permission', content_type=content_type)
    permission_change_permission = Permission.objects.get(codename='change_permission', content_type=content_type)
    permission_delete_permission = Permission.objects.get(codename='delete_permission', content_type=content_type)

    # Employee

    permission_add_employee = Permission.objects.get(codename='add_employee')
    permission_change_employee = Permission.objects.get(codename='change_employee')
    permission_delete_employee = Permission.objects.get(codename='delete_employee')

    # Stage

    permission_add_stage = Permission.objects.get(codename='add_stage')
    permission_change_stage = Permission.objects.get(codename='change_stage')
    permission_delete_stage = Permission.objects.get(codename='delete_stage')

    # Comment

    permission_add_comment = Permission.objects.get(codename='add_comment')
    permission_change_comment = Permission.objects.get(codename='change_comment')
    permission_delete_comment = Permission.objects.get(codename='delete_comment')

    # Task

    permission_add_task = Permission.objects.get(codename='add_task')
    permission_change_task = Permission.objects.get(codename='change_task')
    permission_delete_task = Permission.objects.get(codename='delete_task')

    employee = Group(name='Empleado')
    employee.save()

    supervisor = Group(name='Supervisor')
    supervisor.save()

    project_manager = Group(name='Jefe de proyectos')
    project_manager.save()

    administrator = Group(name='Administrador')
    administrator.save()

    employee_permissions = [permission_add_comment,
                            permission_change_comment,
                            permission_delete_comment]

    supervisor_permissions = [permission_add_task,
                              permission_change_task,
                              permission_delete_task]

    supervisor_permissions.extend(employee_permissions)

    project_manager_permissions = [permission_add_ptype,
                                   permission_change_ptype,
                                   permission_delete_ptype,
                                   permission_add_inst,
                                   permission_change_inst,
                                   permission_delete_inst,
                                   permission_add_permission,
                                   permission_change_permission,
                                   permission_delete_permission,
                                   permission_add_stage,
                                   permission_change_stage,
                                   permission_delete_stage,
                                   permission_add_project,
                                   permission_change_project]

    project_manager_permissions.extend(supervisor_permissions)

    administrator_permissions = [permission_delete_project,
                                 permission_add_employee,
                                 permission_change_employee,
                                 permission_delete_employee]

    administrator_permissions.extend(project_manager_permissions)

    employee.permissions = employee_permissions
    supervisor.permissions = supervisor_permissions
    project_manager.permissions = project_manager_permissions
    administrator.permissions = administrator_permissions