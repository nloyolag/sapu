from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static

import views
import settings

admin.autodiscover()

urlpatterns = patterns('',

    # ex: /admin/
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    #
    # Modals
    #

    # ex: /modal/edit/permission/3/stage/1/
    url(r'^modal/(?P<modal_action>\w+)/(?P<modal_element>\w+)/'
        r'(?P<element_index>\w+)/stage/(?P<stage_id>\w+)/$',
        views.generic_modal,
        name='modal-edit-stage'),

    # ex: /modal/edit/permission/3/project/1/
    url(r'^modal/(?P<modal_action>\w+)/(?P<modal_element>\w+)/'
        r'(?P<element_index>\w+)/project/(?P<project_id>\w+)/$',
        views.generic_modal,
        name='modal-edit-project'),

    # ex: /modal/add/permission/stage/1/
    url(r'^modal/(?P<modal_action>\w+)/'
        r'(?P<modal_element>\w+)/stage/(?P<stage_id>\w+)/$',
        views.generic_modal,
        name='modal-add-stage'),

    # ex: /modal/add/permission/project/1/
    url(r'^modal/(?P<modal_action>\w+)/'
        r'(?P<modal_element>\w+)/project/(?P<project_id>\w+)/$',
        views.generic_modal,
        name='modal-add-project'),

    # ex: /modal/edit/project/6/
    url(r'^modal/(?P<modal_action>\w+)/(?P<modal_element>\w+)/'
        r'(?P<element_index>\w+)/$',
        views.generic_modal,
        name='modal-edit'),

    # ex: /modal/add/project/
    url(r'^modal/(?P<modal_action>\w+)/(?P<modal_element>\w+)/$',
        views.generic_modal,
        name='modal-add'),

    #
    # Modals Delete
    #

    # ex: /delete/institution/3
    url(r'^delete/institution/(?P<institution_id>\d*)/$',
        views.delete_institution_view,
        name='delete-institution'),

    # ex: /delete/project_type/3
    url(r'^delete/project_type/(?P<project_type_id>\d*)/$',
        views.delete_project_type_view,
        name='delete-project-type'),

    # ex: /delete/project/3
    url(r'^delete/project/(?P<project_id>\d*)/$',
        views.delete_project_view,
        name='delete-project'),

    # ex: /delete/permission/3
    url(r'^delete/permission/(?P<permission_id>\d*)/$',
        views.delete_permission_view,
        name='delete-permission'),

    # ex: /delete/employee/3
    url(r'^delete/employee/(?P<employee_id>\d*)/$',
        views.delete_employee_view,
        name='delete-employee'),

    # ex: /delete/stage/3
    url(r'^delete/stage/(?P<stage_id>\d*)/$',
        views.delete_stage_view,
        name='delete-stage'),

    # ex: /delete/comment/3
    url(r'^delete/comment/(?P<comment_id>\d*)/$',
        views.delete_comment_view,
        name='delete-comment'),

    # ex: /delete/task/3
    url(r'^delete/task/(?P<task_id>\d*)/$',
        views.delete_task_view,
        name='delete-task'),

    #
    # Actions
    #

    #ex: /action-login/
    url(r'^action-login/', views.action_login, name='action-login'),

    #ex: /action-logout/
    url(r'^action-logout/', views.action_logout, name='action-logout'),

    #
    # Views
    #

    # ex: /
    url(r'^$', views.projects_render_view, name='home'),

    # ex: /login/
    url(r'^login/$', views.login_render_view, name='login'),

    # ex: /proyectos/
    url(r'^proyectos/$', views.projects_render_view, name='projects'),

    # ex: /usuarios/
    url(r'^usuarios/$', views.users_render_view, name='users'),

    # ex: /instituciones/
    url(r'^instituciones/$', views.institutions_render_view, name='institutions'),

    # ex: /tipos-de-proyecto/
    url(r'^tipos-de-proyecto/$', views.project_type_render_view, name='project-type'),

    # ex: /proyectos/132/
    url(r'^proyectos/(?P<project_id>\d+)/$', views.stages_render_view, name='stages'),

    # ex: /proyectos/132/3
    url(r'^proyectos/(?P<project_id>\d+)/(?P<stage_id>\d+)/$', views.stage_detail_render_view, name='stage-detail'),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
