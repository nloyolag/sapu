#coding:utf-8
#!/usr/bin/python

#Python imports

import os
import datetime

#Django imports

import django
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

#SAPU imports

from permissions import create_permissions
import sapu.models

def populate():

    ###############################################################################
    #
    #  Institutions
    #
    ###############################################################################

    # 1
    institution1 = add_institution(
        name=u"INAH",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 2
    institution2 = add_institution(
        name=u"CEA",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 3
    institution3 = add_institution(
        name=u"CFE",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 4
    institution4 = add_institution(
        name=u"Gobierno Municipal",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 5
    institution5 = add_institution(
        name=u"Gobierno Estatal del Estado de Querétaro el cual es un nombre muy largo a probar",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 6
    institution6 = add_institution(
        name=u"Gobierno Federal",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 7
    institution7 = add_institution(
        name=u"Qbit",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 8
    institution8 = add_institution(
        name=u"Museo de la ciudad",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 9
    institution9 = add_institution(
        name=u"Tec de Monterrey",
        phone=u"4423302576",
        address=u"Vicente Guerrero Norte no. 20",
        email=u"inah@inah.com",
        is_client=True,
        contact_point=u"Juan Gonzalo Perez"
    )

    # 10
    institution10 = add_institution(
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

    #1
    project_type1 = add_project_type(
        name=u"Banqueta",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #2
    project_type2 = add_project_type(
        name=u"Escultura",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #3
    project_type3 = add_project_type(
        name=u"Obra pública",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #4
    project_type4 = add_project_type(
        name=u"Restauración",
        description=u"Obra especificada para creación de nuevas banquetas"
    )

    #5
    project_type5 = add_project_type(
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
    on_time = add_state(
	number= 2,
        name=u"En tiempo",
        description=u"El elemento se encuentra desarrollandose y a tiempo con respecto la fecha de entrega.",
        color=u"#95C0FC"
    )

    # delayed
    delayed = add_state(
	number=1,
        name=u"Retrasado",
        description=u"El elemento se encuentra desarrollandose pero está retrasado",
        color=u"#F3F163"
    )

    # cancelled
    cancelled = add_state(
	number=3,
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
    #TODO change color for standby state
    # standby
    standby = add_state(
	number=4,
        name=u"Terminado",
        description=u"El elemento ha sido terminado",
        color=u"#FFFFFF"
    )

    ###############################################################################
    #
    #  Employees
    #
    ###############################################################################
    # 10 Registers
    photo_test = 'photos/users/test.jpg'

    #1
    employee1 = add_employee(
        user=User.objects.create_user('Armando', 'armando@sapu.com', 'armando'),
        photo=photo_test
    )

    Group.objects.get(name='Administrator').user_set.add(employee1.user)
    employee1.user.first_name = 'Armando Arias'
    employee1.save()

    #2
    employee2 = add_employee(
        user=User.objects.create_user('Baltasar','baltasar@sapu.com', 'baltasar'),
        photo=photo_test
    )

    Group.objects.get(name='Administrator').user_set.add(employee2.user)
    employee1.user.first_name = 'Baltasar Mendez'
    employee2.save()

    #3
    employee3 = add_employee(
        user=User.objects.create_user('Carlos','carlos@sapu.com', 'carlos'),
        photo=photo_test
    )

    Group.objects.get(name='Administrator').user_set.add(employee3.user)
    employee3.save()

    #4
    employee4 = add_employee(
        user=User.objects.create_user('Daniel', 'daniel@sapu.com', 'daniel'),
        photo=photo_test
    )

    Group.objects.get(name='ProjectManager').user_set.add(employee4.user)
    employee4.save()

    #5
    employee5 = add_employee(
        user=User.objects.create_user('Eleazar', 'eleazar@sapu.com', 'eleazar'),
        photo=photo_test
    )

    Group.objects.get(name='ProjectManager').user_set.add(employee5.user)
    employee5.save()

    #6
    employee6 = add_employee(
        user=User.objects.create_user('Felipe', 'felipe@sapu.com', 'felipe'),
        photo=photo_test
    )

    Group.objects.get(name='ProjectManager').user_set.add(employee6.user)
    employee6.save()

    #7
    employee7 = add_employee(
        user=User.objects.create_user('Guillermo', 'guillermo@sapu.com', 'guillermo'),
        photo=photo_test
    )

    Group.objects.get(name='Supervisor').user_set.add(employee7.user)
    employee7.save()

    #8
    employee8 = add_employee(
        user=User.objects.create_user('Hermenegildo', 'hermenegildo@sapu.com', 'hermenegildo'),
        photo=photo_test
    )

    Group.objects.get(name='Supervisor').user_set.add(employee8.user)
    employee8.save()

    #9
    employee9 = add_employee(
        user=User.objects.create_user(u'Ileana', 'ileana@sapu.com', 'ileana'),
        photo=photo_test
    )

    Group.objects.get(name='Supervisor').user_set.add(employee9.user)
    employee9.save()

    #10
    employee10 = add_employee(
        user=User.objects.create_user(u'Jonathan', 'jonathan@sapu.com','jonathan'),
        photo=photo_test
    )

    #11
    employee11 = add_employee(
        user=User.objects.create_user(u'Katia', 'katia@sapu.com','katia'),
        photo=photo_test
    )

    #12
    employee12 = add_employee(
        user=User.objects.create_user(u'Laura', 'laura@sapu.com','laura'),
        photo=photo_test
    )

    #13
    employee13 = add_employee(
        user=User.objects.create_user(u'Mauro', 'mauro@sapu.com','mauro'),
        photo=photo_test
    )

    #14
    add_employee(
        user=User.objects.create_user(u'Nazarín', 'nazarin@sapu.com','nazarin'),
        photo=photo_test
    )

    #15
    add_employee(
        user=User.objects.create_user('Olaf', 'olaf@sapu.com','olaf'),
        photo=photo_test
    )

    ###############################################################################
    #
    #  Projects
    #
    ########################################### ####################################
    # REQUIRES: Institution, ProjectType, State
    # 50 Registers

    datetime1 = datetime.datetime.now()

    # 1
    project1 = add_project(
        project_id=u"A1",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Lienzo Charro",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project1.photo = 'photos/projects/test.jpg'
    project1.save()

    # 2
    project2 = add_project(
        project_id=u"A2",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Bandodromo",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project2.photo = 'photos/projects/test.jpg'
    project2.save()

    # 3
    project3 = add_project(
        project_id=u"A3",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura del gobernador del estado de 1956",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project3.photo = 'photos/projects/test.jpg'
    project3.save()

    # 4
    project4 = add_project(
        project_id=u"A4",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banquetas de avenida universidad",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project4.photo = 'photos/projects/test.jpg'
    project4.save()

    # 5
    project5 = add_project(
        project_id=u"A5",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Alameda",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project5.photo = 'photos/projects/test.jpg'
    project5.save()

    # 6
    project6 = add_project(
        project_id=u"A6",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Carretera a Tlalpan",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project6.photo = 'photos/projects/test.jpg'
    project6.save()

    # 7
    project7 = add_project(
        project_id=u"A7",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Fachada de convento de San Antonio",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project7.photo = 'photos/projects/test.jpg'
    project7.save()

    # 8
    project8 = add_project(
        project_id=u"A8",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banqueta de calle vicente guerrero",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project8.photo = 'photos/projects/test.jpg'
    project8.save()

    # 9
    project9 = add_project(
        project_id=u"A9",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de Francisco Cervantes",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project9.photo = 'photos/projects/test.jpg'
    project9.save()

    # 10
    project10 = add_project(
        project_id=u"A10",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de gato",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type1,
        institution=institution1,
        state=on_time
    )

    project10.photo = 'photos/projects/test.jpg'
    project10.save()

    # 11
    project11 = add_project(
        project_id=u"A11",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Lienzo Charro",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project11.photo = 'photos/projects/test.jpg'
    project11.save()

    # 12
    project12 = add_project(
        project_id=u"A12",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Bandodromo",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project12.photo = 'photos/projects/test.jpg'
    project12.save()

    # 13
    project13 = add_project(
        project_id=u"A13",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura del gobernador del estado de 1956",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project13.photo = 'photos/projects/test.jpg'
    project13.save()

    # 14
    project14 = add_project(
        project_id=u"A14",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banquetas de avenida universidad",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project14.photo = 'photos/projects/test.jpg'
    project14.save()

    # 15
    project15 = add_project(
        project_id=u"A15",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Alameda",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project15.photo = 'photos/projects/test.jpg'
    project15.save()

    # 16
    project16 = add_project(
        project_id=u"A16",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Carretera a Tlalpan",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project16.photo = 'photos/projects/test.jpg'
    project16.save()

    # 17
    project17 = add_project(
        project_id=u"A17",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Fachada de convento de San Antonio",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project17.photo = 'photos/projects/test.jpg'
    project17.save()

    # 18
    project18 = add_project(
        project_id=u"A18",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banqueta de calle vicente guerrero",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project18.photo = 'photos/projects/test.jpg'
    project18.save()

    # 19
    project19 = add_project(
        project_id=u"A19",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de Francisco Cervantes",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project19.photo = 'photos/projects/test.jpg'
    project19.save()

    # 20
    project20 = add_project(
        project_id=u"A20",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de gato",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type2,
        institution=institution2,
        state=on_time
    )

    project20.photo = 'photos/projects/test.jpg'
    project20.save()

    # 21
    project21 = add_project(
        project_id=u"A21",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Lienzo Charro",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project21.photo = 'photos/projects/test.jpg'
    project21.save()

    # 22
    project22 = add_project(
        project_id=u"A22",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Bandodromo",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project22.photo = 'photos/projects/test.jpg'
    project22.save()

    # 23
    project23 = add_project(
        project_id=u"A23",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura del gobernador del estado de 1956",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project23.photo = 'photos/projects/test.jpg'
    project23.save()

    # 24
    project24 = add_project(
        project_id=u"A24",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banquetas de avenida universidad",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project24.photo = 'photos/projects/test.jpg'
    project24.save()

    # 25
    project25 = add_project(
        project_id=u"A25",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Alameda",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project25.photo = 'photos/projects/test.jpg'
    project25.save()

    # 26
    project26 = add_project(
        project_id=u"A26",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Carretera a Tlalpan",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project26.photo = 'photos/projects/test.jpg'
    project26.save()

    # 27
    project27 = add_project(
        project_id=u"A27",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Fachada de convento de San Antonio",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project27.photo = 'photos/projects/test.jpg'
    project27.save()

    # 28
    project28 = add_project(
        project_id=u"A28",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banqueta de calle vicente guerrero",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project28.photo = 'photos/projects/test.jpg'
    project28.save()

    # 29
    project29 = add_project(
        project_id=u"A29",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de Francisco Cervantes",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project29.photo = 'photos/projects/test.jpg'
    project29.save()

    # 30
    project30 = add_project(
        project_id=u"A30",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de gato",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type3,
        institution=institution3,
        state=on_time
    )

    project30.photo = 'photos/projects/test.jpg'
    project30.save()

    # 31
    project31 = add_project(
        project_id=u"A31",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Lienzo Charro",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project31.photo = 'photos/projects/test.jpg'
    project31.save()

    # 32
    project32 = add_project(
        project_id=u"A32",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Bandodromo",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project32.photo = 'photos/projects/test.jpg'
    project32.save()

    # 33
    project33 = add_project(
        project_id=u"A33",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura del gobernador del estado de 1956",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project33.photo = 'photos/projects/test.jpg'
    project33.save()

    # 34
    project34 = add_project(
        project_id=u"A34",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banquetas de avenida universidad",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project34.photo = 'photos/projects/test.jpg'
    project34.save()

    # 35
    project35 = add_project(
        project_id=u"A35",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Alameda",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project35.photo = 'photos/projects/test.jpg'
    project35.save()

    # 36
    project36 = add_project(
        project_id=u"A36",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Carretera a Tlalpan",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project36.photo = 'photos/projects/test.jpg'
    project36.save()

    # 37
    project37 = add_project(
        project_id=u"A37",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Fachada de convento de San Antonio",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project37.photo = 'photos/projects/test.jpg'
    project37.save()

    # 38
    project38 = add_project(
        project_id=u"A38",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banqueta de calle vicente guerrero",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project38.photo = 'photos/projects/test.jpg'
    project38.save()

    # 39
    project39 = add_project(
        project_id=u"A39",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de Francisco Cervantes",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project39.photo = 'photos/projects/test.jpg'
    project39.save()

    # 40
    project40 = add_project(
        project_id=u"A40",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de gato",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type4,
        institution=institution4,
        state=on_time
    )

    project40.photo = 'photos/projects/test.jpg'
    project40.save()

    # 41
    project41 = add_project(
        project_id=u"A41",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Lienzo Charro",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project41.photo = 'photos/projects/test.jpg'
    project41.save()

    # 42
    project42 = add_project(
        project_id=u"A42",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Bandodromo",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project42.photo = 'photos/projects/test.jpg'
    project42.save()

    # 43
    project43 = add_project(
        project_id=u"A43",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura del gobernador del estado de 1956",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project43.photo = 'photos/projects/test.jpg'
    project43.save()

    # 44
    project44 = add_project(
        project_id=u"A44",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banquetas de avenida universidad",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project44.photo = 'photos/projects/test.jpg'
    project44.save()

    # 45
    project45 = add_project(
        project_id=u"A45",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Alameda",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project45.photo = 'photos/projects/test.jpg'
    project45.save()

    # 46
    project46 = add_project(
        project_id=u"A46",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Carretera a Tlalpan",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project46.photo = 'photos/projects/test.jpg'
    project46.save()

    # 47
    project47 = add_project(
        project_id=u"A47",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Fachada de convento de San Antonio",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project47.photo = 'photos/projects/test.jpg'
    project47.save()

    # 48
    project48 = add_project(
        project_id=u"A48",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Banqueta de calle vicente guerrero",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project48.photo = 'photos/projects/test.jpg'
    project48.save()

    # 49
    project49 = add_project(
        project_id=u"A49",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de Francisco Cervantes",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project49.photo = 'photos/projects/test.jpg'
    project49.save()

    # 50
    project50 = add_project(
        project_id=u"A50",
        deadline=datetime1,
        creation_date=datetime1,
        name=u"Escultura de gato",
        description=u"Enorme proyecto municipal de gran interes publico",
        folio=u"A739232",
        project_type=project_type5,
        institution=institution5,
        state=on_time
    )

    project50.photo = 'photos/projects/test.jpg'
    project50.save()

    ###############################################################################
    #
    #  Permissions
    #
    ###############################################################################
    # REQUIRES: Institution, Project
    # 50 Registers

    #1
    add_permission(
        title=u"Permiso INAH",
        description=u"Permiso emitido por el INAH",
        folio="0001",
        institution=institution1,
        project=project1
    )

    #2
    add_permission(
        title=u"Permiso CEA",
        description=u"Permiso emitido por el CEA",
        folio="0002",
        institution=institution2,
        project=project1
    )

    #3
    add_permission(
        title=u"Permiso CFE",
        description=u"Permiso emitido por el CFE",
        folio="0003",
        institution=institution3,
        project=project1
    )

    #4
    add_permission(
        title=u"Permiso Municipio",
        description=u"Permiso emitido por el municipio",
        folio="0004",
        institution=institution4,
        project=project1
    )

    #5
    add_permission(
        title=u"Permiso Estado",
        description=u"Permiso emitido por el estado",
        folio="0005",
        institution=institution5,
        project=project1
    )

    #6
    add_permission(
        title=u"Permiso Federal",
        description=u"Permiso emitido por la Federación",
        folio="0006",
        institution=institution6,
        project=project1
    )

    #7
    add_permission(
        title=u"Permiso Qbit",
        description=u"Permiso emitido por el Qbit",
        folio="0007",
        institution=institution7,
        project=project1
    )

    #8
    add_permission(
        title=u"Permiso Museo de la Ciudad",
        description=u"Permiso emitido por el Museo de la Ciudad",
        folio="0008",
        institution=institution8,
        project=project1
    )

    #9
    add_permission(
        title=u"Permiso ITESM",
        description=u"Permiso emitido por el ITESM",
        folio="0009",
        institution=institution9,
        project=project1
    )

    #10
    add_permission(
        title=u"Permiso ITAM",
        description=u"Permiso emitido por el ITAM",
        folio="0010",
        institution=institution10,
        project=project1
    )

    #11
    add_permission(
        title=u"Permiso INAH",
        description=u"Permiso emitido por el INAH",
        folio="0011",
        institution=institution1,
        project=project2
    )

    #12
    add_permission(
        title=u"Permiso CEA",
        description=u"Permiso emitido por el CEA",
        folio="0012",
        institution=institution2,
        project=project2
    )

    #13
    add_permission(
        title=u"Permiso CFE",
        description=u"Permiso emitido por el CFE",
        folio="0013",
        institution=institution3,
        project=project2
    )

    #14
    add_permission(
        title=u"Permiso Municipio",
        description=u"Permiso emitido por el municipio",
        folio="0014",
        institution=institution4,
        project=project2
    )

    #15
    add_permission(
        title=u"Permiso Estado",
        description=u"Permiso emitido por el estado",
        folio="0015",
        institution=institution5,
        project=project2
    )

    #16
    add_permission(
        title=u"Permiso Federal",
        description=u"Permiso emitido por la Federación",
        folio="0016",
        institution=institution6,
        project=project2
    )

    #17
    add_permission(
        title=u"Permiso Qbit",
        description=u"Permiso emitido por el Qbit",
        folio="0017",
        institution=institution7,
        project=project2
    )

    #18
    add_permission(
        title=u"Permiso Museo de la Ciudad",
        description=u"Permiso emitido por el Museo de la Ciudad",
        folio="0018",
        institution=institution8,
        project=project2
    )

    #19
    add_permission(
        title=u"Permiso ITESM",
        description=u"Permiso emitido por el ITESM",
        folio="0019",
        institution=institution9,
        project=project2
    )

    #20
    add_permission(
        title=u"Permiso ITAM",
        description=u"Permiso emitido por el ITAM",
        folio="0020",
        institution=institution10,
        project=project2
    )

    #21
    add_permission(
        title=u"Permiso INAH",
        description=u"Permiso emitido por el INAH",
        folio="0021",
        institution=institution1,
        project=project3
    )

    #22
    add_permission(
        title=u"Permiso CEA",
        description=u"Permiso emitido por el CEA",
        folio="0022",
        institution=institution2,
        project=project3
    )

    #23
    add_permission(
        title=u"Permiso CFE",
        description=u"Permiso emitido por el CFE",
        folio="0023",
        institution=institution3,
        project=project3
    )

    #24
    add_permission(
        title=u"Permiso Municipio",
        description=u"Permiso emitido por el municipio",
        folio="0024",
        institution=institution4,
        project=project3
    )

    #25
    add_permission(
        title=u"Permiso Estado",
        description=u"Permiso emitido por el estado",
        folio="0025",
        institution=institution5,
        project=project3
    )

    #26
    add_permission(
        title=u"Permiso Federal",
        description=u"Permiso emitido por la Federación",
        folio="0026",
        institution=institution6,
        project=project3
    )

    #27
    add_permission(
        title=u"Permiso Qbit",
        description=u"Permiso emitido por el Qbit",
        folio="0027",
        institution=institution7,
        project=project3
    )

    #28
    add_permission(
        title=u"Permiso Museo de la Ciudad",
        description=u"Permiso emitido por el Museo de la Ciudad",
        folio="0028",
        institution=institution8,
        project=project3
    )

    #29
    add_permission(
        title=u"Permiso ITESM",
        description=u"Permiso emitido por el ITESM",
        folio="0029",
        institution=institution9,
        project=project3
    )

    #30
    add_permission(
        title=u"Permiso ITAM",
        description=u"Permiso emitido por el ITAM",
        folio="0030",
        institution=institution10,
        project=project3
    )

    #31
    add_permission(
        title=u"Permiso INAH",
        description=u"Permiso emitido por el INAH",
        folio="0031",
        institution=institution1,
        project=project4
    )

    #32
    add_permission(
        title=u"Permiso CEA",
        description=u"Permiso emitido por el CEA",
        folio="0032",
        institution=institution2,
        project=project4
    )

    #33
    add_permission(
        title=u"Permiso CFE",
        description=u"Permiso emitido por el CFE",
        folio="0033",
        institution=institution3,
        project=project4
    )

    #34
    add_permission(
        title=u"Permiso Municipio",
        description=u"Permiso emitido por el municipio",
        folio="0034",
        institution=institution4,
        project=project4
    )

    #35
    add_permission(
        title=u"Permiso Estado",
        description=u"Permiso emitido por el estado",
        folio="0035",
        institution=institution5,
        project=project4
    )

    #36
    add_permission(
        title=u"Permiso Federal",
        description=u"Permiso emitido por la Federación",
        folio="0036",
        institution=institution6,
        project=project4
    )

    #37
    add_permission(
        title=u"Permiso Qbit",
        description=u"Permiso emitido por el Qbit",
        folio="0037",
        institution=institution7,
        project=project4
    )

    #38
    add_permission(
        title=u"Permiso Museo de la Ciudad",
        description=u"Permiso emitido por el Museo de la Ciudad",
        folio="0038",
        institution=institution8,
        project=project4
    )

    #39
    add_permission(
        title=u"Permiso ITESM",
        description=u"Permiso emitido por el ITESM",
        folio="0039",
        institution=institution9,
        project=project4
    )

    #40
    add_permission(
        title=u"Permiso ITAM",
        description=u"Permiso emitido por el ITAM",
        folio="0040",
        institution=institution10,
        project=project4
    )

    #41
    add_permission(
        title=u"Permiso INAH",
        description=u"Permiso emitido por el INAH",
        folio="0041",
        institution=institution1,
        project=project5
    )

    #42
    add_permission(
        title=u"Permiso CEA",
        description=u"Permiso emitido por el CEA",
        folio="0042",
        institution=institution2,
        project=project5
    )

    #43
    add_permission(
        title=u"Permiso CFE",
        description=u"Permiso emitido por el CFE",
        folio="0043",
        institution=institution3,
        project=project5
    )

    #44
    add_permission(
        title=u"Permiso Municipio",
        description=u"Permiso emitido por el municipio",
        folio="0044",
        institution=institution4,
        project=project5
    )

    #45
    add_permission(
        title=u"Permiso Estado",
        description=u"Permiso emitido por el estado",
        folio="0045",
        institution=institution5,
        project=project5
    )

    #46
    add_permission(
        title=u"Permiso Federal",
        description=u"Permiso emitido por la Federación",
        folio="0046",
        institution=institution6,
        project=project5
    )

    #47
    add_permission(
        title=u"Permiso Qbit",
        description=u"Permiso emitido por el Qbit",
        folio="0047",
        institution=institution7,
        project=project5
    )

    #48
    add_permission(
        title=u"Permiso Museo de la Ciudad",
        description=u"Permiso emitido por el Museo de la Ciudad",
        folio="0048",
        institution=institution8,
        project=project5
    )

    #49
    add_permission(
        title=u"Permiso ITESM",
        description=u"Permiso emitido por el ITESM",
        folio="0049",
        institution=institution9,
        project=project5
    )

    #50
    add_permission(
        title=u"Permiso ITAM",
        description=u"Permiso emitido por el ITAM",
        folio="0050",
        institution=institution10,
        project=project5
    )
    ###############################################################################
    #
    #  Stages
    #
    ###############################################################################
    # REQUIRES: State, Project, Employee
    # 50 Registers / 5 per project (Los que alcancen)

    datetime1 = datetime.date(2015, 1, 9)
    datetime2 = datetime.date(2015, 2, 16)
    datetime3 = datetime.date(2015, 3, 24)
    datetime4 = datetime.date(2015, 4, 11)
    datetime5 = datetime.date(2015, 6, 15)
    datetime_late = datetime.date(2014, 11, 10)

    #1
    stage1_project1 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project1
    )
    stage1_project1.employee.add(employee1, employee2)

    #2
    stage2_project1 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project1
    )
    stage2_project1.employee.add(employee1, employee2)

    #3
    stage3_project1 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project1
    )
    stage3_project1.employee.add(employee1, employee2)

    #4
    stage4_project1 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project1
    )
    stage4_project1.employee.add(employee1, employee2)

    #5
    stage5_project1 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project1
    )
    stage5_project1.employee.add(employee3, employee4)

    #6
    stage1_project2 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project2
    )
    stage1_project2.employee.add(employee3, employee4)

    #7
    stage2_project2 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project2
    )
    stage2_project2.employee.add(employee3, employee4)

    #8
    stage3_project2 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project2
    )
    stage3_project2.employee.add(employee3, employee4)

    #9
    stage4_project2 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project2
    )
    stage4_project2.employee.add(employee5, employee6)

    #10
    stage5_project2 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project2
    )
    stage5_project2.employee.add(employee3, employee4)

    #11
    stage1_project3 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project3
    )
    stage1_project3.employee.add(employee5, employee6)

    #12
    stage2_project3 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project3
    )
    stage2_project3.employee.add(employee5, employee6)

    #13
    stage3_project3 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project3
    )
    stage3_project3.employee.add(employee5, employee6)

    #14
    stage4_project3 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project3
    )
    stage4_project3.employee.add(employee5, employee6)

    #15
    stage5_project3 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project3
    )
    stage5_project3.employee.add(employee5, employee6)

    #16
    stage1_project4 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project4
    )
    stage1_project4.employee.add(employee5, employee6)

    #17
    stage2_project4 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project4
    )
    stage2_project4.employee.add(employee1, employee2)

    #18
    stage3_project4 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project4
    )
    stage3_project4.employee.add(employee7, employee8)

    #19
    stage4_project4 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project4
    )
    stage4_project4.employee.add(employee7, employee8)

    #20
    stage5_project4 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project4
    )
    stage5_project4.employee.add(employee7, employee8)

    #21
    stage1_project5 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project5
    )
    stage1_project5.employee.add(employee7, employee8)

    #22
    stage2_project5 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime_late,
        state=delayed,
        project=project5
    )
    stage2_project5.employee.add(employee7, employee8)

    #23
    stage3_project5 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime_late,
        state=delayed,
        project=project5
    )
    stage3_project5.employee.add(employee7, employee8)

    #24
    stage4_project5 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime_late,
        state=delayed,
        project=project5
    )
    stage4_project5.employee.add(employee7, employee8)

    #25
    stage5_project5 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project5
    )
    stage5_project5.employee.add(employee7, employee8)

    #26
    stage1_project6 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=completed,
        project=project6
    )
    stage1_project6.employee.add(employee9, employee10)

    #27
    stage2_project6 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=completed,
        project=project6
    )
    stage2_project6.employee.add(employee9, employee10)

    #28
    stage3_project6 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=completed,
        project=project6
    )
    stage3_project6.employee.add(employee9, employee10)

    #29
    stage4_project6 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=completed,
        project=project6
    )
    stage4_project6.employee.add(employee9, employee10)

    #30
    stage5_project6 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=completed,
        project=project6
    )
    stage5_project6.employee.add(employee9, employee10)

    #31
    stage1_project7 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=completed,
        project=project7
    )
    stage1_project7.employee.add(employee11, employee12)

    #32
    stage2_project7 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=completed,
        project=project7
    )
    stage2_project7.employee.add(employee11, employee12)

    #33
    stage3_project7 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=completed,
        project=project8
    )
    stage3_project7.employee.add(employee11, employee12)

    #34
    stage4_project7 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=completed,
        project=project8
    )
    stage4_project7.employee.add(employee11, employee12)

    #35
    stage5_project7 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime3,
        state=completed,
        project=project8
    )
    stage5_project7.employee.add(employee11, employee12)

    #36
    stage1_project8 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=cancelled,
        project=project9
    )
    stage1_project8.employee.add(employee1, employee2)

    #37
    stage2_project8 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=cancelled,
        project=project9
    )
    stage2_project8.employee.add(employee1, employee2)

    #38
    stage3_project8 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=cancelled,
        project=project9
    )
    stage3_project8.employee.add(employee1, employee2)

    #39
    stage4_project8 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=cancelled,
        project=project4
    )
    stage4_project8.employee.add(employee1, employee2)

    #40
    stage5_project8 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=cancelled,
        project=project9
    )
    stage5_project8.employee.add(employee1, employee2)

    #41
    stage1_project9 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=cancelled,
        project=project10
    )
    stage1_project9.employee.add(employee3, employee4)

    #42
    stage2_project9 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=cancelled,
        project=project10
    )
    stage2_project9.employee.add(employee3, employee4)

    #43
    stage3_project9 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=cancelled,
        project=project10
    )
    stage3_project9.employee.add(employee3, employee4)

    #44
    stage4_project9 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=cancelled,
        project=project10
    )
    stage4_project9.employee.add(employee3, employee4)

    #45
    stage5_project9 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime3,
        state=cancelled,
        project=project10
    )
    stage5_project9.employee.add(employee3, employee4)

    #46
    stage1_project10 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project11
    )
    stage1_project10.employee.add(employee5, employee6)

    #47
    stage2_project10 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project11
    )
    stage2_project10.employee.add(employee5, employee6)

    #48
    stage3_project10 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project9
    )
    stage3_project10.employee.add(employee5, employee6)

    #49
    stage4_project10 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project11
    )
    stage4_project10.employee.add(employee5, employee6)

    #50
    stage5_project10 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project11
    )
    stage5_project10.employee.add(employee5, employee6)

    ###############################################################################
    #
    #  Comments
    #
    ###############################################################################
    # REQUIRES: Stage, Employee
    # 50 Registers / 2 per stage (Los que alcancen)

    datetime1 = datetime.datetime.now()

    #1
    add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage1_project1
    )

    #2
    add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage1_project1
    )

    #3
    add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage2_project1
    )

    #4
    add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage2_project1
    )

    #5
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage3_project1
    )

    #6
    add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage3_project1
    )

    #7
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage4_project1
    )

    #8
    add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage4_project1
    )

    #9
    add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage5_project1
    )

    #10
    add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage5_project1
    )

    #11
    add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage1_project2
    )

    #12
    add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage1_project2
    )

    #13
    add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage2_project2
    )

    #14
    add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage2_project2
    )

    #15
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage3_project2
    )

    #16
    add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage3_project2
    )

    #17
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage4_project2
    )

    #18
    add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage4_project2
    )

    #19
    add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage5_project2
    )

    #20
    add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage5_project2
    )

    #21
    add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage1_project3
    )

    #22
    add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage1_project3
    )

    #23
    add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage2_project3
    )

    #24
    add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage2_project3
    )

    #25
    add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage3_project3
    )

    #26
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage3_project3
    )

    #27
    add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage4_project3
    )

    #28
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage4_project3
    )

    #29
    add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage5_project3
    )

    #30
    add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage5_project3
    )

    #31
    add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage1_project4
    )

    #32
    add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage1_project4
    )

    #33
    add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage2_project4
    )

    #34
    add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage2_project4
    )

    #35
    add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage3_project4
    )

    #36
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage3_project4
    )

    #37
    add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage4_project4
    )

    #38
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage4_project4
    )

    #39
    add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage5_project4
    )

    #40
    add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage5_project4
    )

    #41
    add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage1_project5
    )

    #42
    add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage1_project5
    )

    #43
    add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage2_project5
    )

    #44
    add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage2_project5
    )

    #45
    add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage3_project5
    )

    #46
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage3_project5
    )

    #47
    add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage4_project5
    )

    #48
    add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage4_project5
    )

    #49
    add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage5_project5
    )

    #50
    add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage5_project5
    )

    ###############################################################################
    #
    #  Tasks
    #
    ###############################################################################
    # REQUIRES: Stage, Employee
    # 50 Registers / 2 per stage (Los que alcancen)

    datetime_test = datetime.date(2015, 1, 5)
    datetime_now = datetime.datetime.now()

    #1
    add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project1,
        employee=employee1
    )

    #2
    add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project1,
        employee=employee1
    )

    #3
    add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project1,
        employee=employee1
    )

    #4
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project1,
        employee=employee1
    )

    #5
    add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project1,
        employee=employee1
    )

    #6
    add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project1,
        employee=employee1
    )

    #7
    add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project1,
        employee=employee1
    )

    #8
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project1,
        employee=employee1
    )

    #9
    add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project1,
        employee=employee1
    )

    #10
    add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project1,
        employee=employee1
    )

    #11
    add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project2,
        employee=employee1
    )

    #12
    add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project2,
        employee=employee1
    )

    #13
    add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project2,
        employee=employee1
    )

    #14
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project2,
        employee=employee1
    )

    #15
    add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project2,
        employee=employee1
    )

    #16
    add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project2,
        employee=employee1
    )

    #17
    add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project2,
        employee=employee1
    )

    #18
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project2,
        employee=employee1
    )

    #19
    add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project2,
        employee=employee1
    )

    #20
    add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project2,
        employee=employee1
    )

    #21
    add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project3,
        employee=employee1
    )

    #22
    add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project3,
        employee=employee1
    )

    #23
    add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project3,
        employee=employee1
    )

    #24
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project3,
        employee=employee1
    )

    #25
    add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project3,
        employee=employee1
    )

    #26
    add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project3,
        employee=employee1
    )

    #27
    add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project3,
        employee=employee1
    )

    #28
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project3,
        employee=employee1
    )

    #29
    add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project3,
        employee=employee1
    )

    #30
    add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project3,
        employee=employee1
    )

    #31
    add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project4,
        employee=employee1
    )

    #32
    add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project4,
        employee=employee1
    )

    #33
    add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project4,
        employee=employee1
    )

    #34
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project4,
        employee=employee1
    )

    #35
    add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project4,
        employee=employee1
    )

    #36
    add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project4,
        employee=employee1
    )

    #37
    add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project4,
        employee=employee1
    )

    #38
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project4,
        employee=employee1
    )

    #39
    add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project4,
        employee=employee1
    )

    #40
    add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project4,
        employee=employee1
    )

    #41
    add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project5,
        employee=employee1
    )

    #42
    add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project5,
        employee=employee1
    )

    #43
    add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project5,
        employee=employee1
    )

    #44
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project5,
        employee=employee1
    )

    #45
    add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project5,
        employee=employee1
    )

    #46
    add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project5,
        employee=employee1
    )

    #47
    add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project5,
        employee=employee1
    )

    #48
    add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project5,
        employee=employee1
    )

    #49
    add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project5,
        employee=employee1
    )

    #50
    add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project5,
        employee=employee1
    )

    # Print out what we have added to the user.
    for institution in Institution.objects.all():
        print "Inserted Institution - {0}".format(str(institution))

    for project_type in ProjectType.objects.all():
        print "Inserted ProjectType - {0}".format(str(project_type))

    for state in State.objects.all():
        print "Inserted State - {0}".format(str(state))

    for employee in Employee.objects.all():
        print "Inserted Employee - {0}".format(str(employee))

    for project in Project.objects.all():
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
              project
):
    s = Stage.objects.get_or_create(name=name,
                                    description=description,
                                    number=number,
                                    deadline=deadline,
                                    state=state,
                                    project=project)[0]
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

django.setup()

if __name__ == '__main__':
    print "Starting SAPU population script..."
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sapu.settings")
    from sapu.models import Project, Institution, ProjectType, Permission, Stage, State, Employee, Comment, Task
    create_permissions()
    populate()



    ###############################################################################
    #
    #  States
    #
    ###############################################################################

    # sent
    sent = add_state(
        name=u"Solicitado",
        description=u"El permiso ha sido enviado a la institución y se espera aprobación.",
        color=u"#95C0FC"
    )

    # given
    given = add_state(
        name=u"Otorgado",
        description=u"La institución ha otorgado el permiso.",
        color=u"#6CE6A5"
    )

    # rejected
    rejected = add_state(
        name=u"Rechazado",
        description=u"El permiso no fue otorgado por la institución",
        color=u"#F3F163"
    )

    # pending
    pending = add_state(
        name=u"Pendiente",
        description=u"El permiso no se ha enviado para su aprobación.",
        color=u"#E47F91"
    )