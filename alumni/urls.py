""" school register URL Configuration"""
from django.urls import re_path
from .views import (
    AlumniList,
    AlumniRedirectMostrar,
    AlumniRetrieve,
    AlumniRetrievePadres,
    AlumniRetrieveAutorizado,
    AlumniRetrieveFinanzas,
    AlumniRetrieveDocumentos,
    AlumniRegister,
    AlumniRegisterPadres,
    AlumniRegisterAutorizado,
    AlumniRegisterFinanzas,
    AlumniRegisterDocumentos,
    AlumniUpdate,
    AlumniUpdatePadres,
    AlumniUpdateAutorizado,
    AlumniUpdateFinanzas,
    AlumniUpdateDocumentos,
    AlumniDelete
)

urlpatterns = [
    re_path(
        r'^$',
        AlumniList.as_view(),
        name='list'),
    re_path(
        r'^(?P<pk>\d+)$',
        AlumniRedirectMostrar.as_view(),
        name='redirect-show'),
    re_path(
        r'^mostrar/(?P<pk>\d+)$',
        AlumniRetrieve.as_view(),
        name='alumni-show'),
    re_path(
        r'^mostrar/padres/(?P<pk>\d+)$',
        AlumniRetrievePadres.as_view(),
        name='alumni-show-parents'),
    re_path(
        r'^mostrar/autorizado/(?P<pk>\d+)$',
        AlumniRetrieveAutorizado.as_view(),
        name='alumni-show-authorized'),
    re_path(
        r'^mostrar/finanzas/(?P<pk>\d+)$',
        AlumniRetrieveFinanzas.as_view(),
        name='alumni-show-finances'),
    re_path(
        r'^mostrar/documentos/(?P<pk>\d+)$',
        AlumniRetrieveDocumentos.as_view(),
        name='alumni-show-documents'),
    re_path(
        r'^inscripcion/$',
        AlumniRegister.as_view(),
        name='alumni-inscripcion'),
    re_path(
        r'^inscripcion/padres/(?P<pk>\d+)$',
        AlumniRegisterPadres.as_view(),
        name='alumni-inscripcion-padres'),
    re_path(
        r'^inscripcion/autorizado/(?P<pk>\d+)$',
        AlumniRegisterAutorizado.as_view(),
        name='alumni-inscripcion-autorizado'),
    re_path(
        r'^inscripcion/finanzas/(?P<pk>\d+)$',
        AlumniRegisterFinanzas.as_view(),
        name='alumni-inscripcion-finanzas'),
    re_path(
        r'^inscripcion/documentos/(?P<pk>\d+)$',
        AlumniRegisterDocumentos.as_view(),
        name='alumni-inscripcion-documentos'),
    re_path(
        r'^actualizar/(?P<pk>\d+)$',
        AlumniUpdate.as_view(),
        name='alumni-actualizar'),
    re_path(
        r'^actualizar/padres/(?P<pk>\d+)$',
        AlumniUpdatePadres.as_view(),
        name='alumni-actualizar-padres'),
    re_path(
        r'^actualizar/autorizado/(?P<pk>\d+)$',
        AlumniUpdateAutorizado.as_view(),
        name='alumni-actualizar-autorizado'),
    re_path(
        r'^actualizar/finanzas/(?P<pk>\d+)$',
        AlumniUpdateFinanzas.as_view(),
        name='alumni-actualizar-finanzas'),
    re_path(
        r'^actualizar/documentos/(?P<pk>\d+)$',
        AlumniUpdateDocumentos.as_view(),
        name='alumni-actualizar-documentos'),
    re_path(
        r'^borrar/(?P<pk>\d+)$',
        AlumniDelete.as_view(),
        name='alumni-borrar'),
]