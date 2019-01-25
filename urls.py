from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('home/', views.home, name = 'home'),
    path('calendar/', views.calendar, name='calendar'),
    path('chartjs/', views.chartjs, name='chartjs'),
    path('chartjs2/', views.chartjs2, name='chartjs2'),
    path('contacts/', views.contacts, name='contacts'),
    path('e_commerce/', views.e_commerce, name='e_commerce'),
    path('echarts/', views.echarts, name='echarts'),
    path('fixed_footer/', views.fixed_footer, name='fixed_footer'),
    path('fixed_sidebar/', views.fixed_sidebar, name='fixed_sidebar'),
    path('form/', views.form, name='form'),
    path('form_advanced/', views.form_advanced, name='form_advanced'),

    path('form_buttons/', views.form_buttons, name='form_buttons'),
    path('form_upload/', views.form_upload, name='form_upload'),
    path('form_validation/', views.form_validation, name='form_validation'),
    path('form_wizards/', views.form_wizards, name='form_wizards'),
    path('general_elements/', views.general_elements, name='general_elements'),
    path('glyphicons/', views.glyphicons, name='glyphicons'),
    path('icons/', views.icons, name='icons'),
    path('inbox/', views.inbox, name='inbox'),
    path('index/', views.index, name='index'),
    path('index2/', views.index2, name='index2'),

    path('index3/', views.index3, name='index3'),
    path('invoice/', views.invoice, name='invoice'),
    path('level2/', views.level2, name='level2'),
    path('login/', views.login, name='login'),
    path('map/', views.map, name='map'),
    path('media_gallery/', views.media_gallery, name='media_gallery'),
    path('morisjs/', views.morisjs, name='morisjs'),
    path('other_charts/', views.other_charts, name='other_charts'),
    path('page_403/', views.page_403, name='page_403'),
    path('page_404/', views.page_404, name='page_404'),

    path('page_500/', views.page_500, name='page_500'),
    path('plain_page/', views.plain_page, name='plain_page'),
    path('pricing_tables/', views.pricing_tables, name='pricing_tables'),
    path('profile/', views.profile, name='profile'),
    path('project_detail/', views.project_detail, name='project_detail'),
    path('projects/', views.projects, name='projects'),
    path('tables/', views.tables, name='tables'),
    path('tables_dynamic/', views.tables_dynamic, name='tables_dynamic'),
    path('typography/', views.typography, name='typography'),
    path('widgets/', views.widgets, name='widgets'),

    path('xx/', views.xx, name='xx'),

]