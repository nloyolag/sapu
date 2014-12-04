#coding:utf-8

# Django imports
import django.contrib.auth.models
import django.db.models
import datetime


class Institution (django.db.models.Model):

    phone = django.db.models.CharField(max_length=255, verbose_name=u"Teléfono", blank=True)
    address = django.db.models.CharField(max_length=255, verbose_name=u"Dirección", blank=True)
    email = django.db.models.EmailField(verbose_name=u"Email", blank=True)
    is_client = django.db.models.BooleanField(default=None, verbose_name=u"¿Es cliente?")
    contact_point = django.db.models.CharField(max_length=255, verbose_name=u"Punto de Contacto", blank=True)
    name = django.db.models.CharField(max_length=255, verbose_name=u"Nombre")
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")

    class Meta:

        verbose_name = u"Institución"
        verbose_name_plural = u"Instituciones"

    def __unicode__(self):

        return unicode(self.name)


class ProjectType (django.db.models.Model):

    name = django.db.models.CharField(max_length=255, verbose_name=u"Nombre")
    description = django.db.models.TextField(verbose_name=u"Descripción", blank=True)
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")

    class Meta:

        verbose_name = u"Tipo de Proyecto"
        verbose_name_plural = u"Tipos de Proyecto"

    def __unicode__(self):

        return unicode(self.name)


class State (django.db.models.Model):
    number = django.db.models.IntegerField(verbose_name=u"Código de estado", unique=True)
    name = django.db.models.CharField(max_length=20)
    description = django.db.models.CharField(max_length=255, verbose_name=u"Descripción")
    color = django.db.models.CharField(max_length=7)
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")

    class Meta:

        verbose_name = u"Estado"
        verbose_name_plural = u"Estados"

    def __unicode__(self):

        return unicode(self.name)


class Project (django.db.models.Model):
    project_id = django.db.models.CharField(max_length=255, verbose_name=u"ID de Proyecto")
    creation_date = django.db.models.DateTimeField(verbose_name=u"Fecha de creación")
    deadline = django.db.models.DateTimeField(verbose_name=u"Fecha límite")
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")
    name = django.db.models.CharField(max_length=150,
                                      verbose_name=u"Proyecto")

    photo = django.db.models.ImageField(upload_to="photos/projects",
                                        verbose_name=u"Foto",
                                        default="photos/projects/default.jpg")

    description = django.db.models.TextField(verbose_name=u"Descripción",
                                             blank=True)

    folio = django.db.models.CharField(max_length=255, verbose_name=u"Folio de oficio de solicitud")

    institution = django.db.models.ForeignKey(Institution,
                                              on_delete=django.db.models.PROTECT,
                                              related_name="project_institution",
                                              verbose_name=u"Cliente",
                                              blank=True,
                                              null=True)

    project_type = django.db.models.ForeignKey(ProjectType,
                                               on_delete=django.db.models.PROTECT,
                                               related_name="project_project_type",
                                               verbose_name=u"Tipo de Proyecto",
                                               blank=True,
                                               null=True)

    state = django.db.models.ForeignKey(State,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="project_state",
                                        verbose_name=u"Estado")

    class Meta:

        verbose_name = u"Proyecto"
        verbose_name_plural = u"Proyectos"

    def __unicode__(self):

        return unicode(self.name)


class PermissionState (django.db.models.Model):
    number = django.db.models.IntegerField(verbose_name=u"Código de estado del permiso", unique=True)
    name = django.db.models.CharField(max_length=255)
    description = django.db.models.CharField(max_length=255, verbose_name=u"Descripción")
    color = django.db.models.CharField(max_length=7)

    class Meta:

        verbose_name = u"Estado del permiso"
        verbose_name_plural = u"Estados de los permisos"

    def __unicode__(self):

        return unicode(self.name)


class Permission (django.db.models.Model):

    title = django.db.models.CharField(max_length=255, verbose_name=u"Titulo")
    description = django.db.models.TextField(verbose_name=u"Descripción", blank=True)
    folio = django.db.models.CharField(max_length=255, verbose_name=u"Folio", blank=True)
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")
    permission_state = django.db.models.ForeignKey(PermissionState,
                                                   on_delete=django.db.models.PROTECT,
                                                   related_name="permission_permission_state",
                                                   verbose_name=u"Estado de permiso")
    institution = django.db.models.ForeignKey(Institution,
                                              on_delete=django.db.models.PROTECT,
                                              related_name="permission_institution",
                                              verbose_name=u"Institución")

    project = django.db.models.ForeignKey(Project,
                                          on_delete=django.db.models.PROTECT,
                                          related_name="permission_project",
                                          verbose_name=u"Proyecto")

    class Meta:

        verbose_name = u"Permiso"
        verbose_name_plural = u"Permisos"

    def __unicode__(self):

        return unicode(self.title)


class Employee (django.db.models.Model):

    user = django.db.models.OneToOneField(django.contrib.auth.models.User,
                                          on_delete=django.db.models.PROTECT,
                                          related_name="employee",
                                          verbose_name=u"Usuario")

    photo = django.db.models.ImageField(upload_to="photos/users",
                                        verbose_name=u"Foto",
                                        default="photos/users/default.png")

    logged = django.db.models.BooleanField(default=False, verbose_name=u"¿Se conectó hoy?")

    class Meta:

        verbose_name = u"Empleado"
        verbose_name_plural = u"Empleados"

    def __unicode__(self):

        return unicode(self.user.username)


class Stage (django.db.models.Model):
    name = django.db.models.CharField(max_length=255, verbose_name=u"Nombre")
    description = django.db.models.TextField(verbose_name=u"Descripción", blank=True)
    number = django.db.models.IntegerField(verbose_name=u"Número", blank=True)
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")
    creation_date = django.db.models.DateTimeField(verbose_name=u"Fecha de creación", blank=True)
    deadline = \
        django.db.models.DateTimeField(verbose_name=u"Fecha Límite")

    employee = django.db.models.ManyToManyField(Employee,
                                                blank=True,
                                                through="Assignment",
                                                related_name="stage_employees",
                                                verbose_name=u"Empleados")

    project = django.db.models.ForeignKey(Project,
                                          on_delete=django.db.models.PROTECT,
                                          related_name="stage_project",
                                          verbose_name=u"Proyecto")

    state = django.db.models.ForeignKey(State,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="stage_state",
                                        verbose_name=u"Estado")

    class Meta:

        verbose_name = u"Etapa"
        verbose_name_plural = u"Etapas"

    def __unicode__(self):

        return unicode(self.name)


class Assignment (django.db.models.Model):
    stage = django.db.models.ForeignKey(Stage,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="assignment_stage",
                                        null=True,
                                        verbose_name=u"Etapa")

    employee = django.db.models.ForeignKey(Employee,
                                           on_delete=django.db.models.PROTECT,
                                           related_name="assignment_employee",
                                           null=True,
                                           verbose_name=u"Empleado")

    completed = django.db.models.BooleanField(default=False, verbose_name=u"¿Completó la etapa?")

    class Meta:

        verbose_name = u"Asignación"
        verbose_name_plural = u"Asignaciones"

    def __unicode__(self):

        return unicode(self.stage.name + " - " + self.employee.user.first_name)


class Comment (django.db.models.Model):
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")
    stage = django.db.models.ForeignKey(Stage,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="comment_stage",
                                        verbose_name=u"Etapa")

    employee = django.db.models.ForeignKey(Employee,
                                           on_delete=django.db.models.PROTECT,
                                           related_name="comment_employee",
                                           verbose_name=u"Empleado")

    title = django.db.models.CharField(max_length=255, verbose_name=u"Título")
    description = django.db.models.TextField(verbose_name=u"Descripción", blank=True)
    date =\
        django.db.models.DateTimeField(verbose_name=u"Fecha")

    class Meta:

        verbose_name = u"Comentario"
        verbose_name_plural = u"Comentarios"

    def __unicode__(self):

        return unicode(self.title)


class Task (django.db.models.Model):
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")
    stage = django.db.models.ForeignKey(Stage,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="task_stage",
                                        verbose_name=u"Etapa")

    employee = django.db.models.ForeignKey(Employee,
                                           on_delete=django.db.models.PROTECT,
                                           related_name="task_employee",
                                           verbose_name=u"Empleado")

    title = django.db.models.CharField(max_length=255, verbose_name=u"Título")

    deadline =\
        django.db.models.DateTimeField(verbose_name=u"Fecha Límite")

    finished_date =\
        django.db.models.DateTimeField(verbose_name=u"Fecha de Completitud", blank=True, null=True)

    is_complete = django.db.models.BooleanField(default=False, verbose_name=u"¿Está completada?")

    class Meta:

        verbose_name = u"Tarea"
        verbose_name_plural = u"Tareas"

    def __unicode__(self):

        return unicode(self.title)

