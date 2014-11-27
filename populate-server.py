#coding:utf-8
#!/usr/bin/python

#Python imports

import os
import datetime

#Django imports

import django
from django.utils import timezone
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

#SAPU imports

from permissions import create_permissions
import sapu.models


def populate():

    ###############################################################################
    #
    #  States
    #
    ###############################################################################

    # delayed
    delayed = add_state(
        number=1,
        name=u"Retrasado",
        description=u"El elemento se encuentra desarrollandose pero está retrasado",
        color=u"#F3F163"
    )

    # on_time
    on_time = add_state(
        number=2,
        name=u"En tiempo",
        description=u"El elemento se encuentra desarrollandose y a tiempo con respecto la fecha de entrega.",
        color=u"#95C0FC"
    )

    # standby
    standby = add_state(
        number=3,
        name=u"Congelado",
        description=u"El elemento ha sido sido congelado",
        color=u"#FFFFFF"
    )

    # cancelled
    cancelled = add_state(
        number=4,
        name=u"Cancelado",
        description=u"El elemento no se terminó o ha sido pospuesto.",
        color=u"#E47F91"
    )

    # completed
    completed = add_state(
        number=5,
        name=u"Terminado",
        description=u"El elemento ha sido terminado",
        color=u"#6CE6A5"
    )

    ###############################################################################
    #
    #  Permission States
    #
    ###############################################################################

    # denied
    denied = add_permission_state(
        number=1,
        name=u"Negado",
        description=u"El permiso ha sido negado por la institución.",
        color=u"#D9534F"
    )

    # applied_for
    applied_for = add_permission_state(
        number=2,
        name=u"Solicitado",
        description=u"Se ha solicitado el permiso y se espera su autorización.",
        color=u"#F3F163"
    )

    # authorized
    authorized = add_permission_state(
        number=3,
        name=u"Autorizado",
        description=u"El permiso ha sido autorizado",
        color=u"#6CE6A5"
    )

    # no_competence
    no_competence = add_permission_state(
        number=4,
        name=u"No competencia",
        description=u"El permiso fue autorizado bajo una categoría de no competencia.",
        color=u"#6CE6A5"
    )

    ###############################################################################
    #
    #  Employees
    #
    ###############################################################################
    # 10 Registers
    photo_test = 'photos/users/default.png'

    #1
    employee1 = add_employee(
        user=User.objects.create_user('charles', 'charles@sapu.com', 'charles'),
        photo=photo_test
    )

    Group.objects.get(name='Administrador').user_set.add(employee1.user)
    employee1.user.first_name = 'Charles Maire'
    employee1.save()

    # Print out what we have added to the user.

    for state in State.objects.all():
        print "Inserted State - {0}".format(str(state))

    for permission_state in PermissionState.objects.all():
        print "Inserted Permission State - {0}".format(str(permission_state))

    for employee in Employee.objects.all():
        print "Inserted Employee - {0}".format(str(employee))


def add_project(
        project_id,
        deadline,
        creation_date,
        name,
        description,
        folio,
        project_type,
        institution,
        state
):
    p = Project.objects.get_or_create(project_id=project_id,
                                      deadline=deadline,
                                      creation_date=creation_date,
                                      name=name,
                                      description=description,
                                      folio=folio,
                                      project_type=project_type,
                                      institution=institution,
                                      state=state)[0]
    return p


def add_institution(
        name,
        phone,
        address,
        email,
        is_client,
        contact_point
):
    i = Institution.objects.get_or_create(name=name,
                                          phone=phone,
                                          address=address,
                                          email=email,
                                          is_client=is_client,
                                          contact_point=contact_point)[0]
    return i


def add_project_type(name, description):
    p = ProjectType.objects.get_or_create(name=name, description=description)[0]
    return p


def add_permission(title, description, folio, permission_state, institution, project):
    p = Permission.objects.get_or_create(title=title,
                                         description=description,
                                         folio=folio,
                                         permission_state=permission_state,
                                         institution=institution,
                                         project=project)[0]
    return p


def add_stage(
    name,
    description,
    number,
    creation_date,
    deadline,
    state,
    project
):
    s = Stage.objects.get_or_create(name=name,
                                    description=description,
                                    number=number,
                                    creation_date=creation_date,
                                    deadline=deadline,
                                    state=state,
                                    project=project)[0]
    return s


def add_assignment(
    stage,
    employee,
    completed=False
):
    a = Assignment.objects.get_or_create(stage=stage,
                                         employee=employee,
                                         completed=completed)[0]
    return a


def add_state(number, name, description, color):
    s = State.objects.get_or_create(number=number, name=name, description=description, color=color)[0]
    return s


def add_permission_state(number, name, description, color):
    s = PermissionState.objects.get_or_create(number=number, name=name, description=description, color=color)[0]
    return s


def add_employee(user, photo):
    e = Employee.objects.get_or_create(user=user, photo=photo)[0]
    return e


def add_comment(title, description, date, employee, stage):
    c = Comment.objects.get_or_create(title=title,
                                      description=description,
                                      date=date,
                                      employee=employee,
                                      stage=stage)[0]
    return c


def add_task(
    title,
    deadline,
    finished_date,
    is_complete,
    stage,
    employee
):
    t = Task.objects.get_or_create(title=title,
                                   deadline=deadline,
                                   finished_date=finished_date,
                                   is_complete=is_complete,
                                   stage=stage,
                                   employee=employee)[0]
    return t

# Start execution here!

django.setup()

if __name__ == '__main__':
    print "Starting SAPU population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sapu.settings")
    from sapu.models import Project, Institution, ProjectType, Permission, Stage, State, Employee, Comment, Task, PermissionState, Assignment
    create_permissions()
    populate()