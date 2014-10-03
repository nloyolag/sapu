from django.conf.urls import patterns, include, url

from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns('',

    #ex: /admin/
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    #
    # Modals
    #

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
