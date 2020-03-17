"""marketproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from marketapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
	path('tovar/', views.tovar_view, name='tovar-view'),
	path('sklad/', views.sklad_view, name='sklad-view'),
	path('postavschik/', views.postavschik_view, name='postavschik-view'),
	path('postavka/', views.postavka_view, name='postavka-view'),

    path('tovar/add/', views.tovaradd, name='tovaradd'),
    path('tovar/edit/<int:tovar_id>/', views.tovaredit, name='tovaredit'),
    path('tovar/delete/<int:tovar_id>/', views.tovardelete, name='tovardelete'),
    path('api/tovar/', views.TovarList.as_view()),
    re_path(r'^api/tovar/(?P<pk>\d+)/$', views.TovarDetail.as_view()),
    path('tovar/csv/', views.tovar_csv, name='tovar_csv'),


    path('sklad/add/', views.skladadd, name='skladadd'),
    path('sklad/edit/<int:sklad_id>/', views.skladedit, name='skladedit'),
    path('sklad/delete/<int:sklad_id>/', views.skladdelete, name='skladdelete'),
    path('api/sklad/', views.SkladList.as_view()),
    re_path(r'^api/sklad/(?P<pk>\d+)/$', views.SkladDetail.as_view()),
    path('sklad/csv/', views.sklad_csv, name='sklad_csv'),

    path('postavka/add/', views.postavkaadd, name='postavkaadd'),
    path('postavka/edit/<int:postavka_id>/', views.postavkaedit, name='postavkaedit'),
    path('postavka/delete/<int:postavka_id>/', views.postavkadelete, name='postavkadelete'),
    path('api/postavka/', views.PostavkaList.as_view()),
    re_path(r'^api/postavka/(?P<pk>\d+)/$', views.PostavkaDetail.as_view()),
    path('postavka/csv/', views.postavka_csv, name='postavka_csv'),
    
    path('postavschik/add/', views.postavschikadd, name='postavschikadd'),
    path('postavschik/edit/<int:postavschik_id>/', views.postavschikedit, name='postavschikedit'),
    path('postavschik/delete/<int:postavschik_id>/', views.postavschikdelete, name='postavschikdelete'),
    path('api/postavschik/', views.PostavschikList.as_view()),
    re_path(r'^api/postavschik/(?P<pk>\d+)/$', views.PostavschikDetail.as_view()),
    path('postavschik/csv/', views.postavschik_csv, name='postavschik_csv'),
]
