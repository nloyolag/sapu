#coding:utf-8

# Django imports
import django.contrib.auth.models
import django.db.models
import datetime


class Institution (django.db.models.Model):

    phone = django.db.models.CharField(max_length=255, verbose_name=u"Teléfono")
    address = django.db.models.CharField(max_length=255, verbose_name=u"Dirección")
    email = django.db.models.EmailField(verbose_name=u"Email")
    is_client = django.db.models.BooleanField(default=None, verbose_name=u"¿Es cliente?")
    contact_point = django.db.models.CharField(max_length=255, verbose_name=u"Punto de Contacto")
    name = django.db.models.CharField(max_length=255, verbose_name=u"Nombre")
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")

    class Meta:

        verbose_name = u"Institución"
        verbose_name_plural = u"Instituciones"

    def __unicode__(self):

        return unicode(self.name)


class ProjectType (django.db.models.Model):

    name = django.db.models.CharField(max_length=255, verbose_name=u"Nombre")
    description = django.db.models.TextField(verbose_name=u"Descripción")
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")

    class Meta:

        verbose_name = u"Tipo de Proyecto"
        verbose_name_plural = u"Tipos de Proyecto"

    def __unicode__(self):

        return unicode(self.name)


class State (django.db.models.Model):
    number = django.db.models.CharField(max_length=255, verbose_name=u"Código de estado")
    name = django.db.models.CharField(max_length=20)
    description = django.db.models.CharField(max_length=255, verbose_name="Descripción")
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
                                        verbose_name=u"Foto")

    description = django.db.models.CharField(max_length=255,
                                             verbose_name="Descripción")

    folio = django.db.models.CharField(max_length=255, verbose_name=u"Folio de oficio de solicitud")

    institution = django.db.models.ForeignKey(Institution,
                                              on_delete=django.db.models.PROTECT,
                                              related_name="project_institution",
                                              verbose_name=u"Institución")

    project_type = django.db.models.ForeignKey(ProjectType,
                                               on_delete=django.db.models.PROTECT,
                                               related_name="project_project_type",
                                               verbose_name=u"Tipo de Proyecto")

    state = django.db.models.ForeignKey(State,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="project_state",
                                        verbose_name=u"Estado")

    class Meta:

        verbose_name = u"Proyecto"
        verbose_name_plural = u"Proyectos"

    def __unicode__(self):

        return unicode(self.name)


class Permission (django.db.models.Model):

    title = django.db.models.CharField(max_length=255, verbose_name=u"Titulo")
    description = django.db.models.TextField(verbose_name=u"Descripción")
    folio = django.db.models.CharField(max_length=255, verbose_name=u"Folio")
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")
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
                                        verbose_name=u"Foto")

    class Meta:

        verbose_name = u"Empleado"
        verbose_name_plural = u"Empleados"

    def __unicode__(self):

        return unicode(self.user.username)


class Stage (django.db.models.Model):
    name = django.db.models.CharField(max_length=255)
    description = django.db.models.CharField(max_length=255, verbose_name="Descripción")
    number = django.db.models.IntegerField(verbose_name="Número")
    is_active = django.db.models.BooleanField(default=True, verbose_name=u"¿Está activo?")
    deadline = \
        django.db.models.DateTimeField(verbose_name=u"Fecha Límite")

    employee = django.db.models.ManyToManyField(Employee,
                                                blank=True,
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
    description = django.db.models.TextField(verbose_name=u"Descripción")
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
        django.db.models.DateTimeField(verbose_name=u"Fecha de Completitud")

    is_complete = django.db.models.BooleanField(default=None,verbose_name=u"¿Está completada?")

    class Meta:

        verbose_name = u"Tarea"
        verbose_name_plural = u"Tareas"

    def __unicode__(self):

        return unicode(self.title)


class Permission_State (django.db.models.Model):
    number = django.db.models.CharField(max_length=255, verbose_name=u"Código de estado del permiso")
    name = django.db.models.CharField(max_length=20)
    description = django.db.models.CharField(max_length=255, verbose_name="Descripción")
    color = django.db.models.CharField(max_length=7)

    class Meta:

        verbose_name = u"Estado del permiso"
        verbose_name_plural = u"Estados de los permisos"

    def __unicode__(self):

        return unicode(self.name)