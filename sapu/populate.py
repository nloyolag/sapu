#coding:utf-8

#Python imports

import os


def populate():

    #TODO Fill population script
    #TODO Investigate how to create datetime objects
    #TODO Investigate how to create image objects
    #TODO Investigate how to populate n to n relationship

    ###############################################################################
    #
    #  Institutions
    #
    ###############################################################################

    # 1
    add_institution(
        name=u"INAH",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 2
    add_institution(
        name=u"CEA",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 3
    add_institution(
        name=u"CFE",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 4
    add_institution(
        name=u"Gobierno Municipal",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 5
    add_institution(
        name=u"Gobierno Estatal del Estado de Querétaro el cual es un nombre muy largo a probar",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 6
    add_institution(
        name=u"Gobierno Federal",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 7
    add_institution(
        name=u"Qbit",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 8
    add_institution(
        name=u"Museo de la ciudad",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 9
    add_institution(
        name=u"Tec de Monterrey",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 10
    add_institution(
        name=u"ITAM",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 11
    add_institution(
        name=u"Delegación Centro Histórico",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 12
    add_institution(
        name=u"Six Flags",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 13
    add_institution(
        name=u"Nintendo",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 14
    add_institution(
        name=u"Sony",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 15
    add_institution(
        name=u"Mariachi Games",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 16
    add_institution(
        name=u"Rdio",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 17
    add_institution(
        name=u"Spotify",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 18
    add_institution(
        name=u"Microsoft",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 19
    add_institution(
        name=u"Apple",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 20
    add_institution(
        name=u"Asus",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=False,
        contact_point=u"Juan Gonzalo Perez"
    )

    ###############################################################################
    #
    #  Project Types
    #
    ###############################################################################
    # 10 Registers

    #1
    add_project_type(
        name=u"Banqueta",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #2
    add_project_type(
        name=u"Escultura",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #3
    add_project_type(
        name=u"Obra pública",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #4
    add_project_type(
        name=u"Restauración",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #5
    add_project_type(
        name=u"Edificio de gran formato",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #6
    add_project_type(
        name=u"Tipo de Proyecto Especial con Nombre Largo sin razón aparente",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #7
    add_project_type(
        name=u"Proyecto Especial",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #8
    add_project_type(
        name=u"Proyecto acuifero",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #9
    add_project_type(
        name=u"Proyecto de aeropuerto",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #10
    add_project_type(
        name=u"Maquetación básica",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    ###############################################################################
    #
    #  States
    #
    ###############################################################################

    # on_time
    add_state(
        name=u"En tiempo",
        description=u"El elemento se encuentra desarrollandose y a tiempo con respecto la fecha de entrega.",
        color=u"#95C0FC"
    )

    # delayed
    add_state(
        name=u"Retrasado",
        description=u"El elemento se encuentra desarrollandose pero está retradado.",
        color=u"#F3F163"
    )

    # cancelled
    add_state(
        name=u"Cancelado",
        description=u"El elemento no se terminó o ha sido pospuesto.",
        color=u"#E47F91"
    )

    # completed
    add_state(
        name=u"Terminado",
        description=u"El elemento ha sido terminado",
        color=u"#6CE6A5"
    )

    ###############################################################################
    #
    #  Employees
    #
    ###############################################################################
    # 10 Registers


    ###############################################################################
    #
    #  Projects
    #
    ###############################################################################
    # REQUIRES: Institution, ProjectType, State
    # 50 Registers


    ###############################################################################
    #
    #  Permissions
    #
    ###############################################################################
    # REQUIRES: Institution, Project
    # 50 Registers


    ###############################################################################
    #
    #  Stages
    #
    ###############################################################################
    # REQUIRES: State, Project, Employee
    # 50 Registers / 5 per project (Los que alcancen)


    ###############################################################################
    #
    #  Comments
    #
    ###############################################################################
    # REQUIRES: Stage, Employee
    # 50 Registers / 2 per stage (Los que alcancen)


    ###############################################################################
    #
    #  Tasks
    #
    ###############################################################################
    # REQUIRES: Stage, Employee
    # 50 Registers / 2 per stage (Los que alcancen)


    # Print out what we have added to the user.
    for institution in Institution.objects.all():
        print "Inserted Institution - {0}".format(str(institution))

    for project_type in ProjectType.objects.all():
        print "Inserted ProjectType - {0}".format(str(project_type))

    for state in State.objects.all():
        print "Inserted State - {0}".format(str(state))

    for employee in Employee.objects.all():
        print "Inserted Employee - {0}".format(str(employee))

    for project in Institution.objects.all():
        print "Inserted Project - {0}".format(str(project))

        for permission in Permission.objects.filter(project=project):
            print "    Inserted Permission - {0}".format(str(permission))

        for stage in Stage.objects.filter(project=project):
            print "    Inserted Stage - {0}".format(str(stage))

            for comment in Comment.objects.filter(stage=stage):
                print "        Comment - {0}".format(str(comment))

            for task in Task.objects.filter(stage=stage):
                print "        Task - {0}".format(str(task))


def add_project(
        project_id,
        deadline,
        name,
        photo,
        description,
        folio,
        project_type,
        institution,
        state
):
    p = Project.objects.get_or_create(project_id=project_id,
                                      deadline=deadline,
                                      name=name,
                                      photo=photo,
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


def add_permission(title, description, folio, institution, project):
    p = Permission.objects.get_or_create(title=title,
                                         description=description,
                                         folio=folio,
                                         institution=institution,
                                         project=project)[0]
    return p


def add_stage(name,
              description,
              number,
              deadline,
              state,
              project,
              employee
):
    s = Stage.objects.get_or_create(name=name,
                                    description=description,
                                    number=number,
                                    deadline=deadline,
                                    state=state,
                                    project=project,
                                    employee=employee)[0]
    return s


def add_state(name, description, color):
    s = State.objects.get_or_create(name=name, description=description, color=color)[0]
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


def add_task(title,
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
if __name__ == '__main__':
    print "Starting SAPU population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sapu.settings')
    from sapu.models import Project, Institution, ProjectType, Permission, Stage, State, Employee, Comment, Task
    populate()
