#coding:utf-8

#Python imports

import os

#Django imports

import datetime


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
        description=u"El elemento se encuentra desarrollandose pero está retradado.",
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

    #1

    #employee1 = add_employee(

     #   from django.contrib.auth.models import User
     #   user1 = User.objects.create_user('Armando', 'armando@sapu.com','armando')
     #   photo1 = 'photos/users/test.jpg'
     #  employee = Employee(user=user1, photo=photo1)
    #)

    #user1.save()



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


    ###############################################################################
    #
    #  Stages
    #
    ###############################################################################
    # REQUIRES: State, Project, Employee
    # 50 Registers / 5 per project (Los que alcancen)

    #1
    stage1_project1 = add_stage(
        name = 'Investigación',
        description = 'Se hará levantamiento de medidas en la localidad y se',
        #number
        #deadline
        #state
        #project
        #employee
    )
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

    # for employee in Employee.objects.all():
    #     print "Inserted Employee - {0}".format(str(employee))

    for project in Institution.objects.all():
        print "Inserted Project - {0}".format(str(project))

        # for permission in Permission.objects.filter(project=project):
        #     print "    Inserted Permission - {0}".format(str(permission))
        #
        # for stage in Stage.objects.filter(project=project):
        #     print "    Inserted Stage - {0}".format(str(stage))
        #
        #     for comment in Comment.objects.filter(stage=stage):
        #         print "        Comment - {0}".format(str(comment))
        #
        #     for task in Task.objects.filter(stage=stage):
        #         print "        Task - {0}".format(str(task))


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
