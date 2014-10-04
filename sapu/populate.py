#Python imports

import os


def populate():

    #TODO Fill population script
    #TODO Investigate how to create datetime objects
    #TODO Investigate how to create image objects
    #TODO Investigate how to populate n to n relationship

    # Add Institutions


    # Add ProjectTypes


    # Add States
    # on_time
    # delayed
    # cancelled
    # completed


    # Add Employees


    # Add Projects
    # REQUIRES: Institution, ProjectType, State


    # Add Permissions
    # REQUIRES: Institution, Project


    # Add Stages
    # REQUIRES: State, Project, Employee


    # Add Comment
    # REQUIRES: Stage, Employee


    # Add Task
    # REQUIRES: Stage, Employee



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
