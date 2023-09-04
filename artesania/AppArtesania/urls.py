from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from . import views



urlpatterns = [
    
    path('mate/list', MateList.as_view(), name="mates"),
    path('vidrio/list', VidrioList.as_view(), name="vidrios"),
    path('joyeria/list', JoyeriaList.as_view(), name="joyerias"),
    path('pintura/list', PinturaList.as_view(), name="pinturas"),
    path('especial/list', EspecialList.as_view(), name="especiales"),

    path('mateDetalle/<int:pk>/', MateDetalle.as_view(), name='mate'),
    path('vidrioDetalle/<int:pk>/', VidrioDetalle.as_view(), name='vidrio'),
    path('joyeriaDetalle/<int:pk>/', JoyeriaDetalle.as_view(), name='joyeria'),
    path('pinturaDetalle/<int:pk>/', PinturaDetalle.as_view(), name='pintura'),
    path('especialDetalle/<int:pk>/', EspecialDetalle.as_view(), name='especial'),

    path('mateEdicion/<int:pk>/', MateUpdate.as_view(), name='mate_editar'),
    path('vidrioEdicion/<int:pk>/', VidrioUpdate.as_view(), name='vidrio_editar'),
    path('joyeriaEdicion/<int:pk>/', JoyeriaUpdate.as_view(), name='joyeria_editar'),
    path('pinturaEdicion/<int:pk>/', PinturaUpdate.as_view(), name='pintura_editar'),
    path('especialEdicion/<int:pk>/', EspecialUpdate.as_view(), name='especial_editar'),

    path('matesBorrar/<int:pk>/', MateDelete.as_view(), name='mate_eliminar'),
    path('vidriosBorrar/<int:pk>/', VidrioDelete.as_view(), name='vidrio_eliminar'),
    path('joyeriasBorrar/<int:pk>/', JoyeriaDelete.as_view(), name='joyeria_eliminar'),
    path('pinturasBorrar/<int:pk>/', PinturaDelete.as_view(), name='pintura_eliminar'),
    path('especialesBorrar/<int:pk>/', EspecialDelete.as_view(), name='especial_eliminar'),

    path('mateDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('vidrioDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('joyeriaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('pinturaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('especialDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('artesaniaCreacion/', ArtesaniaCreacion.as_view(), name='nuevo'),
    path('buscar_artesanias/', buscar_artesanias, name="buscar_artesanias"),
    path('pages/', busqueda, name="busqueda"),
    path('detalle_artesania/<int:artesania_id>/', views.detalle_artesania, name='detalle_artesania')

    
]
   

