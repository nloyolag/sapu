#coding:utf-8

# Django imports
import django.contrib.auth.models
import django.db.models
import datetime

class Institution (django.db.models.Model):

    #phone, address, email, contact_point, name

class ProjectType (django.db.models.Model):

    #name, description

class Permission (django.db.models.Model):

    #title, folio, description

    #folio = django.db.models.CharField(unique=True, max_length=255, verbose_name=u"Folio")

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