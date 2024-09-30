from django.db import models

# Create your models here.
dictInstructores = {
    1: {"rut": "12345678-9", "nombre": "Juan Pérez", "categoria": "Entrenador Principal", "area": "Fútbol", "ubicacion": "Cancha principal", "fecha_ingreso": "2022-11-22"},
    2: {"rut": "98765432-1", "nombre": "María López", "categoria": "Entrenador Asistente", "area": "Básquetbol", "ubicacion": "Gimnasio", "fecha_ingreso": "2019-03-15"},
    3: {"rut": "87654321-0", "nombre": "Pedro Ramírez", "categoria": "Preparador Físico", "area": "Atletismo", "ubicacion": "Pista de atletismo", "fecha_ingreso": "2021-05-01"},
    4: {"rut": "76543210-9", "nombre": "Ana Torres", "categoria": "Entrenador Principal", "area": "Vóleibol", "ubicacion": "Gimnasio", "fecha_ingreso": "2018-08-12"},
    5: {"rut": "65432109-8", "nombre": "Luis Fernández", "categoria": "Entrenador Asistente", "area": "Fútbol", "ubicacion": "Cancha auxiliar", "fecha_ingreso": "2023-02-25"},
    6: {"rut": "54321098-7", "nombre": "Carla Rojas", "categoria": "Preparador Físico", "area": "Básquetbol", "ubicacion": "Gimnasio", "fecha_ingreso": "2020-11-18"},
    7: {"rut": "43210987-6", "nombre": "Jorge Morales", "categoria": "Entrenador Principal", "area": "Atletismo", "ubicacion": "Pista de atletismo", "fecha_ingreso": "2017-09-07"},
    8: {"rut": "32109876-5", "nombre": "Sofía Castillo", "categoria": "Entrenador Asistente", "area": "Vóleibol", "ubicacion": "Gimnasio", "fecha_ingreso": "2022-04-19"},
    9: {"rut": "21098765-4", "nombre": "Ricardo Soto", "categoria": "Preparador Físico", "area": "Fútbol", "ubicacion": "Sala de pesas", "fecha_ingreso": "2016-12-11"},
    10: {"rut": "10987654-3", "nombre": "Elena Vargas", "categoria": "Entrenador Principal", "area": "Básquetbol", "ubicacion": "Gimnasio", "fecha_ingreso": "2015-07-28"}
}

dictEquipos = {
    1: {"nombre": "Equipo 1", "estado": "Operativo", "modelo": "Model A1", "ubicacion": "Planta Norte"},
    2: {"nombre": "Equipo 2", "estado": "En mantenimiento", "modelo": "Model B2", "ubicacion": "Planta Sur"},
    3: {"nombre": "Equipo 3", "estado": "Operativo", "modelo": "Model C3", "ubicacion": "Planta Este"},
    4: {"nombre": "Equipo 4", "estado": "Falla", "modelo": "Model D4", "ubicacion": "Planta Oeste"},
    5: {"nombre": "Equipo 5", "estado": "Operativo", "modelo": "Model E5", "ubicacion": "Planta Norte"},
    6: {"nombre": "Equipo 6", "estado": "En mantenimiento", "modelo": "Model F6", "ubicacion": "Planta Sur"},
    7: {"nombre": "Equipo 7", "estado": "Operativo", "modelo": "Model G7", "ubicacion": "Planta Este"},
    8: {"nombre": "Equipo 8", "estado": "Falla", "modelo": "Model H8", "ubicacion": "Planta Oeste"},
    9: {"nombre": "Equipo 9", "estado": "Operativo", "modelo": "Model I9", "ubicacion": "Planta Norte"},
    10: {"nombre": "Equipo 10", "estado": "En mantenimiento", "modelo": "Model J10", "ubicacion": "Planta Sur"}
}

dictMantenciones = {
    1: {"fecha": "2024-09-01", "hora": "10:00", "ubicacion": "Planta Norte"},
    2: {"fecha": "2024-09-02", "hora": "12:30", "ubicacion": "Planta Sur"},
    3: {"fecha": "2024-09-03", "hora": "14:00", "ubicacion": "Planta Este"},
    4: {"fecha": "2024-09-04", "hora": "16:15", "ubicacion": "Planta Oeste"},
    5: {"fecha": "2024-09-05", "hora": "09:00", "ubicacion": "Planta Norte"},
    6: {"fecha": "2024-09-06", "hora": "11:45", "ubicacion": "Planta Sur"},
    7: {"fecha": "2024-09-07", "hora": "13:30", "ubicacion": "Planta Este"},
    8: {"fecha": "2024-09-08", "hora": "15:00", "ubicacion": "Planta Oeste"},
    9: {"fecha": "2024-09-09", "hora": "08:30", "ubicacion": "Planta Norte"},
    10: {"fecha": "2024-09-10", "hora": "10:45", "ubicacion": "Planta Sur"}
}
