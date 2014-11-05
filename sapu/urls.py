from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static

import views
import settings

admin.autodiscover()

urlpatterns = patterns('',

    #ex: /admin/
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    #
    # Modals
    #

    # ex: /modal/

    # ex: /modal/restaurant/1/edit/category/6/
    # url(r'^modal/restaurant/(?P<restaurant_id>\d+)/'
    #     r'(?P<modal_action>\w+)/(?P<modal_element>\w+)/'
    #     r'(?P<element_index>\w+)/$',
    #     sellpad.views.generic_modal,
    #     name='modal_restaurant'),
    #
    # # ex: /modal/restaurant/1/edit/category/
    # url(r'^modal/restaurant/(?P<restaurant_id>\d+)/'
    #     r'(?P<modal_action>\w+)/(?P<modal_element>\w+)/$',
    #     sellpad.views.generic_modal,
    #     name='modal_restaurant'),
    #
    # # ex: /modal/edit/category/6/
    # url(r'^modal/(?P<modal_action>\w+)/(?P<modal_element>\w+)/'
    #     r'(?P<element_index>\w+)/$',
    #     sellpad.views.generic_modal,
    #     name='modal'),
    #
    # # ex: /modal/edit/category/
    # url(r'^modal/(?P<modal_action>\w+)/(?P<modal_element>\w+)/$',
    #     sellpad.views.generic_modal,
    #     name='modal'),

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
