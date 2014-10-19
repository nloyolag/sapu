#coding:utf-8

#Python imports

import os
import datetime

#Django imports

from django.contrib.auth.models import User


def populate():
    #TODO Add multiple employees to stage

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
        name=u"En tiempo",
        description=u"El elemento se encuentra desarrollandose y a tiempo con respecto la fecha de entrega.",
        color=u"#95C0FC"
    )

    # delayed
    delayed = add_state(
        name=u"Retrasado",
        description=u"El elemento se encuentra desarrollandose pero está retrasado",
        color=u"#F3F163"
    )

    # cancelled
    cancelled = add_state(
        name=u"Cancelado",
        description=u"El elemento no se terminó o ha sido pospuesto.",
        color=u"#E47F91"
    )

    # completed
    completed = add_state(
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
    photo_test = 'photos/users/test.jpg'

    #1
    employee1 = add_employee(
        user1=User.objects.create_user('Armando', 'armando@sapu.com', 'armando'),
        photo=photo_test
    )
    employee1.save()

    #2
    employee2 = add_employee(
        user2=User.objects.create_user('Baltasar', 'baltasar@sapu.com','baltasar'),
        photo=photo_test
    )
    employee2.save()

    #3
    employee3 = add_employee(
        user3=User.objects.create_user('Carlos', 'carlos@sapu.com','carlos'),
        photo=photo_test
    )
    employee3.save()

    #4
    employee4 = add_employee(
        user4=User.objects.create_user('Daniel', 'daniel@sapu.com','daniel'),
        photo=photo_test
    )

    #5
    employee5 = add_employee(
        user5=User.objects.create_user('Eleazar', 'eleazar@sapu.com','eleazar'),
        photo=photo_test
    )

    employee5.save()

    #6
    employee6 = add_employee(
        user6=User.objects.create_user('Felipe', 'felipe@sapu.com','felipe'),
        photo=photo_test
    )
    employee6.save()

    #7
    employee7 = add_employee(
        user7=User.objects.create_user('Guillermo', 'guillermo@sapu.com','guillermo'),
        photo=photo_test
    )
    employee7.save()

    #8
    employee8 = add_employee(
        user8=User.objects.create_user('Hermenegildo', 'hermenegildo@sapu.com','hermenegildo'),
        photo=photo_test
    )
    employee8.save()

    #9
    employee9 = add_employee(
        user9=User.objects.create_user(u'Ileana', 'ileana@sapu.com','ileana'),
        photo=photo_test
    )

    #10
    employee10 = add_employee(
        user10=User.objects.create_user(u'Jonathan', 'jonathan@sapu.com','jonathan'),
        photo=photo_test
    )

    #11
    employee11 = add_employee(
        user11=User.objects.create_user(u'Katia', 'katia@sapu.com','katia'),
        photo=photo_test
    )
    employee11.save()

    #12
    employee12 = add_employee(
        user12=User.objects.create_user(u'Laura', 'laura@sapu.com','laura'),
        photo=photo_test
    )
    employee12.save()

    #13
    employee13 = add_employee(
        user13=User.objects.create_user(u'Mauro', 'mauro@sapu.com','mauro'),
        photo=photo_test
    )
    employee13.save()

    #14
    add_employee(
        user14=User.objects.create_user(u'Nazarín', 'nazarin@sapu.com','nazarin'),
        photo=photo_test
    )

    #15
    employee15 = add_employee(
        user15=User.objects.create_user('Olaf', 'olaf@sapu.com','olaf'),
        photo=photo_test
    )

    ###############################################################################
    #
    #  Projects
    #
    ###############################################################################
    # REQUIRES: Institution, ProjectType, State
    # 50 Registers

    datetime1 = datetime.datetime.now()

    # 1
    project1 = add_project(
        project_id=u"A1",
        deadline=datetime1,
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
        project=project1,
        employee=employee1
    )

    #2
    stage2_project1 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project1,
        employee=employee2
    )

    #3
    stage3_project1 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project1,
        employee=employee1
    )

    #4
    stage4_project1 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project1,
        employee=employee1
    )

    #5
    stage5_project1 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project1,
        employee=employee3
    )

    #6
    stage1_project2 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project2,
        employee=employee4
    )

    #7
    stage2_project2 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project2,
        employee=employee2
    )

    #8
    stage3_project2 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project2,
        employee=employee10
    )

    #9
    stage4_project2 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project2,
        employee=employee6
    )

    #10
    stage5_project2 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project2,
        employee=employee3
    )

    #11
    stage1_project3 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project3,
        employee=employee1
    )

    #12
    stage2_project3 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project3,
        employee=employee2
    )

    #13
    stage3_project3 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project3,
        employee=employee1
    )

    #14
    stage4_project3 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project3,
        employee=employee1
    )

    #15
    stage5_project4 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project3,
        employee=employee3
    )

    #16
    stage1_project4 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project4,
        employee=employee6
    )

    #17
    stage2_project4 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project4,
        employee=employee2
    )

    #18
    stage3_project4 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project4,
        employee=employee10
    )

    #19
    stage4_project4 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project4,
        employee=employee4
    )

    #20
    stage5_project4 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project = project4,
        employee = employee3
    )

    #21
    stage1_project5 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project5,
        employee=employee1
    )

    #22
    stage2_project5 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime_late,
        state=delayed,
        project=project5,
        employee=employee2
    )

    #23
    stage3_project5 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime_late,
        state=delayed,
        project=project5,
        employee=employee1
    )

    #24
    stage4_project5 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime_late,
        state=delayed,
        project=project5,
        employee=employee1
        )

    #25
    stage5_project5 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project5,
        employee=employee3
    )

    #26
    stage1_project6 = add_stage(
        name = 'Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=completed,
        project=project6,
        employee=employee4
    )

    #27
    stage2_project6 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=completed,
        project=project6,
        employee=employee2
    )

    #28
    stage3_project6 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=completed,
        project=project6,
        employee=employee10
    )

    #29
    stage4_project6 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=completed,
        project=project6,
        employee=employee6
    )

    #30
    stage5_project6 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=completed,
        project=project6,
        employee=employee3
        )

    #31
    stage1_project7 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=completed,
        project=project7,
        employee=employee1
    )

    #32
    stage2_project7 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=completed,
        project=project7,
        employee=employee2
    )

    #33
    stage3_project8 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=completed,
        project=project8,
        employee=employee1
    )

    #34
    stage4_project8 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=completed,
        project=project8,
        employee=employee1
    )

    #35
    stage5_project8 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime3,
        state=completed,
        project=project8,
        employee=employee13
    )

    #36
    stage1_project9 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=cancelled,
        project=project9,
        employee=employee12
    )

    #37
    stage2_project9=add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=cancelled,
        project=project9,
        employee=employee2
    )

    #38
    stage3_project9 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=cancelled,
        project=project9,
        employee=employee10
    )

    #39
    stage4_project9 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=cancelled,
        project=project4,
        employee=employee9
    )

    #40
    stage5_project9 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=cancelled,
        project=project9,
        employee=employee3
    )

    #41
    stage1_project10 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=cancelled,
        project=project10,
        employee=employee1
    )

    #42
    stage2_project10 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=cancelled,
        project=project10,
        employee=employee2
    )

    #43
    stage3_project10 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=cancelled,
        project=project10,
        employee=employee1
    )

    #44
    stage4_project10 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=cancelled,
        project=project10,
        employee=employee10
    )

    #45
    stage5_project10 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime3,
        state=cancelled,
        project=project10,
        employee=employee13
    )

    #46
    stage1_project11 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=1,
        deadline=datetime1,
        state=on_time,
        project=project11,
        employee=employee12
    )

    #47
    stage2_project11 = add_stage(
        name='Planos',
        description='Se dibujarán los planos de la estructura general',
        number=2,
        deadline=datetime2,
        state=on_time,
        project=project11,
        employee=employee2
    )

    #48
    stage3_project11 = add_stage(
        name='Investigación',
        description='Se hará levantamiento de medidas en la localidad y se',
        number=3,
        deadline=datetime3,
        state=on_time,
        project=project9,
        employee=employee11
    )

    #49
    stage4_project11 = add_stage(
        name='Cimientos',
        description='Se construirán los cimientos',
        number=4,
        deadline=datetime4,
        state=on_time,
        project=project11,
        employee=employee11
    )

    #50
    stage5_project11 = add_stage(
        name='Hidráulica',
        description='Se construirá la instalación hidráulica',
        number=5,
        deadline=datetime5,
        state=on_time,
        project=project11,
        employee=employee3
    )

    ###############################################################################
    #
    #  Comments
    #
    ###############################################################################
    # REQUIRES: Stage, Employee
    # 50 Registers / 2 per stage (Los que alcancen)

    datetime1 = datetime.datetime.now()

    #1
    comment1 = add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage1
    )

    #2
    comment2 = add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage1
    )

    #3
    comment3 = add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage2
    )

    #4
    comment4 = add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage2
    )

    #5
    comment5 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage3
    )

    #6
    comment6 = add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage3
    )

    #7
    comment7 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage4
    )

    #8
    comment8 = add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage4
    )

    #9
    comment9 = add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage5
    )

    #10
    comment10 = add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage5
    )

    #11
    comment11 = add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage6
    )

    #12
    comment12 = add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage6
    )

    #13
    comment13 = add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage7
    )

    #14
    comment14 = add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage7
    )

    #15
    comment15 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage8
    )

    #16
    comment16 = add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage8
    )

    #17
    comment17 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage9
    )

    #18
    comment18 = add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage9
    )

    #19
    comment19 = add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage10
    )

    #20
    comment20 = add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage10
    )

    #21
    comment21 = add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage11
    )

    #22
    comment22 = add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage11
    )

    #23
    comment23 = add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage12
    )

    #24
    comment24 = add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage12
    )

    #25
    comment25 = add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage13
    )

    #26
    comment26 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage13
    )

    #27
    comment27 = add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage14
    )

    #28
    comment28 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage14
    )

    #29
    comment29 = add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage15
    )

    #30
    comment30 = add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage15
    )

    #31
    comment31 = add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage16
    )

    #32
    comment32 = add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage16
    )

    #33
    comment33 = add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage17
    )

    #34
    comment34 = add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage17
    )

    #35
    comment35 = add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage18
    )

    #36
    comment36 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage18
    )

    #37
    comment37 = add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage19
    )

    #38
    comment38 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage19
    )

    #39
    comment39 = add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage20
    )

    #40
    comment40 = add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage20
    )

    #41
    comment41 = add_comment(
        title=u"Limpiar",
        description=u"Dejar limpio el lugar",
        date=datetime1,
        employee=employee2,
        stage=stage21
    )

    #42
    comment42 = add_comment(
        title=u"Enviar solicitud",
        description=u"Enviar la solicitud de permiso al instituto",
        date=datetime1,
        employee=employee1,
        stage=stage21
    )

    #43
    comment43 = add_comment(
        title=u"Pedir materiales",
        description=u"Enviar el pedido de materiales al distribuidor autorizado",
        date=datetime1,
        employee=employee2,
        stage=stage22
    )

    #44
    comment44 = add_comment(
        title=u"Reunirse con el director",
        description=u"Asistir a la reunion con el director del lugar",
        date=datetime1,
        employee=employee1,
        stage=stage22
    )

    #45
    comment45 = add_comment(
        title=u"Delegar asignaciones",
        description=u"Establecer asignaciones de trabajo a los empleados",
        date=datetime1,
        employee=employee2,
        stage=stage23
    )

    #46
    comment46 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage23
    )

    #47
    comment47 = add_comment(
        title=u"Hacer planos",
        description=u"Hacer la propuesta de los planos del proyecto",
        date=datetime1,
        employee=employee2,
        stage=stage24
    )

    #48
    comment48 = add_comment(
        title=u"Reportar avances",
        description=u"Reportar los avances del proyecto hasta este punto",
        date=datetime1,
        employee=employee1,
        stage=stage24
    )

    #49
    comment49 = add_comment(
        title=u"Instalar tuberias",
        description=u"Realizar las instalaciones de las tuberias",
        date=datetime1,
        employee=employee2,
        stage=stage25
    )

    #50
    comment50 = add_comment(
        title=u"Instalar cables",
        description=u"Instalar los cables de luz",
        date=datetime1,
        employee=employee1,
        stage=stage25
    )

    ###############################################################################
    #
    #  Tasks
    #
    ###############################################################################
    # REQUIRES: Stage, Employee
    # 50 Registers / 2 per stage (Los que alcancen)

    datetime_test = datetime.date(2015, 1, 5)
    datetime_now = datetime.datetime()

    #1
    task1 = add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project1,
        employee=employee1
    )

    #2
    task2 = add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project1,
        employee=employee1
    )

    #3
    task3 = add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project1,
        employee=employee1
    )

    #4
    task4 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project1,
        employee=employee1
    )

    #5
    task5 = add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project1,
        employee=employee1
    )

    #6
    task6 = add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project1,
        employee=employee1
    )

    #7
    task7 = add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project1,
        employee=employee1
    )

    #8
    task8 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project1,
        employee=employee1
    )

    #9
    task9 = add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project1,
        employee=employee1
    )

    #10
    task10 = add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project1,
        employee=employee1
    )

    #11
    task11 = add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project2,
        employee=employee1
    )

    #12
    task12 = add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project2,
        employee=employee1
    )

    #13
    task13 = add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project2,
        employee=employee1
    )

    #14
    task14 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project2,
        employee=employee1
    )

    #15
    task15 = add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project2,
        employee=employee1
    )

    #16
    task16 = add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project2,
        employee=employee1
    )

    #17
    task17 = add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project2,
        employee=employee1
    )

    #18
    task18 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project2,
        employee=employee1
    )

    #19
    task19 = add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project2,
        employee=employee1
    )

    #20
    task20 = add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project2,
        employee=employee1
    )

    #21
    task21 = add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project3,
        employee=employee1
    )

    #22
    task22 = add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project3,
        employee=employee1
    )

    #23
    task23 = add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project3,
        employee=employee1
    )

    #24
    task24 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project3,
        employee=employee1
    )

    #25
    task25 = add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage = stage3_project3,
        employee=employee1
    )

    #26
    task26 = add_task(
        title = u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project3,
        employee=employee1
    )

    #27
    task27 = add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project3,
        employee=employee1
    )

    #28
    task28 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project3,
        employee=employee1
    )

    #29
    task29 = add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project3,
        employee=employee1
    )

    #30
    task30 = add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project3,
        employee=employee1
    )

    #31
    task31 = add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project4,
        employee=employee1
    )

    #32
    task32 = add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project4,
        employee=employee1
    )

    #33
    task33 = add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project4,
        employee=employee1
    )

    #34
    task34 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project4,
        employee=employee1
    )

    #35
    task35 = add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project4,
        employee=employee1
    )

    #36
    task36 = add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project4,
        employee=employee1
    )

    #37
    task37 = add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project4,
        employee=employee1
    )

    #38
    task38 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project4,
        employee=employee1
    )

    #39
    task39 = add_task(
        title=u'Cotizar iluminación',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project4,
        employee=employee1
    )

    #40
    task40 = add_task(
        title=u'Instalar jardinería',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage5_project4,
        employee=employee1
    )

    #41
    task41 = add_task(
        title=u'Hacer planos',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project5,
        employee=employee1
    )

    #42
    task42 = add_task(
        title=u'Sacar permiso CEA',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage1_project5,
        employee=employee1
    )

    #43
    task43 = add_task(
        title=u'Cotizar metales',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project5,
        employee=employee1
    )

    #44
    task44 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage2_project5,
        employee=employee1
    )

    #45
    task45 = add_task(
        title=u'Montar instalación eléctrica básica',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project5,
        employee=employee1
    )

    #46
    task46 = add_task(
        title=u'Conectar generador',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage3_project5,
        employee=employee1
    )

    #47
    task47 = add_task(
        title=u'Instalar tuberías',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project5,
        employee=employee1
    )

    #48
    task48 = add_task(
        title=u'Contactar compañía de concreto',
        deadline=datetime_test,
        finished_date=datetime_now,
        is_complete=True,
        stage=stage4_project5,
        employee=employee1
    )

    #49
    task49 = add_task(
        title = u'Cotizar iluminación',
        deadline = datetime_test,
        finished_date = datetime_now,
        is_complete = True,
        stage = stage5_project5,
        employee = employee1
    )

    #50
    task50 = add_task(
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
        description,
        folio,
        project_type,
        institution,
        state
):
    p = Project.objects.get_or_create(project_id=project_id,
                                      deadline=deadline,
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
