#coding:utf-8

# Django imports
import django.contrib.auth.models
import django.db.models
import datetime


class Institution (django.db.models.Model):

    phone = django.db.models.CharField(max_length=255, verbose_name=u"Teléfono")

    address = django.db.models.CharField(max_length=255, verbose_name=u"Dirección")
    #email (EmailField)
    contact_point = django.db.models.CharField(max_length=255, verbose_name=u"Punto de Contacto")
    name = django.db.models.CharField(max_length=255, verbose_name=u"Nombre")


class ProjectType (django.db.models.Model):

    name = django.db.models.CharField(max_length=255, verbose_name=u"Nombre")

    description = django.db.models.TextField(verbose_name=u"Descripción")


class Permission (django.db.models.Model):

    title = django.db.models.CharField(unique=True, max_length=255, verbose_name=u"Titulo")

    description = django.db.models.TextField(verbose_name=u"Descripción")

    folio = django.db.models.CharField(unique=True, max_length=255, verbose_name=u"Folio")

    institution = django.db.models.ForeignKey(Institution,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="institution",
                                        verbose_name=u"Institución")

    project = django.db.models.ForeignKey(Project,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="project",
                                        verbose_name=u"Proyecto")


class Stage (django.db.models.Model):
    name = django.db.models.CharField(max_length=255)
    description = django.db.models.CharField(max_length=255, verbose_name="Descripción")
    number = django.db.models.IntegerField(verbose_name="Número")
    deadline = \
        django.db.models.DateTimeField(verbose_name=u"Fecha Límite")

    class Meta:

        verbose_name = u"Etapa"
        verbose_name_plural = u"Etapas"

    def __unicode__(self):

        return unicode(self.name)


class State (django.db.models.Model):
    name = django.db.models.CharField(max_length=20)
    description = django.db.models.CharField(max_length=255, verbose_name="Descripción")
    color = django.db.models.CharField(max_length=7)

    class Meta:

        verbose_name = u"Estado"
        verbose_name_plural = u"Estados"

    def __unicode__(self):

        return unicode(self.name)


class Project (django.db.models.Model):
    project_id = django.db.models.CharField(max_length=255, verbose_name=u"ID de Proyecto")
    deadline = django.db.models.DateTimeField(verbose_name=u"Fecha límite")
    name = django.db.models.CharField(max_length=150,
                                      verbose_name=u"Proyecto")
    photo= django.db.models.ImageField(upload_to="photos/projects",
                                        verbose_name=u"Foto") 
    description = django.db.models.CharField(max_length=255,
                                               verbose_name="Descripción")
    folio = django.db.models.CharField( max_length=255, verbose_name=u"Folio de oficio de solicitud")

    class Meta:

        verbose_name = u"Estado"
        verbose_name_plural = u"Estados"

    def __unicode__(self):

        return unicode(self.name)


#class Role
#    employee = django.db.models.ForeignKey(Employee,
#                                           on_delete=django.db.models.PROTECT,
#                                           verbose_name=u"Usuario")
#    description = django.db.models.CharField(max_length=255,
#                                               verbose_name="Descripción")
#    name = django.db.models.CharField(max_length=50,
#                                               verbose_name="Tipo de Rol")


#class Privilege(django.db.models.Model)
#   name = django.db.models.CharField(max_length = 20, verbose_name="Privilegio")
    #PENDING
    #action = associated methods


class Employee (django.db.models.Model):

    stage = django.db.models.ManyToManyField(Stage,
                                             blank=True,
                                             related_name="stages",
                                             verbose_name=u"Etapas")

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


class Comment (django.db.models.Model):

    stage = django.db.models.ForeignKey(Stage,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="comments",
                                        verbose_name=u"Etapa")

    employee = django.db.models.ForeignKey(Employee,
                                           on_delete=django.db.models.PROTECT,
                                           related_name="comments",
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

    stage = django.db.models.ForeignKey(Stage,
                                        on_delete=django.db.models.PROTECT,
                                        related_name="tasks",
                                        verbose_name=u"Etapa")

    employee = django.db.models.ForeignKey(Employee,
                                           on_delete=django.db.models.PROTECT,
                                           related_name="tasks",
                                           verbose_name=u"Empleado")

    title = django.db.models.CharField(max_length=255, verbose_name=u"Título")

    deadline =\
        django.db.models.DateTimeField(verbose_name=u"Fecha Límite")

    finished_date =\
        django.db.models.DateTimeField(verbose_name=u"Fecha de Completitud")

    is_complete = django.db.models.BooleanField(default=False,
                                                verbose_name=u"¿Está completada?")

    class Meta:

        verbose_name = u"Tarea"
        verbose_name_plural = u"Tareas"

    def __unicode__(self):

        return unicode(self.title)
