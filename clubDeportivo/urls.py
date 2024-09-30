from django.urls import path
from clubDeportivo import views as vista

urlpatterns = [
    path('inicio/', vista.inicio, name='inicio'),
    path('dashboard/', vista.dashboard, name='dashboard'),

    path('inventarioequipos/', vista.inventarioequipos, name='inventarioequipos'),
    path('equipo/', vista.equipo, name='crear_equipo'),  
    path('equipo/<int:id>/', vista.equipo, name='editar_equipo'),
    path('equipo/eliminar/<int:id>/', vista.eliminar_equipo, name='eliminar_equipo'),
  
    path('mantenciones/', vista.mantenciones, name='mantenciones'),
    path('mantencion/', vista.mantencion, name='crear_mantencion'),
    path('mantencion/<int:id>/', vista.mantencion, name='editar_mantencion'),
    path('mantencion/eliminar/<int:id>/', vista.eliminar_mantencion, name='eliminar_mantencion'),

    path('mantenciones/calendario/', vista.calendario, name='calendario'),
    

    path('instructores/', vista.instructores, name='instructores'),
    path('instructor/', vista.instructor, name='crear_instructor'),
    path('instructor/<int:id>/', vista.instructor, name='editar_instructor'),
    path('instructor/eliminar/<int:id>/', vista.eliminar_instructor, name='eliminar_instructor'),
]
